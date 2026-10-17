
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


function play() {

    if (vid.paused) {

        vid.play();

        titre_video.style.height = "250px";
        titre_video.style.left = "2%";
        titre_video.style.top = "52%";

        texte_intro.style.opacity = "0";

    }
    
    else {

        vid.pause();

        titre_video.style.height = "400px";
        titre_video.style.left = "2%";
        titre_video.style.top = "20%";

        texte_intro.style.opacity = "1";
    }
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

let Images = document.querySelector('.e_image');
let Droite = document.getElementById('fle-droite');
let Gauche = document.getElementById('fle-gauche');
let Rectangle = document.querySelector('.rectangle_affichage');
let carouselOffset = 0;
let carouselHover = false;

function largeurPasCarousel() {
    const premierElement = Images.firstElementChild;
    if (!premierElement) return 410;

    const largeur = premierElement.getBoundingClientRect().width;
    const style = getComputedStyle(Images);
    const gap = parseFloat(style.columnGap || style.gap) || 10;

        return (largeur + gap) * 2;
}

function offsetMaximumCarousel() {
    return Math.max(0, Images.scrollWidth - Rectangle.clientWidth + 20);
}

function mettreAJourFleches() {
    if (!carouselHover) {
        Gauche.style.opacity = "0";
        Droite.style.opacity = "0";
        return;
    }

    const max = offsetMaximumCarousel();
    Gauche.style.opacity = carouselOffset > 1 ? "1" : "0";
    Droite.style.opacity = carouselOffset < max - 1 ? "1" : "0";
}

function appliquerPositionCarousel() {
    const max = offsetMaximumCarousel();
    carouselOffset = Math.max(0, Math.min(carouselOffset, max));
    Images.style.transform = `translateX(${-carouselOffset}px)`;
    mettreAJourFleches();
}

Droite.addEventListener('click', function() {
    carouselOffset += largeurPasCarousel();
    appliquerPositionCarousel();
});

Gauche.addEventListener('click', function() {
    carouselOffset -= largeurPasCarousel();
    appliquerPositionCarousel();
});

Rectangle.addEventListener("mouseover", function() {
    carouselHover = true;
    mettreAJourFleches();
});

Rectangle.addEventListener("mouseleave", function() {
    carouselHover = false;
    mettreAJourFleches();
});

window.addEventListener('resize', appliquerPositionCarousel);
appliquerPositionCarousel();


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
