// Create event listener for button

document.getElementById('button').addEventListener('click', loadData);

function loadData() {
  // Create XHR object
  const xhr = new XMLHttpRequest();

  //Open
  xhr.open('GET', 'data.txt', true);

  // Options for spinners and loaders
  // xhr.onprogress = function(){
  //   // display your image
  // }

  xhr.onload = function() {
    if(this.status === 200) {
      console.log(this.responseText);
      let response = this.responseText;
      displayResponse(response);
    }
  }
  // The old way, see readyState chart. Doesn't seem applicable:
  // xhr.onreadystatechange = function() {
  //   if(this.status ===200 && this.readyState ===4){
  //     console.log(this.responseText);
  //   }
  // }

  // xhr.onerror = function(){
  //   console.log('request error or wahtever')
  // }

  xhr.send();

  // readyState Values
  // 0: request not initialized
  // 1: server connnection established
  // 2: request received
  // 3: processing request
  // 4: request finished and response is ready

  //HTTP Status
  // 200: "OK"
  // 403: "Forbidden"
  // 404: "Not Found"
}

function displayResponse(response) {
  const data = response;
  const displayNode = document.getElementById('output-response');
  displayNode.innerText = response;
}