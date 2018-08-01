// ################################
// #######Accessing the DOM########
// ################################

//let val;

// val = document;
// val = document.all;
// // returns an html collection, arraylike and comma separated
// val = document.all[3];
// val = document.head;
// val = document.body;
// val = document.doctype;
// val = document.domain;
// val = document.URL;
// val = document.characterSet;
// val = document.contentType;

// val = document.forms;
// val = document.forms[0];
// val = document.forms[0].id;
// val = document.forms[0].method;
// val = document.forms[0].action;

// val = document.links;
// val = document.links[0];
// val = document.links[0].className;
// val = document.links[0].classList;

// val = document.images;

// val = document.scripts;
// val = document.scripts[0];
// val = document.scripts[2].getAttribute('src');

// let scripts = document.scripts;

// //need to arrayify the HTML collection
// let scriptsArr = Array.from(scripts);

// scriptsArr.forEach(function(script) {
//   console.log(script.getAttribute('src'));
// });

// console.log(val);

// ################################
// #######DOM Selectors############
// ################################

//Select item

// console.log(document.getElementById('task-title'))

//Get Things from the Element

// console.log(document.getElementById('task-title').id);
// console.log(document.getElementById('task-title').className);

//Change Styling

// document.getElementById('task-title').style.background = '#333';
// document.getElementById('task-title').style.color = '#fff';
// document.getElementById('task-title').style.padding = '5px';
// document.getElementById('task-title').style.display = 'none';

//Change Content

//easier to set a variable.
const taskTitle = document.getElementById('task-title');
//both change the displayed content in between the tags
taskTitle.textContent = 'Task List';
taskTitle.innerText = 'My Tasks';
taskTitle.innerHTML = '<span style="color:red">Task List</span>';

//document.querySelector()- a single selector

//works with any css selector

// console.log(document.querySelector('#task-title'));
// console.log(document.querySelector('.card-title'));
// console.log(document.querySelector('h5'));

// document.querySelector('li').style.color = 'red';
// document.querySelector('ul li').style.color = 'red';
// document.querySelector('li:last-child').style.color = 'red';
// document.querySelector('li:nth-child(3)').style.color = 'yellow';
// document.querySelector('li:nth-child(odd)').style.background = '#ccc';


// Selecting Multiple Elements

// const items = document.getElementsByClassName('collection-item');
// console.log(items);
// console.log(items[0]);
// items[0].style.color = 'red';
// items[3].textContent = 'Hello';

// const listItems = document.querySelector('ul').getElementsByClassName('collection-item');

// console.log(listItems)

//document.getElementsByTagName - selects by tag instead of class or id
let lis = document.getElementsByTagName('li');
// console.log(lis);
// console.log(lis[0]);

// To do array methods, turn into array
lis = Array.from(lis);

// lis.reverse();

// lis.forEach(function(li, index){
//   console.log(li.className)
//   li.textContent = `${index}: Hello`;
// })

//document.querySelectorAll()- returns node list which can do more array methods without conversion

const items = document.querySelectorAll('ul.collection li.collection-item');

// items.forEach(function(item, index){
//   console.log(item.className)
//   item.textContent = `${index}: Hello`;
// })

const liOdd = document.querySelectorAll('li:nth-child(odd)');
const liEven = document.querySelectorAll('li:nth-child(even)');

// Can iterate through the items with querySelectorAll
liOdd.forEach(function(li){
  li.style.background = '#ccc'
})

// Or with a for loop

for(let i=0;i<liEven.length;i++){
  liEven[i].style.background = '#f4f4f4'
};

console.log(items)

// ################################
// #######Traversing the DOM#######
// ################################

let val;

const list = document.querySelector('ul.collection');
const listItem = document.querySelector('li.collection-item:first-child');

val = listItem;
val = list;

//Get Child Nodes
val = list.childNodes;//gives the items as well as some text nodes (in this case it is just the space in between nodes)
val = list.childNodes[0];
val = list.childNodes[0].nodeName;
val = list.childNodes[1].nodeType;

//--Node Types--
//1 - Element
//2 - Attribute (deprecated)
//3 - Text Node
//8 - Comment
//9 - Document itself
//10 - Doctype


// Get teh children element nodes
// val = list.children; // gives an htmlcollection of just the children elements

val = list.children[0];
val = list.children[1].textContent = 'Hell';
val = list.children[3].children[0].id = 'test-link';

// First Child
val = list.firstChild; //gives first child regardless
val = list.firstElementChild; //gives first element

// Last Child
val = list.lastChild;
val = list.lastElementChild;

// Get Parent Node
val = listItem.parentNode; //Ul
val = listItem.parentElement.parentElement; //can get grandparents!

//Get Sibling

val = listItem.nextSibling; //in this case, text node
val = listItem.nextElementSibling;

val = listItem.previousSibling;
val = listItem.previousElementSibling;

console.log(val);




// ################################
// #######Creating Elements########
// ################################


//Create Element

const li = document.createElement('li');

//Add Class
li.className = 'collection-item';

//Add id
li.id = 'new-item';

//Add attribute
li.setAttribute('title', 'New Item');

// Create text node and append

li.appendChild(document.createTextNode('Hello World'));

//create new link element
const link = document.createElement('a');
//add classes
link.className= 'delete-item secondary-content';

//Add icon html
link.innerHTML = '<i class="fa fa-remove"></i>';

//Append link into
li.appendChild(link);

// Append li as childe to ul
document.querySelector('ul.collection').appendChild(li);


console.log(li);

// #################################
// #Removing and Replacing Elements#
// #################################

//REPLACE ELEMENT

//Create Element

