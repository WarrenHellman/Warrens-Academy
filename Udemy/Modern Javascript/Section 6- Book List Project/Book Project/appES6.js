// Using ES6 JS

class Book {
  constructor(title, author, isbn) {
    this.title = title;
    this.author = author;
    this.isbn = isbn;
  }
}

class UI {

  addBookToList(book) {
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
  
  showAlert(message, className) {
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

  deleteBook(target) {
    if (target.classList.contains('delete')){
      target.parentElement.parentElement.remove();
    }
  }

  clearFields() {
    document.getElementById('title').value = "";
    document.getElementById('author').value = "";
    document.getElementById('isbn').value = "";
  }
}

//Local Storage Class
class Store {
  static getBooks(){
    let books;
    if (localStorage.getItem('books')===null){
      books = [];
    }
    else {
      books = JSON.parse(localStorage.getItem('books'));
    }
    return books;
  }
  
  static displayBooks(){
    const books = Store.getBooks();

    books.forEach(function(book){
      const ui = new UI;

      //Add book to UI
      ui.addBookToList(book);
    })
  }
  
  static addBooks(book) {
    const books = Store.getBooks();
    books.push(book);

    localStorage.setItem('books', JSON.stringify(books));
  }

  static removeBook(isbn) {
    const books = Store.getBooks();

    books.forEach(function(book, index){
      if (book.isbn === isbn) {
        books.splice(index, 1)
      }
    });
    localStorage.setItem('books', JSON.stringify(books));
  }
}

//DOM Load Event
document.addEventListener('DOMContentLoaded', Store.displayBooks);

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

    //Add to LS
    Store.addBooks(book)

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

  // Remove from LS
  Store.removeBook(e.target.parentElement.previousElementSibling.textContent);

  //Show Message
  ui.showAlert('Book Removed', 'success')

  e.preventDefault();
})