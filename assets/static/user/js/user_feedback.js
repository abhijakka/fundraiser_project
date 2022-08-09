function validation(){
    let feedback_name = document.myform.feedback_name;
    let feedback_cause = document.myform.feedback_cause;
    let feedback_email = document.myform.feedback_email;
    let feedbacks = document.myform.feedbacks;

    if(feedback_name.value.length <= 0){

        alert("Please Enter Your Name: ");
        feedback_name.focus();
        return false;
      } 

      if(feedbacks.value.length <= 0){

        alert("Please Write Your Message: ");
        feedbacks.focus();
        return false;
      } 


      if(feedback_cause.value.length <= 0){

        alert("Please Write Your Cause: ");
        feedback_cause.focus();
        return false;
      } 

      if(feedback_email.value.length <= 0){
        alert( 'Please Your Email: ');
        feedback_email.focus();
      
        return false;
    } 

    if(!feedback_email.value.match(mailformat)){
        alert( 'Please Your Email: ');
        feedback_email.focus();
      
        return false;
    } 


}