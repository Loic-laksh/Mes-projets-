let inputNom=document.querySelector('#nom');
let inputLogin=document.querySelector('#login');
let inputEmail=document.querySelector('#email');
let inputMdp=document.querySelector('#mdp');
let inputConfirmation=document.querySelector('#confirmation');

inputNom.addEventListener('keyup',function(event) 
{
   console.log('Touche nom relâchée');
   let texte=inputNom.value;
   texte=texte.toLowerCase();
   texte=texte.replace(/[^a-z]/g,'-');
   inputLogin.value=texte;
   let erreur=document.querySelector('#erreur-nom');
   if(/^[a-zA-Z' ]+$/.test(inputNom.value)){erreur.style.opacity=0;}
   else{erreur.style.opacity=1;}
});

inputMdp.addEventListener('keyup',function(event) 
{
   console.log('Touche mot de passe relâchée');
   let erreur=document.querySelector('#erreur-mdp');
   if(inputMdp.value.length<6){erreur.style.opacity=1;}
   else{erreur.style.opacity=0;}
   let erreurConfirmation=document.querySelector('#erreur-confirmation');
   if(inputMdp.value==inputConfirmation.value){erreurConfirmation.style.opacity=0;}
   else {erreurConfirmation.style.opacity=1;}
});

inputConfirmation.addEventListener('keyup',function(event) 
{
   console.log('Touche confirmation relâchée');
   let erreurConfirmation=document.querySelector('#erreur-confirmation');
   if(inputMdp.value==inputConfirmation.value){erreurConfirmation.style.opacity=0;}
   else {erreurConfirmation.style.opacity=1;}
});

inputEmail.addEventListener('keyup',function(event) 
{
   console.log('Touche email relâchée');
   let erreur=document.querySelector('#erreur-email');
   if(/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(inputEmail.value)){erreur.style.opacity=0;}
   else {erreur.style.opacity=1;}
});