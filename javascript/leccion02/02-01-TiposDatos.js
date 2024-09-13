// Tipos de Datos en JavaScrip
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es idéntica.
*/
// Tipo Stream (Str)
var nombre = 'Gabriel'; 
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre)
// Tipo Numérico
var numero = 3000; 
console.log(numero);
// Tipo Object
var objeto = {
    nombre : "Gabriel",
    apellido : "Bruni",
    telefono : "2604-400867"
}

console.log(objeto);

// Tipo de Boolean
var bandera = true
console.log(typeof bandera)

// Tipo de dato Función
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo de dato Symbol
var simbolo = Symbol("Mi símbolo");
console.log(simbolo);

// Tipo de dato Clase (Es una Función)
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona)

// Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

// null: signifuca ausencia de valor
var y = null; // null no es un tipo de dato, pero su origen es de tipo object
console.log(typeof y);

// Tipo de dato array y Empty String
var autos = ['Citroen','Audi','BMW','Ford']
console.log(autos);
console.log(typeof autos); // Preguntamos que tipo de dato es:

var z = '';
console.log(z); // Esto se refiere a que es una cadena vacía: 
console.log(typeof z);
