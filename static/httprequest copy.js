// send HTTP request to service.py

document.addEventListener('DOMContentLoaded', bindButtons);
function bindButtons() {
    // when button is clicked
    document.getElementById('get-reviews').addEventListener('click', function (event) {
        event.preventDefault();
        var req = new XMLHttpRequest();
        var place_id = 'ChIJW69I7FhZwokR61IbDPnsqTo'
        var myURL = 'flip3.engr.oregonstate.edu:33133/' + place_id

        // send request
        req.open('GET', myURL, true);
        req.setRequestHeader('Access-Control-Allow-Headers', '*');
        req.setRequestHeader('Content-Type', 'application/json');
        req.setRequestHeader('Access-Control-Allow-Origin', '*');

        req.send(place_id);
        //req.send(JSON.stringify(place_id))
        var response = JSON.stringify(req.responseText);
        console.log(response)
        console.log('here')
        // display       
        document.getElementById("reviews").innerHTML = response;
        })
};
