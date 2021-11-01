// handle the frontend's AJAX request and send back the appropriate data
var express = require('express');
var mysql = require('./myCred.js');  // export pool
var cors = require('cors')

var app = express();
var handlebars = require('express-handlebars').create({ defaultLayout: 'main' });

// setup bodyParser for pulling a request from body
var bodyParser = require('body-parser');
const e = require("express");
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 33133);
app.use(cors())

// serve static files
app.use(express.static('static'));

// GET request to show all rows of the table
app.get('/', function (req, res, next) {
  console.log('testingserver')
});

app.listen(app.get('port'), function () {
  console.log('listening on port:' + app.get('port') + '/; press Ctrl-C to terminate.');
});
