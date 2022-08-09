function validation() {
    // var name=document.myform.name;
    let nameEl = document.myform.Name;
    let nameE2 = document.myform.raisefundfor;
    let nameE3 = document.myform.relation;
    let Cause = document.myform.cause;
    var phoneNum=document.myform.phone_number;
    var image1=document.myform.upload_image;
    var image2=document.myform.upload_proof;
    var image3=document.myform.upload_doc;
    // let fundprice = document.myform.fund_price;
    let document_verification = document.myform.document_verification;
    let proof = document.myform.proof;
    let describtion = document.myform.describtion;
    let email = document.myform.email;
    let title = document.myform.title;
    let currency = document.myform.currency;
    let numbers = /^[0-9]+([,-][0-9]+)?$/;

    //[0-9]+ matches 1 or more digits [,-] matches a , or a -

    //(...)? is an optional match

    //^ anchors the start and $ anchors the end of the string

    let txt = document.getElementById('fund_id');
    
    

    if(nameEl.value.length <= 0){

        alert("Please Enter Your Name: ");
        nameEl.focus();
        return false;
      }  
    
    if(nameE3.value.length <= 0){

       alert("Please Enter Your Relation: ");
       nameE3.focus();
       return false;
    }

    if(nameE2.value.length <= 0){
        alert( 'Please Enter Raise Funds For: ');
        nameE2.focus();
      
        return false;
    } 

    if(email.value.length <= 0){
        alert( 'Please Your Email: ');
        email.focus();
      
        return false;
    } 

    if(!email.value.match(mailformat)){
        alert( 'Please Your Email: ');
        email.focus();
      
        return false;
    } 




    // if(fundprice.value.length <= 0){

    //    alert("Please Enter Your Fundprice: ");
    //    fundprice.focus();
    //    return false;
    // } 
    
    if (proof.value == 'select'){

        alert("Please Select Proof Type: ");
        proof.focus();

        return false;
    }

    if (currency.value == 'select'){

        alert("Please Select currency: ");
        currency.focus();

        return false;
    }
    
    if(describtion.value.length <= 0){

        alert("Please Type describtion");
        describtion.focus();
        return false;
     } 
    
    
    if (Cause.value == 'select'){

        alert("Please Select Cause");
        Cause.focus();

        return false;
    }

    if(document_verification.value == 'select Verification'){

        alert("Please Select DocumentVerification: ");
        document_verification.focus();
        return false;
     } 



   


    if (phoneNum.value.length != 10) {

        alert("please Enter valid mobile number");
        
        return false;
        
    }

    if (phoneNum.value.length <= 0) {

        alert("Please Enter Mobile Number");

        return false;
    }
 
    if (image1.value.length == " ") {

        alert("You Forget To Uploadimage");
        image1.focus();

        return false;
    }

    if (image2.value.length == " ") {

        alert("You Forget To UploadProof");
        image2.focus();

        return false;
    }
    if (image3.value.length == " ") {

        alert("You Forget To UploadDocument");
        image3.focus();

        return false;
    }

    if(title.value.length <= 0){

        alert("Please Enter Your Title: ");
        title.focus();
        return false;
     }

    

     if (txt.value.match(numbers)) {
         alert('Your input is valid');
         return true;
     }
     else {
         alert('Please input numeric characters only');
         return false;
     }

    return true;   
    
 }