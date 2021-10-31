
document.addEventListener('DOMContentLoaded', bindButtons);
function bindButtons() {

    // when the star sign link is clicked
    // document.getElementById('Aries').addEventListener('click', function (event) {
    //     event.preventDefault();
    
    //     const starsign = 'Aries'; 
    //     console.log(starsign)             
    //     document.getElementById("your-sign").textContent = 'You are ' + starsign;
    
    // document.getElementById('submit').addEventListener('click', function (event) {
    //     event.preventDefault();
    
    //     const starsign = 'Aries'; 
    //     console.log(starsign)             
    //     document.getElementById("your-sign").textContent = 'You are ' + starsign;
        
    // })
    // })
    }

function birthdayfunc() {
    var select = document.getElementById("birthday");
    var bir = select.value;
    if (bir == '') {    
        document.getElementById("birthday-result").innerHTML = '<span style="color:#FDC286">Select your birthday!</span>';
    } else {
        // document.getElementById("birthday-result").textContent = 'You are ' + bir;
        document.getElementById("birthday-result").innerHTML =
    'You are ' + '<a href="signs/'+ bir +'.html"><span id="bir">' + bir + '</span></a>';
    }
};