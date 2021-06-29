import io
import json
import os

import matplotlib.pyplot as plt
import numpy as np
import requests
import wikipedia
from PIL import Image
from django.conf import settings
from django.shortcuts import render, redirect
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import decode_predictions
from tensorflow.keras.applications.resnet50 import preprocess_input

from .forms import ContentForm

wikipedia.set_lang("en")
INPUT_SHAPE = (224, 224, 3)
model = ResNet50(weights=None,input_shape=INPUT_SHAPE)
model.load_weights('isenw_app/modelweight/resnet50_weights_tf_dim_ordering_tf_kernels.h5')


# Create your views here.
def home(request):
    valid = True
    request.session.modified = True
    context = dict()
    form = ContentForm(request.POST or None, request.FILES or None)
    if request.method == "POST":

        if form.is_valid():
            image = form.cleaned_data.get("image")
            form.cleaned_data['bin_image'] = image.read()
            request.session['image_name'] = image._name
            request.session['image'] = form.cleaned_data['bin_image'].decode('ISO-8859-1')

        elif 'urlbtn' in request.POST and request.POST['urltext']:

            url = request.POST['urltext']
            try:
                contents = requests.get(url, stream=True).content
                print(type(contents))
                request.session['image'] = contents.decode("ISO-8859-1")

            except Exception as e:
                if e.__dict__['response'] is None:
                    valid = False

        if valid:
            request.session['camera'] = False
            return redirect('result/')
        else:
            request.session['camera']=True

    context['form'] = form
    context['valid'] = valid
    return render(request, "home.html", context=context)


def result(request):
    print(request.POST.get('camera'), request.session.get('camera'))
    if request.POST.get('camera') or request.session.get('camera'):
        if request.POST.get("camera"):
            img_arr = list(json.loads(request.POST['image']).values())
            request.session['image'] = request.POST['image']
        else:
            img_arr = list(json.loads(request.session.get('image')).values())

        img_arr = np.array(img_arr).reshape((186, 224, 4))
        img_arr = img_arr[:, :, :-1]
        img = img_arr.astype(np.uint8)
        imge = Image.fromarray(img)
        request.session['camera'] = True

    else:
        u_image = request.session['image'].encode("ISO-8859-1")
        print('[GOT IMAGE] : ', type(u_image))
        stream = io.BytesIO(u_image)

        imge = Image.open(stream)
        img = np.array(imge)

    imge.save('isenw_app/uploads/image.png')

    img = preprocess_input(img)
    img = np.resize(img, (1,) + img.shape)

    predictions = model.predict(img)
    print(decode_predictions(predictions, top=10))

    top_results = decode_predictions(predictions, top=4)

    val = [top_results[0][0][2], top_results[0][1][2], top_results[0][2][2], top_results[0][3][2]]
    lbl = [top_results[0][0][1], top_results[0][1][1], top_results[0][2][1], top_results[0][3][1]]
    fig, ax = plt.subplots(nrows=1, ncols=1)  # create figure & 1 axi
    color = ['orange', 'teal', 'red', 'skyblue']
    # lbl.append('Others')
    # val.append(1 - sum(val))
    ax.bar(lbl, val, color=color)
    ax.set_ylim(0.0, 1.0)
    ax.set_title('Probability')
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    handles = [plt.Rectangle((0, 0), 1, 1, color=color[i]) for i in range(4)]
    ax.legend(handles, lbl, fontsize=15)
    fig.savefig('isenw_app/uploads/result.png', format='png')

    title = top_results[0][0][1].replace('_', ' ')
    keyword = top_results[0][0][1]
    print(keyword)
    try:
        page = wikipedia.page(title=keyword, auto_suggest=False)
        info = page.content
    except Exception:
        page = wikipedia.page(title=keyword, auto_suggest=True)

        info = page.content
    print(page)
    print(top_results)

    if top_results[0][0][2] < 0.02:
        title = 'Unknown'
        info = 'No info available'
    elif top_results[0][0][2] < 0.04:
        title = title + '  <h6>(Not sure)</h6>'

    context = {'imgpath': os.path.join(settings.UPLOAD_URL, 'image.png'),
               'prediction': top_results,
               'predictedPie': os.path.join(settings.UPLOAD_URL, 'result.png'),
               'info': info,
               'title': title}

    return render(request, "result.html", context=context)
