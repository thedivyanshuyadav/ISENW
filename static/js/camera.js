'use script';

// Get the modal
const modal = document.getElementById("Modal");
const span = document.getElementsByClassName("close")[0];


const video=document.getElementById("video")
const canvas=document.getElementById("canvas")
const snap=document.getElementById("snap")
const errorMsgElement=document.getElementById("spanErrorMsg")

const retake=document.getElementById("retake");
const go=document.getElementById("go");

function b64toBlob(b64Data, contentType, sliceSize) {
    contentType = contentType || '';
    sliceSize = sliceSize || 512;

    var byteCharacters = atob(b64Data); // window.atob(b64Data)
    var byteArrays = [];

    for (var offset = 0; offset < byteCharacters.length; offset += sliceSize) {
        var slice = byteCharacters.slice(offset, offset + sliceSize);

        var byteNumbers = new Array(slice.length);
        for (var i = 0; i < slice.length; i++) {
            byteNumbers[i] = slice.charCodeAt(i);
        }

        var byteArray = new Uint8Array(byteNumbers);

        byteArrays.push(byteArray);
    }

    var blob = new Blob(byteArrays, {type: contentType});
    return blob;
}



const constraints={
    audio:false,
    video:true
}


async function init(){
    try{
        const stream=await navigator.mediaDevices.getUserMedia(constraints);
        handleSuccess(stream);
    }
    catch(e){
        errorMsgElement.innerHTML=`navigator.getUserMedia.error:${e.toString()}`;
    }
}

function handleSuccess(stream){
    window.stream=stream;
    video.srcObject=stream;
}

const context=canvas.getContext('2d');
snap.addEventListener("click",function (){
    context.drawImage(video,0,0,640,480);
    canvas.style.display="block";
    go.style.display="block";
    retake.style.display="block";
    video.style.display="none";
    snap.style.display="none";

})

retake.addEventListener("click",function (){
    canvas.style.display="none";
    go.style.display="none";
    retake.style.display="none";
    video.style.display="block";
    snap.style.display="block";
});
go.addEventListener("click",function () {
    var imgData = context.getImageData(0, 0, 640, 480);
    var data={
        "image":imgData,
    }
    $.redirect('/result/',data);
});

const useCameraBtn=document.getElementById("useCamera");
useCameraBtn.addEventListener("click", function (){
    init();
    modal.style.display = "block";
})





// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


