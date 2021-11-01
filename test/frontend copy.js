
document.addEventListener('DOMContentLoaded', bindButtons);
function bindButtons() {

    // when the star sign link is clicked from index.html
    document.getElementById('test').addEventListener('click', function (event) {
        event.preventDefault();
        var starsign = 'Aries';
        // open 
        
        const http = require("https");

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
        
        const req = http.request(options, function (res) {
            const chunks = [];
        
            res.on("data", function (chunk) {
                chunks.push(chunk);
            });
        
            res.on("end", function () {
                const body = Buffer.concat(chunks);
                console.log(body.toString());
            });
            // display results
            document.getElementById('result').textContent = 'testets';
        });
        
        req.end();
    })}