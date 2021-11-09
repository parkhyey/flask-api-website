function birthdayfunc() {
    var select = document.getElementById("birthday");
    var bir = select.value;
    if (bir == '') {    
        document.getElementById("birthday-result").innerHTML = '<span style="color:#FDC286">Select your birthday!</span>';
    } else {
        // document.getElementById("birthday-result").textContent = 'You are ' + bir;
        document.getElementById("birthday-result").innerHTML =
    'You are ' + '<a href="signs/'+ bir +'" id="bir" >' + bir + '</a>';
    }
};