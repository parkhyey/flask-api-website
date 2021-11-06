// send HTTP request to service.py

document.addEventListener('DOMContentLoaded', bindButtons);
function bindButtons() {
    // when button is clicked
    document.getElementById('get-reviews').addEventListener('click', function (event) {
        event.preventDefault();
        var req = new XMLHttpRequest();
        var place_id = 'ChIJW69I7FhZwokR61IbDPnsqTo';
        //var myURL = 'http://127.0.0.1:33033/' + place_id
        var myURL = 'http://flip3.engr.oregonstate.edu:33133/' + place_id;

        // send request
        req.open('GET', myURL, true);
        req.setRequestHeader('Content-Type', 'application/json');

        req.send(JSON.stringify(place_id));
        //var response = JSON.parse(req.responseText);
        var response = req.responseText;
        console.log(response);
        console.log('here');
        // display       
        document.getElementById("reviews-result").textContent = "test" + response;
        })
};
