// Book Constructor
function Book(title, author, isbn){
  this.title = title;
  this.author = author;
  this.isbn = isbn;
}


// UI Constructor

function UI() {}

UI.prototype.addBookToList = function(book){
  const list = document.getElementById('book-list');
  //Create tr element
  const row = document.createElement('tr');
  //insert Cols
  row.innerHTML = 
  `
  <td>${book.title}</td>
  <td>${book.author}</td>
  <td>${book.isbn}</td>
  <td><a href="#" class="delete">X</a></td>
  `;
  list.appendChild(row);
}

//Show Alert
UI.prototype.showAlert = function(message, className){
  //create div
  const div = document.createElement('div');
  //Add classes
  div.className=`alert ${className}`;
  //add text
  div.appendChild(document.createTextNode(message));
  const container = document.querySelector('.container');
  const form = document.querySelector('#book-form');
  //Insert Alert
  container.insertBefore(div, form);

  //Timeout after 3 seconds
  setTimeout(function(){
    document.querySelector('.alert').remove()}, 3000);
}

//delete Book
UI.prototype.deleteBook =function(target) {
  if (target.classList.contains('delete')){
    target.parentElement.parentElement.remove();
  }
}

//Clear Fields
UI.prototype.clearFields = function(){
  document.getElementById('title').value = "";
  document.getElementById('author').value = "";
  document.getElementById('isbn').value = "";
}

//Event Listeners
document.getElementById('book-form').addEventListener('submit', function(e){
  const title = document.getElementById('title').value,
    author = document.getElementById('author').value,
    isbn = document.getElementById('isbn').value;

  // Instantiating a book
  const book = new Book(title, author, isbn);

  // Instantiate UI
  const ui = new UI();

  //Validate
  if(title===""||author===""||isbn===""){
    ui.showAlert('Please fill in all fields', 'error')
  }
  else {
    // Add book to list
    ui.addBookToList(book);
    //Show Alert
    ui.showAlert('Book Added!', 'success');

    //Clear fields
    ui.clearFields();
  }

  e.preventDefault();
});

// Event Listener for Delete
document.getElementById('book-list').addEventListener('click', function(e){
  // Instantiated UI
  const ui = new UI();

  // Delete Book
  ui.deleteBook(e.target);

  //Show Message
  ui.showAlert('Book Removed', 'success')

  e.preventDefault();
})