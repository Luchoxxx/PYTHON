
//alert("Hola mundo");
// Variables

let numero_secreto = Math.floor(Math.random()*10) + 1;
let numero_usuario = 0;
let intentos = 1;
let max_intentos=3;
//let palabraVeces ="vez"
console.log(numero_secreto);
while (numero_usuario != numero_secreto) {
            
    numero_usuario = parseInt(prompt("Me indicas un numero entre 1 al 10"));
    console.log(numero_usuario);

    // Condicion de comparacion
    if (numero_usuario== numero_secreto) {
        alert(`Acertaste el numero fue ${numero_usuario} . Lo acertaste en ${intentos} ${intentos==1?"vez":"veces"}`);
    
    }else{
        
        if (numero_usuario > numero_secreto) {
        alert("El numero es menor")
        //  alert("El numero no fue asertado");
        }else{
            alert("El numero es mayor");
        } 
        // incrementamos contador cuando no acierta
        intentos ++;
        //palabraVeces = "veces";
        if (intentos > max_intentos) {
             alert(`Alcansaste el maximo de ${intentos} intentos`);
            break;            
        }
    }
}






