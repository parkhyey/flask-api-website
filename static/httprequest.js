// send AJAX request to backend
// once data received from backend, update table accordingly

document.addEventListener('DOMContentLoaded', bindButtons);
function bindButtons() {
    // when Add New button is clicked after adding new data
    document.getElementById('get-reviews').addEventListener('click', function (event) {
        event.preventDefault();
        var req = new XMLHttpRequest();
        var place_id = 'ChIJW69I7FhZwokR61IbDPnsqTo'
        var myURL = 'http://127.0.0.1:5000/?id' + place_id

        // send request using an asynchronous call via POST
        req.open('GET', myURL, false);
        req.setRequestHeader('Content-Type', 'application/json');
        req.send(null);

        var response = JSON.parse(req.responseText);
        // call displayRows function to display       
        document.getElementById("reviews").innerHTML = '<b>' + response + '</b>';
        })
};

