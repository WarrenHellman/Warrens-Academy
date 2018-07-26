// #############################
// ########The Console##########
// #############################

// Dev Tools in Chrome- open with f12

// Can write JS in the console in Dev Tools (doesn't save)

document.querySelector('h1').style.color = 'red' // will make all h1 elements red 

console.table() // will show a table of an object literal
console.error() // will show an error in console log, useful to flag an error for you
// console.warning() // will show a warning in console log
//console.clear() // clears it out
//console.time('anyName')


//console.timeEnd('anyName') // logs the time in between the start (time) and end (timeEnd)

// #############################
// ########Variables############
// #############################

// var, (since es6) let, const

// var- try to phase out

// let- can be initialized without a value

// const- cannont be initialized without a value or reassigned to another primitive value (although you can change arrays and objects.) You should use const unless it is inappropriate (if you need it initialized without a value, in a for loop, or some functions)!! It will help keep your data from being accidentally altered. 


// #############################
// ########Data Types###########
// #############################

// Primative Data Types- Stored directly in the location the variable accesses. Stored on the stack

// Reference Data Types- Accessed by reference, stored on the heap with a pointer 

// Primatives- String, number, Boolean, null, undefined, Symbols (ES6)

// JS is dynamically typed (you can changes the data type of a variable at will). Typescript makes it statically typed (like Java, C#, C++)

// Primitive Types:
// STRING
const name = 'John Doe';
// NUM
const age = 45
// Boolean
const hasKids=true;
// null
const car = null;
// undefined
let test;
// Symbol, new primative type
const sym = Symbol()

// REFERENCE TYPE (object)
// Array
const hobbies = ['movies', 'music']
// Object Literal
const address = {
    city: 'Boston',
    state: 'MA'
}
const today = new Date();

// To check the data type, use console.log(typeof variable);

// #############################
// ########Type Conversion######
// #############################

let val;

// Number to String

val = String(555)
val = String (4+4)

// Boolean to string
val = String(true)

// date to string
val = String(new Date())

// array to string
val = String([1,2,3,4])

// toString() method
val = (5).toString();

//String to number
val = Number('5')
val = Number(true) //= 1 // can be used for logical operators
val = Number(false) //= 0
val = Number(null) //= 0
val = Number('hello') //= NaN

val = parseInt('100.3') //= 100 //(whole number integer from string)
val = parseFloat('100.3') //= 100.3 //for the parseFloat


// #############################
// #######Type Coersion#########
// #############################

// JavaScript can coerce type if not clear

const val1 = 5
const val2 = 6
const sum = val1 + val2// = 11, number

const val3 = String(5)
const val4 = 6
const sum1 = val3 + val4 //= 56 //, string (it concatenates the two numbers but coerces 6 into a string)

// #############################
// #######Math Object###########
// #############################

const num1 = 100;
const num2 = 50;


//Simple math with numbers

val = num1 + num2
val = num1 * num2

// Math Object

val = Math.PI; // gives a value of PI
val = Math.round(2.8); //rounds to 3
val = Math.floor(2.8); //gives 2
val = Math.ceil(2.3); // gives 3
val = Math.sqrt ()// square root
val = Math.abs(-3) //gives 3
val = Math.random(); //Gives a pseudo random number between 0-1
val = Math.floor(Math.random() * 100 +1 ) //gives a whole number between 1 and 100. 


// #############################
// #######String Methods########
// #############################

const firstName = 'Will';
const lastName = 'John';


//Concatenation
val = firstName + ' ' + lastName;

//Append
val = 'Brad ';
val += 'Traversy' ; // appends to the string

//Escaping

val = 'That\'s awesome and I can\'t wait' //the single quotes mess it up, could use double quotes or escape w/ a backslash \ in front of the quotes


//length
val = firstName.length; // 4

//concat
val = firstName.concat(' ', lastName); // concatenates the two

//Change changes
val = firstName.toUpperCase(); //capitalizes
val = firstName.toLowerCase(); //lowers

val = firstName[2]; //returns 3rd letter

//indexOf()

val = firstName.indexOf('l') //gives 2, first 'l'
val = firstName.lastIndexOf('l') //gives 3 for the last index of 'l' in Will

//charAt()

val = firstName.charAt('2'); //gives 'l', at index 2 of Will
val = firstName.charAt(firstName.length-1);

//substring()

val = firstName.substring(0,2); // Wi

//slice() 
val = firstName.slice(0,2);//will do the same as substring and return 'Wi'
val = firstName.slice(-2); // actually returns last two characters. 

//split()
str= 'Hello there, my name is Brad';
val = str.split(' '); //creates an array where each index is split by the character added (in this case a space)

//replace();
val = str.replace('Brad', 'Jack') // first argument is found, replaced by second argument

//includes()
val = str.includes('Brad') // true, returns a boolean if it is found

// #############################
// #######Template Literal######
// #############################

const name1= 'John'
const age1 = 30
const job1 = 'Web Developer'
const city1 = 'Miami'
let html;

//without template strings (es5)
html = '<ul><li>Name: '+name1+'</li><li>Age: '+age1+ '</li><li>Job: '+job1+'</li><li>City: '+city1+'</li></ul>'

