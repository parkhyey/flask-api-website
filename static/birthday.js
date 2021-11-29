// JS function to support dropdown search feature to find star signs
function birthdayfunc() {
    var select = document.getElementById("birthday");
    var birthday = select.value;
    if (birthday == '') {    
        document.getElementById("birthday-result").innerHTML = '<span style="color:#FDC286">Select your birthday!</span>';
    } else {
        document.getElementById("birthday-result").innerHTML =
    'You are ' + '<a href="signs/'+ birthday +'" id="bir" >' + birthday + '</a>';
    }
};