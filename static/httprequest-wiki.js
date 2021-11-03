// send HTTP request to service.py

document.addEventListener('DOMContentLoaded', bindButtons);
function bindButtons() {

    document.getElementById('wiki').addEventListener('click', function (event) {
        event.preventDefault();
        var req = new XMLHttpRequest();
        var wiki = 'Zakynthos'
        var myURL = 'http://flip1.engr.oregonstate.edu:4752/' + wiki

        req.open('GET', myURL, true);
        req.setRequestHeader('Access-Control-Allow-Headers', '*');
        req.setRequestHeader('Content-Type', 'application/json');
        req.setRequestHeader('Access-Control-Allow-Origin', '*');
        req.send(wiki);

        var response = req.responseText;

        console.log(response)
        console.log('test')
    
        document.getElementById("wiki").innerHTML = response;
        })
};
