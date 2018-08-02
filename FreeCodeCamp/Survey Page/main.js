function formValidator(){
    let number = document.getElementById('number').value;
    if (number<0 ||number>7){
        alert("Please select a number between 0-7");
        return false;    
    }
    
    let reg = new RegExp('^[0-9]$');
    if (reg.test(number)===false){
        alert("Please enter a number between 0-7")
        return false;
    }

    let emailID = document.getElementById('email').value;
    let atpos = emailID.indexOf("@");
    let dotpos = emailID.lastIndexOf(".");
    
    if (atpos < 1 || ( dotpos - atpos < 2 )){
        alert("Please enter correct email ID")
        return false;
    }
    

}