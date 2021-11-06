// send HTTP request to service.py
var express = require("express");
var axios = require("axios");
var request = require("request");
var app = express();
app.use(express.static(__dirname));
let JSON = require("JSON");

document.addEventListener("DOMContentLoaded", bindButtons);
function bindButtons() {
  document.getElementById("wiki").addEventListener("click", function (event) {
    event.preventDefault();
    const url = "http://flip1.engr.oregonstate.edu:4752/Zakynthos";

    function test_request(url) {
      request(url, function (error, response, body) {
        console.error("error: ", error);
        console.log("status code: ", response && response.statusCode);
        console.log("body: ", body);
      });
    }

    let data = getBody(url, function (err, body) {
      if (err) {
        console.log(err);
      } else {
        console.log(body)
        obj = JSON.parse(body);
        console.log(obj);
        return body;
      }
    });

    console.log(data);

    function getBody(url, callback) {
      request(
        {
          url: url,
          json: true,
        },
        function (error, response, body) {
          if (error || response.statusCode !== 200) {
            return callback(error || { statusCode: response.statusCode });
          }
          callback(null, JSON.stringify(body));
        }
      );
    }
  });
}
