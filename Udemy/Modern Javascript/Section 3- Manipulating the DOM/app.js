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