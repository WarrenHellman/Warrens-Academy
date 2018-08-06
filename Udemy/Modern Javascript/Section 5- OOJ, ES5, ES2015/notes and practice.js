// ##################################
// ####Basic Constructor Function####
// ##################################
function Person(name, dob){
  this.name = name;
  // this.age = age
  this.birthday = new Date(dob);
  this.calculateAge = function(){
    const diff = Date.now() - this.birthday.getTime();
    const ageDate = new Date(diff);
    return Math.abs(ageDate.getUTCFullYear() - 1970);
  }
}
//
const warren = new Person('Warren', '9-1-1984');
// const john = new Person('John')
// console.log(warren.calculateAge())


// ###################################
// #######Other Constructors##########
// ###################################

// String

const name1 = 'Jeff'
const name2 = new String('Jeff');

name2.foo = 'bar';
// console.log(name1)

// console.log(typeof name2)

//Name 2 is an object so it won't evaluate as a primitive string
// if (name2 == 'Jeff'){
//   console.log('YES');
// }
// else {console.log('NO')}

//Number
const num1 =5;
const num2 = new Number(5);

//Boolean
const bool1 = true;
const bool2 = new Boolean(true)

//Functions

const getSum1 = function(x, y){
  return x + y;
}
getSum1(1,3);

const getSum2 = new Function('x','y', 'return 1 + 1')

const john1 = {name: 'John'}
const john2 = new Object({name: 'John'})

const arr1 = [1,2,3,4];
const arr2 = new Array([1,2,3,4])

//Regular Expressions

const re1 = /\w+/;
const re2 = new RegExp('\\w+');
