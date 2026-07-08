
window.addEventListener('scroll',background);
let vid = document.querySelector("video")

function background()
    {
    
        if (window.scrollY <10){

        document.querySelector(".table").style.background='linear-gradient(black, rgba(18, 18, 18, 0) 85%)';
        

        
        
        }
        else{
        document.querySelector(".table").style.background='rgba(18, 18, 18,1)';
        }

        if (window.scrollY >450){
        vid.pause();
        titre_video.style.height="400px";
        titre_video.style.top="20%";
        setTimeout(function(){
                
                texte_intro.style.opacity="1";
                
        }, 500);
        }
        
    }


let playy = document.getElementById("play")
playy.addEventListener("click", play)
let titre_video = document.getElementById("image_video");
let texte_intro = document.getElementById("texte_introductif");


function play()
    {
        if (vid.paused){

            vid.play();

            setTimeout(function(){

                titre_video.style.height="250px";
                titre_video.style.left="2%";
                titre_video.style.top="52%";
        
            }, 2000);

            setTimeout(function(){
                texte_intro.style.opacity="0";}, 1800);
        
        }

            
        
        else{
            vid.pause();
            titre_video.style.height="400px";
            titre_video.style.top="20%";
            setTimeout(function(){
                
                texte_intro.style.opacity="1";
                
            }, 500)}

        }







let image= document.querySelector(".imge");
let contenant= document.querySelector(".content");
let description= document.querySelector(".description");
let affi;

image.addEventListener("mouseover", function(){
    
    affi=setTimeout(affichage, 400);

    }

)


function affichage(){
    
            image.style.cursor="pointer";
            contenant.style.backgroundImage="linear-gradient(black, rgba(18, 18, 18,1) 11%)";
            contenant.style.scale="1.2";
            contenant.style.boxShadow="0px 8px 16px 0px rgba(40, 42, 42,1)";
            contenant.style.left="2%";

            description.style.opacity="1";
            description.style.pointerEvents="auto";
            description.style.cursor="default";
        }

contenant.addEventListener("mouseleave", enlever)


function enlever(){image.style.scale="1.0";
clearTimeout(affi);

    contenant.style.backgroundImage="linear-gradient(black, rgba(18, 18, 18,0) 11%)";
    contenant.style.scale="1";
    contenant.style.boxShadow="0px 8px 16px 0px rgba(40, 42, 42,0)";
    contenant.style.left="0%";


    description.style.opacity="0";
    description.style.pointerEvents="none";
}

let films= document.querySelectorAll(".Titre");
let film_descrip= document.querySelectorAll(".apparition")


for ( let i=0; i< films.length; i++){
    films[i].style.cursor="pointer";

            
    films[i].addEventListener("mouseover", function(){
        film_descrip[i].style.width="130px";
        film_descrip[i].style.opacity="1";

        

    
    });

    films[i].addEventListener("mouseleave", function(){
        film_descrip[i].style.width="100px";
        film_descrip[i].style.opacity="0";
    
        

    });

}

        
document.querySelector('.e_image').style.left='0px';
let Images=document.querySelector('.e_image');
let Droite=document.getElementById('fle-droite');
Droite.addEventListener('click',function(){
  console.log('Flèche droite');
  let pos=parseInt(Images.style.left);
  pos-=410;
  if(pos<-412*3.5){pos=-412*3.5;}
  Images.style.left=pos+'px';
});

let Gauche=document.getElementById('fle-gauche');
Gauche.addEventListener('click',function(){
  console.log('Flèche gauche');
  let pos=parseInt(Images.style.left);
  pos+=410;
  if(pos>0){pos=0;}
  Images.style.left=pos+'px';
});

let Rectangle = document.querySelector(".rectangle_affichage");

Rectangle.addEventListener("mouseover", function(){
    let pos = parseInt(Images.style.left) || 0; 
    if (pos < 0) {
        Gauche.style.opacity = "1";} 
    else {
        Gauche.style.opacity = "0";}
    if (pos > -412 * 3.5) {
        Droite.style.opacity = "1";} 
    else {
        Droite.style.opacity = "0";}
});
  Rectangle.addEventListener("mouseleave", function(){
    Droite.style.opacity="0";
    Gauche.style.opacity="0";
 });


 let input= document.getElementById("Recherche");

document.addEventListener("click", function(event) {
    if (event.target.nodeName === "INPUT") {
        input.style.width= "250px"; 
        input.style.border= "1px solid white"; 
        input.style.backgroundColor= " #181818"
    } 
    else {
        input.style.width= "0px";
        input.style.border= "none";
        input.style.backgroundColor= "transparent"
    }
});

input.addEventListener("mouseover", ()=>{input.style.backgroundColor= "#989797";})
input.addEventListener("mouseleave", ()=>{input.style.backgroundColor= "transparent";})
