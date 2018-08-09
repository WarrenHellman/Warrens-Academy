const http = new easyHTTP;

//Get All Posts
// http.get('https://jsonplaceholder.typicode.com/posts', function(err, posts){
//   if (err){
//     console.log(err);
//   } else {
//     console.log(posts);
//   }
  
// });

// Get single post

// http.get('https://jsonplaceholder.typicode.com/posts/1', function(err, posts){
//   if (err){
//     console.log(err);
//   } else {
//     console.log(posts);
//   }
  
// });

// Create Data

const data = {
  title: 'Custome Post',
  body: 'this is a custom post',
  userID: 49494
}

//Create Post

// http.post('https://jsonplaceholder.typicode.com/posts', data, function(err, post){
//   if (err){
//         console.log(err);
//       } else {
//         console.log(post);
//       }
// });

// Update Post

http.put('https://jsonplaceholder.typicode.com/posts/1', data, function(err, post){
  if (err){
    console.log(err);
  } else {
    console.log(post);
  }
})


//Delete REquest

http.delete('https://jsonplaceholder.typicode.com/posts/1', function(err, response){
  if (err){
    console.log(err);
  } else {
    console.log(response);
  }
  
});