var dadosProcessados =[];

fetch('./homunculario.csv')
.then(response => response.text())
.then(data => {
    const linhas = data.split("\n");
    for (const linha of linhas){
        const valores = linha.split(",");
        dadosProcessados.push(valores);
    }
})

let diff = 0
var HabilidadesEscolhidas = []
var HabilidadesRepetidas = []
var QuantCaract = 0


function escolherDificuldade(DificuldadeEscrita){
    if (DificuldadeEscrita== "facil"){
        QuantCaract = 3
        diff = 3
    }else if(DificuldadeEscrita == "normal"){
        QuantCaract = 4
        diff = 6
    }else if(DificuldadeEscrita == "dificil"){
        QuantCaract = 5
        diff = 9
    }else if(DificuldadeEscrita == "extrema"){
        QuantCaract = 6
        diff = 12
    }
    return [diff, QuantCaract]
}

function Habis (diff){
    var aleatorio = Math.floor(Math.random()*diff) +1
    var linhaEscolhida = dadosProcessados[aleatorio]
    var Escolhido = linhaEscolhida[Math.floor(Math.random() * linhaEscolhida.length )]

    while(HabilidadesEscolhidas.indexOf(Escolhido) > 0){
        var aleatorio = Math.floor(Math.random()*diff) +1
        var linhaEscolhida = dadosProcessados[aleatorio]
        var Escolhido = linhaEscolhida[Math.floor(Math.random() * linhaEscolhida.length )]
    }

    HabilidadesEscolhidas.push(Escolhido)
  }

function iniciar(){
    HabilidadesEscolhidas = []
    diff = 0
    QuantCaract = 0
    var campo = document.getElementById('campo')
    var escritaDif = document.getElementById("a").value
    var habilidadeExtra = parseInt(document.getElementById("b").value)
   
    var total = Math.floor(habilidadeExtra/6)
    let criatura = escolherDificuldade(escritaDif)

    while (HabilidadesEscolhidas.length < criatura[1] + total){
        Habis(criatura[0])
    }

    campo.innerHTML = HabilidadesEscolhidas
}