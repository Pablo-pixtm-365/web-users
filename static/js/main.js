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


(function() {
  $('form div button').keyup(function() {

      var empty = false;
      $('form div input').each(function() {
          if ($(this).val() == '') {
              empty = true;
          }
      });

      if (empty) {
          $('#bt-register').attr('disabled', 'disabled'); // updated according to http://stackoverflow.com/questions/7637790/how-to-remove-disabled-attribute-with-jquery-ie
      } else {
          $('#bt-register').removeAttr('disabled'); // updated according to http://stackoverflow.com/questions/7637790/how-to-remove-disabled-attribute-with-jquery-ie
      }
  });
})()