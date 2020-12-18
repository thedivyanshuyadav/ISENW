from django.shortcuts import render,HttpResponse

# Create your views here.
from .models import File
from .webscrap import scrap

from django.conf import settings
from django.core.files.storage import FileSystemStorage

# import the necessary packages
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import Xception,ResNet50,DenseNet201
from tensorflow.keras.applications.xception import preprocess_input
from tensorflow.keras.applications.xception import decode_predictions
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import matplotlib.pyplot as plt
import matplotlib as mpl
import urllib,os
import requests

model = Xception()
model.load_weights('templates/modelweight/xception_weight.h5')


def index(request):
    fname=''
    toupload=True
    result=''
    if request.method == 'POST':
        if('filebtn' in request.POST and 'myfile' in request.FILES):
            myfile = request.FILES['myfile']
            myfile.name='upload.jpg'
            document=File.objects.create(file=myfile)
            document.save()
            fname=myfile.name
        elif('urlbtn' in request.POST and request.POST['urltext']):
            urlname = request.POST['urltext']
            print(urlname)
            fname='urlimage.jpg'
            opener = urllib.request.URLopener()
            opener.addheader('User-Agent', 'whatever')
            opener.retrieve(urlname, 'media\\icml\\images\\'+fname)

        else:
            return render(request, 'icml/index.html',
                          {
                              'toupload': toupload,
                              'imgpath': os.path.join(settings.MEDIA_URL, 'icml/images/' + fname),
                              'MEDIA_URL': settings.MEDIA_URL,
                              'prediction': result,
                              'predictedPie': os.path.join(settings.MEDIA_URL, 'icml/predictedPie/prediction.png'),
                              'info': scrap(result[0][0][1]) if (result) else '',
                              'title': result[0][0][1].replace('_', ' ') if (result) else ''
                          })

        print(os.path.join(settings.MEDIA_URL,'icml/images/'+fname))
        # Xception Model
        IMAGE_PATH ='media\\icml\\images\\' + fname
        img = image.load_img(IMAGE_PATH, target_size=(224, 224))
        img = image.img_to_array(img)
        img = preprocess_input(img)
        predictions = model.predict(np.array([img]))
        result=decode_predictions(predictions, top=3)
        toupload=False

        val = [result[0][0][2],result[0][1][2],result[0][2][2]]
        lbl = [result[0][0][1],result[0][1][1],result[0][2][1]]
        fig, ax = plt.subplots(nrows=1, ncols=1)  # create figure & 1 axi

        color = ['orange', 'teal', 'red','skyblue']
        lbl.append('Others')
        val.append(1-sum(val))

        ax.bar(lbl,val,color=color)
        ax.set_ylim(0.0, 1.0)
        ax.set_title('Probability')

        ax.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=False)

        handles = [plt.Rectangle((0, 0), 1, 1, color=color[i]) for i in range(4)]
        ax.legend(handles, lbl,fontsize=15)

        fig.savefig(os.path.join(settings.BASE_DIR, 'media\\icml\\predictedPie\\prediction.png'), format='png')

    if (result):
        title=result[0][0][1].replace('_', ' ')
        info = scrap(result[0][0][1])
        if (val[0] < 0.4):
            title = 'Sorry , Can\'t recognise it.'
            info='No Info available as Image is not recognised.'
        elif (val[0] < 0.5):
            title += '    (Not sure)'

    else:
        info=''
        title=''

    print('\n\n',title,result,'\n\n')
    return render(request, 'icml/index.html',{'toupload':toupload,'imgpath':os.path.join(settings.MEDIA_URL,'icml/images/'+fname),'MEDIA_URL':settings.MEDIA_URL,
                                              'prediction':result,'predictedPie':os.path.join(settings.MEDIA_URL,'icml/predictedPie/prediction.png'),'info':info,'title':title})
