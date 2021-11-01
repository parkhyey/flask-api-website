
document.addEventListener('DOMContentLoaded', bindButtons);
function bindButtons() {

    // when the star sign link is clicked from index.html
    document.getElementById('test').addEventListener('click', function (event) {
        event.preventDefault();
        var starsign = 'aquarius';
        // open 
        var req = new XMLHttpRequest();
        const options = {
            "method": "POST",
            "hostname": "sameer-kumar-aztro-v1.p.rapidapi.com",
            "port": null,
            "path": "/?sign=aquarius&day=today",
            "headers": {
                "x-rapidapi-host": "sameer-kumar-aztro-v1.p.rapidapi.com",
                "x-rapidapi-key": "c232a67fd7msh5d9690a65c5ee5ep19f6a0jsn958fd5326d04",
                "useQueryString": true
            }
        };

        req.open('POST', options, false);
        req.send('aquarius');
        const response = JSON.parse(req.responseText);

        if (!response) {
            showError('It is not a valid input. Try again.');
        }
        else {
            console.log(response);
            document.getElementById('result').textContent = 'Weather Info for ' + input;
        }
    })}