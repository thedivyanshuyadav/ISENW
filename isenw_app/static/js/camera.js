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


video.addEventListener('loadedmetadata', function() {
            context.translate(video.videoWidth, 0);
            context.scale(-1, 1);
         });

const constraints={
    audio:false,
    video:{
        width:640,height:480
    },
}


async function init(){
    try{
        canvas.style.display="none";
        go.style.display="none";
        retake.style.display="none";
        video.style.display="block";
        snap.style.display="block";
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


function postwith (to,p) {
  var myForm = document.createElement("form");
  myForm.method="post" ;
  myForm.action = to ;
  for (var k in p) {
    var myInput = document.createElement("input") ;
    myInput.setAttribute("name", k) ;
    myInput.setAttribute("value", p[k]);
    myForm.appendChild(myInput) ;
  }
  document.body.appendChild(myForm) ;
  myForm.submit() ;
  document.body.removeChild(myForm) ;
}

go.addEventListener("click",function () {

    video.src="";
    window.stream.getTracks()[0].stop();

    var imgData = context.getImageData(0, 0, 640, 480).data;
    var data={
            "csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val(),
            "image":JSON.stringify(imgData),
            "camera":true,
        }
    postwith('result/',data);

});

const useCameraBtn=document.getElementById("useCamera");
useCameraBtn.addEventListener("click", function (){
    init();
    modal.style.display = "block";
})





// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";

  video.src="";
  window.stream.getTracks()[0].stop();

}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


