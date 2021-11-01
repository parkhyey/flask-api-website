
document.addEventListener('DOMContentLoaded', bindButtons);
function bindButtons() {

    // when the star sign link is clicked from index.html
    document.getElementById('Aries').addEventListener('click', function (event) {
        event.preventDefault();
        
        // open 
       
        window.open('signs/01Aries.html')
        const starsign = 'Aries'; 
        localStorage.setItem(starsign); 
        console.log(starsign)             
        // document.getElementById('your-sign').innerHTML = starsign;
        document.getElementById("your-sign").innerHTML = localStorage.getItem(starsign);
    })}