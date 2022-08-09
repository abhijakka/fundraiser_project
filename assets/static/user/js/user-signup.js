function validation2() {


var pw = document.myform2.password
let nameEl = document.myform2.name;
let passwordE2 = document.myform2.password;
let gmail = document.myform2.gmail;
let Gmail = document.myform2.getElementById("email").value 


if(nameEl.value.length <= 0){

    alert("Please Enter Your Name: ");
    nameEl.focus();
    return false;
  }  

  
  
  if(gmail.value.length <= 0){
    alert( 'Please Your Email: ');
    gmail.focus();
  
    return false;
} 

if(!gmail.value.match(mailformat)){
    alert( 'Please Your Email: ');
    gmail.focus();
  
    return false;
} 

if(passwordE2.value.length <= 0){
    alert('Please Enter Your password: ');
    passwordE2.focus();
    return false;
  }
   
     
    //check empty password field  
    if(pw == "") {  
       document.getElementById("message").innerHTML = "**Fill the password please!";  
       return false;  
    }  
     
   //minimum password length validation  
    if(pw.length < 8) {  
       document.getElementById("message").innerHTML = "**Password length must be atleast 8 characters";  
       return false;  
    }  
    
  //maximum length of password validation  
    if(pw.length > 15) {  
       document.getElementById("message").innerHTML = "**Password length must not exceed 15 characters";  
       return false;  
    } else {  
       alert("Password is correct");  
    }  
    
  
   
 return true;
}  
