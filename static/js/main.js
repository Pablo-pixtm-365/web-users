function change_page(){
    window.location.href = "test.html";
  } 


function myFunction() {
  var x = document.getElementById("id_password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function toggle_visibility(id) {
  var e = document.getElementById("closealert");
  if(e.style.display == 'block')
     e.style.display = 'none';
  else
     e.style.display = 'block';
}