const btnMamou = document.getElementById('btn')
const mensagemMamou = document.querySelectorAll('.mamaou')

const cores = ["#FF5733", "#33FF57", "#3357FF", "#FF33F6", "#F6FF33"];
const corAleatoria = cores[Math.floor(Math.random() * cores.length)];

numero = 1

function mamou() {

    btnMamou.classList.add("piscar");
    
    document.body.style.backgroundColor = cores[Math.floor(Math.random() * cores.length)];
    console.log(mensagemMamou) //.classList.add('show')
   
    if (numero == 1) {
        document.getElementById("musica").play();
        mensagemMamou[0].classList.add('show')
        btnMamou.innerText = "MAMAR"
    }
    if (numero == 2){
        mensagemMamou[0].innerText = "Mamou de novo!!! :-O"
    }
    if (numero == 3) {
        mensagemMamou[0].innerText = `É o MAMAS?? Já mamou ${numero} vezes`
    }
    if (numero > 3) {
        mensagemMamou[0].innerText = `Contagem de mamadas do MAMAS: ${numero} `
    }

    setTimeout(function() {
        btnMamou.classList.remove("piscar");
    }, 1000);

    numero++
}

btnMamou.addEventListener('click', mamou)