const newHeading = document.createElement('h2');
//Add id
newHeading.id = 'task-title';
//New Text Node
newHeading.appendChild(document.createTextNode('Task List'));

//Get old heading

const oldHeading = document.getElementById('task-title');
//Parent
const cardAction = document.querySelector('.card-action');

//Replace
cardAction.replaceChild(newHeading, oldHeading);

//REMOVE ELEMENT
const lis = document.querySelectorAll('li');
const list = document.querySelector('ul');

//Remove list item
lis[0].remove();

//Remove child element
list.removeChild(lis[3]);

//Classes and Attributes
const firstLi = document.querySelector('li:first-child');
const link = firstLi.children[0];

let val;

val = link.className
val = link.classList;
val = link.classList[0];
link.classList.add('test');
link.classList.remove('test');

//Attributes
val = link.getAttribute('href');
val = link.setAttribute('href', 'http://google.com');
link.setAttribute('title', 'Google')
val = link.hasAttribute('title'); // returns Boolean

console.log(val);

// ################################
// #######Event Listeners##########
// ################################

// document.querySelector('.clear-tasks').addEventListener('click', function(e){
//     console.log('hello world');

//     e.preventDefault(); // prevents default event behavior
// });

document.querySelector('.clear-tasks').addEventListener('click', onClick);

function onClick(e){
    // console.log('Clicked');
    let val;
    val = e; // gives all of the event on the clicked object

    //Event target
    val = e.target;
    val = e.target.id;
    val = e.target.className;
    val = e.target.classList;
    e.target.innerText='Hello'
    //Event Type
    val = e.type
    //Timestamp
    val = e.timeStamp;
    //Coordinates event relative to window
    val = e.clientY;

    //Coordinates relative the the element
    val = e.offsetY;
    val = e.offsetX;

    
    console.log(val);
}

// ################################
// #######Mouse Events#############
// ################################

const clearBTn = document.querySelector('.clear-tasks');
const card = document.querySelector('.card');
const heading = document.querySelector('h5');

//Click
// clearBTn.addEventListener('click', runEvent)
//Double click
// clearBTn.addEventListener('dblclick', runEvent);
//Mouse down/Up- on click down, or release
// clearBTn.addEventListener('mousedown', runEvent);
// clearBTn.addEventListener('mouseup', runEvent);
//Mouseenter
// clearBTn.addEventListener('mouseenter', runEvent);
// clearBTn.addEventListener('mouseleave', runEvent);
//Mouseover
// clearBTn.addEventListener('mouseover', runEvent);
//Mouseleave
// clearBTn.addEventListener('mouseout', runEvent);

//Mousemove
card.addEventListener('mousemove', runEvent);




//Event Handler
function runEvent(e){
    console.log(`EVENT TYPE: ${e.type}`)
    // heading.textContent= `MouseX: ${e.offsetX} MouseY: ${e.offsetY}`;
    document.body.style.backgroundColor = `rgb(${e.offsetX},${e.offsetY},40)`
}

// ################################
// #######Input and Form Events####
// ################################

const form = document.querySelector('form');
const taskInput = document.getElementById('task');
const heading = document.querySelector('h5')

//Submit
// form.addEventListener('submit', runEvent);

//Keydown
// taskInput.addEventListener('keydown', runEvent)

//Keyup
// taskInput.addEventListener('keydown', runEvent)

//Keypress
// taskInput.addEventListener('keypress', runEvent)

//Focus- when you click in
// taskInput.addEventListener('focus', runEvent)

//blur- when you click out
// taskInput.addEventListener('blur', runEvent)

//cut
// taskInput.addEventListener('cut', runEvent)

//paste
// taskInput.addEventListener('paste', runEvent)

//copy
// taskInput.addEventListener('copy', runEvent)

//Input- any activity on element
// taskInput.addEventListener('input', runEvent)



//Clear input
taskInput.value = '';

function runEvent(e){
    console.log(`EVENT TYPE: ${e.type}`);
    
    // heading.innerText = e.target.value;

    //Get input value
    // console.log(taskInput.value); //doesn't work
    // e.preventDefault();
}

// ################################
// #Event Bubbling & Delegation####
// ################################

//Bubbling, events work their way up through the parent elements. Follows the idea that by clicking on a child, you are also clicking on all parent elements

//Delegation, target a parent element to apply event to child

document.querySelector('.card-title').addEventListener('click', function(){
  console.log('card title')
})


//Event Delegation

// const delItem = document.querySelector('.delete-item')

// delItem.addEventListener('click', deleteItem);

document.body.addEventListener('click', deleteItem)

function deleteItem(e){

  if (e.target.parentElement.classList.contains('delete-item')){
      console.log('delete item')
      e.target.parentElement.parentElement.remove();
  }
}

// ################################
// #Session and local storage######
// ################################

//Set local storage item
// localStorage.setItem('name', 'Warren')

//Set session storage item
// sessionStorage.setItem('name', 'Erin')

//remove from storage
// localStorage.removeItem('name')

//get from storage
// const name = localStorage.getItem('name');
// const age = localStorage.getItem('age')

//clear local storage
// localStorage.clear();
// console.log(name);

document.querySelector('form').addEventListener('submit', function(e){
  const task = document.getElementById('task').value;

  let tasks;
  if (localStorage.getItem('tasks')===null){
      tasks =[];
  }
  else {
      tasks=JSON.parse(localStorage.getItem('tasks'));
  }

  tasks.push(task);
  localStorage.setItem('tasks', JSON.stringify(tasks));

  e.preventDefault();
});

const tasks = JSON.parse(localStorage.getItem('tasks'));

tasks.forEach(function(task){
  console.log(tasks)
})