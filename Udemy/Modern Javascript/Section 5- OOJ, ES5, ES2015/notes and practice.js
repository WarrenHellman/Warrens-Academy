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


// ##################################
// #########Prototypes###############
// ##################################

// Object.prototype

function Person(firstName, lastName, dob){
  this.firstName = firstName;
  this.lastName = lastName;

  this.birthday = new Date(dob);
  // this.calculateAge = function(){
  //   const diff = Date.now() - this.birthday.getTime();
  //   const ageDate = new Date(diff);
  //   return Math.abs(ageDate.getUTCFullYear() - 1970);
  // }
}

// It is better to add methods to the prototype, instead of the constructor
//Calculate age
Person.prototype.calculateAge = function(){
  const diff = Date.now() - this.birthday.getTime();
  const ageDate = new Date(diff);
  return Math.abs(ageDate.getUTCFullYear() - 1970);
}

//Get full name
Person.prototype.getFullName = function(){
  return `${this.firstName} ${this.lastName}`;
}

//Gets married
Person.prototype.getsMarried = function(newLastName){
  this.lastName = newLastName;
}

const warren = new Person('Warren', 'Hellman', '8/12/90')
const mary = new Person('Mary', 'Contrary', 'March 20 1978')

console.log(mary)
warren.getsMarried('Korte')
console.log(warren.getFullName());

console.log(warren.hasOwnProperty('middleName'))

// ##################################
// #####Prototypical Inheritance#####
// ##################################

function Person(firstName, lastName){
  this.firstName= firstName;
  this.lastName= lastName;
}

//Greeting
Person.prototype.greeting = function(){
  return `Hello there ${this.firstName} ${this.lastName}`;
}

const person1 = new Person('John', 'Doe');
// console.log(person1.greeting())

function Customer(firstName, lastName, phone, membership) {
  
  //calls another constructor for info
  Person.call(this, firstName, lastName);
  this.phone = phone;
  this.membership = membership;
}

//Inherit the Person prototype methods
Customer.prototype = Object.create(Person.prototype);

//Make customer.prototype return Customer()
Customer.prototype.constructor= Customer;

// Create Customer
const customer1 = new Customer('Tom', 'Smith', '555-555-5555', 'Standard')

console.log(customer1);

//Overwrite inherited greeting
Customer.prototype.greeting = function(){
  return `Hello there ${this.firstName} ${this.lastName}, welcome to the company`;
}

console.log(customer1.greeting());

// ##################################
// #####Using Object.create##########
// ##################################

// easier way without having to create a whole new constructor

const personPrototypes = {
  greeting: function(){
    return `Hello there ${this.firstName} ${this.lastName}`
  },
  getsMarried: function(newLastName){
    this.lastName = newLastName;
  }
}

const mary = Object.create(personPrototypes);
mary.firstName = 'Mary';
mary.lastName= 'Williams';
mary.age = 30;

mary.getsMarried('Hellman')

console.log(mary.greeting())

const warren = Object.create(personPrototypes, {
  firstName: {value: 'Warren'},
  lastName: {value: 'Woodler'},
  age: {value: 36}
});

console.log(warren)
console.log(warren.greeting())

// ##################################
// #####ES6 Object Syntax############
// ##################################

class Person {
  constructor(firstName, lastName, dob) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.birthday = new Date(dob);
  }
  greeting() {
    return `Hello there ${this.firstName} ${this.lastName}`
  }
  calculateAge(){
    const diff = Date.now() - this.birthday.getTime();
    const ageDate = new Date(diff);
    return Math.abs(ageDate.getUTCFullYear()-1970);
  }
  getsMarried(newLastName){
    this.lastName = newLastName;
  }

  //Static Method
  static addNumbers(num1, num2){
    return num1 + num2
  }
}

const mary = new Person('Mary', 'Thalasinos', '8/2/1986')

console.log(mary)

//Call Static methods
console.log(Person.addNumbers(1,2));

// ##################################
// #####Sub Classes##################
// ##################################

class Person {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  greeting() {
    return `Hello there ${this.firstName} ${this.lastName}`;
  }
}

// Extends the methods from the parent class
class Customer extends Person {
  constructor(firstName, lastName, phone, membership){
    super(firstName, lastName);

    this.phone = phone;
    this.membership = membership;
  }
  static getMembershipCost(){
    return 500;
  }
}

const warren = new Customer('Warren', 'Felix', '555-555-5555', 'Standard')

console.log(warren)

console.log(warren.greeting())
console.log(Customer.getMembershipCost())