//With Template strings, uses variables in between ${variable} nested inside of ``, or grave accent

html = `
<ul>
    <li>Name: ${name}</li>
    <li>Age: ${age}</li>
    <li>Job: ${job1}</li>
    <li>City: ${city1}</li>
    <li>${2+2}</li>
    <li>${function hello(){}}</li>
</ul>
`;

document.body.innerHTML = html;

// #############################
// #######Arrays################
// #############################

//Create arrays
const numbers = [32, 4, 7, 77];
//or
const numbers2 = new Array(22,45,22,66,54);   //using an array constructor
const fruit = ['nana', 'strawb', 'appa']
val = numbers.length // check length

// check if is array

val = Array.isArray(numbers) //returns true

val =numbers[3] //returns value at index 3

//insert into array
numbers[2] = 69 //changes value

val = numbers.indexOf(4) //returns 1, the index of 4

//Mutating Arrays

//add to back
numbers.push(250) //adds 250 to end of array

// add to front
numbers.unshift(90);

//take off from end
numbers.pop();

//take off from front 
numbers.shift();

//splice values
numbers.splice(1,1) //gives start position and end position. This only removes 1 index

//reverse
numbers.reverse();

//concatenate array
val = numbers.concat(numbers2) //adds both arrays together

//sorting arrays

//val = numbers.sort(fruit) //sorts alphabetically. Will not sort numbers correctly because of it sorts by first number only!

//user compare function to sort numbers
val = numbers.sort(function(x,y){
    return x-y;
});

//reverse sort
val = numbers.sort(function(x,y){
    return y-x;
});

//find
function under50(num){
    return num < 50
}

val = numbers.find(under50) //will find the first number in the array under 50

// #############################
// #######Object Literals#######
// #############################

const person = {
    firstName: 'Steve',
    lastName: 'Smith',
    age: 30,
    email: 'steve@aol.com',
    hobbies: ['music', 'sports'],
    address: {
        city: 'Miami',
        state: 'FL'
    },
    getBirthYear: function(){
        return 2017-this.age;
    },

};

val=person

//select key and values
val=person.firstName;
val=person['firstName'];
val=person.age
val=person.hobbies[1];
val=person.getBirthYear();



const people =[
    {name: 'John', age: 30},
    {name: 'Mike', age: 23}
];

for (let i=0; i<people.length; i++){
    //console.log(people[i].name)
    //console.log(people[i].age)

}

// #############################
// #######Dates and Times#######
// #############################

const dateToday= new Date();
let birthday = new Date('6-1-1984 11:25:10') 
birthday = new Date('June 1 1984 11:25')
//check MDN for more on dates
val = today.getDate()
// month starts at 0
val = today.getMonth()
val = today.getDay()
val = today.getHours()
val = today.getMinutes()
val = today.getMilliseconds()
val = today.getTime()

birthday.setMonth(2)
birthday.setDate(10)
birthday.setFullYear(2018)
birthday.setHours(9)
birthday.setMinutes(4)

// #############################
// #######If and Comparison#####
// #############################

const id = 100;

//equal to
if (id == 101){
    console.log('correct')
}

//Not Equal To

if (id!=100){
    console.log('correct')
}

//Equal to Value and Type

// if (id === 100){
//     console.log('correct')
// }
// else {console.log('incorrect')}


// tests if undefined
// if (typeof id !== 'undefined'){
//     console.log(`The ID is ${id}`)
// }
// else {console.log('no ID')}

//Ternary Operator

(id === 100 ? 'CORRECT' : 'INCORRECT');

// Without Braces, curly braces are not necessary!
// if (id === 100)
//     console.log('correct')
// else 
//     console.log('incorrect')

// #############################
// #######Switches##############
// #############################

let color = 'orange'

// switch(color){
//     case 'red':
//         console.log('Color is red')
//         break;
//     case 'blue':
//         console.log('Color is blue')
//         break;
//     default:
//         console.log('color is not red or blue')
//         break;
// }

switch(new Date().getDay()){
    case 0:
        day = 'Sunday'
        break;
    case 1:
        day = 'Monday'
        break;
    case 2:
        day = 'Tuesday'
        break;
    case 3:
        day = 'Wednesday'
        break;
    case 4:
        day = 'Thursday'
        break;
    case 5:
        day = 'Friday'
        break;
    case 6:
        day = 'Saturday'
        break;
}
// Tells us the day
// console.log(`Today is ${day}`);

// #############################
// #######Function##############
// #############################

//Function Declarations

// in ES6 you can define defaults in case of undefined inside the argument
function greet(firstName='John', lastName='Doe'){
    return ('Hello '+firstName+' '+lastName);
}

// console.log(greet('Warren'))

//Function Expressions

const square = function(x){
    return x*x;
}
console.log(square(8))

//Immediately invocable function expressions - IIFEs

// they need to end wiht the open close parentheses
// (function(name){
//     console.log('Hello '+name);
// })('Warren');

//Property Methods

const todo = {
    add: function(){
        console.log('Add todo..');
    },
    edit: function(id){
        console.log(`Edit todo ${id}`);
    }
}
// can also define methods outside of the object
todo.delete = function(){
    console.log('Delete todo...');
}

todo.add();
todo.edit(22);
todo.delete();

console.log(todo)