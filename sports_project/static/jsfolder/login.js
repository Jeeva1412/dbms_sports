
function validate(){
  var userid=document.querySelector('#userid').value;
  var password=document.querySelector('#password').value;


  if(userid==""){
    alert("Enter userid ");
    return false;
  }
  else if(password==""){
    alert("Enter password");
    return false;
  }
  else if((userid.length <8)) {
    alert("userid must be atleast 8 characters");
    return false;
  }
    else if((password.length <8)) {
    alert("password must be atleast 8 characters");
    return false;
  }
  else if(userid !== password)
  {
    alert("enter valid userid and password");
    return false;
  }
  else{
    return true;
  }


}

