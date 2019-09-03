var express = require('express');
var mysql = require('mysql');
var bodyParser = require('body-parser');
var logger = require('morgan');
var app = express();
var port = 8080;
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(logger('dev'));

var db = mysql.createConnection({
    host: 'localhost',
    user: 'add',
    password: '1234567',
    database: 'pauradb'
});

/*
CREATE TABLE `hosts` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`ip` VARCHAR(15) NULL DEFAULT NULL,
	`hostname` VARCHAR(20) NULL DEFAULT NULL,
	PRIMARY KEY (`id`)
)
COLLATE='latin1_swedish_ci'
;


*/


app.post('/add_hosts', function (request, response, next) {
  var sql_query = 'INSERT INTO hosts (ip,hostname) VALUES (\''+request.body.ip+'\',\''+request.body.hostname+'\')';
  db.query(sql_query,
  request.body, function (err, rows, fields) {
    if (!err) {
      response.status(200).send(rows);
    } else {
      response.status(200).send('Errore di connesione o query!'+sql_query);
    }
  });
});


app.get('/', function (request, response, next) {
    db.query('SELECT * FROM hosts', function (err, rows, fields) {
        if (!err) {
            response.status(200).send(rows);
        } else {
            response.status(200).send('Errore di connesione o query!');
        }
    });
});

app.get('/id/:id', function (request, response, next) {
    db.query('SELECT * FROM hosts WHERE id = ?',
[request.params.id], function (err, rows, fields) {
        if (!err) {
            response.status(200).send(rows);
        } else {
            response.status(200).send('Errore di connesione o query!');
        }
    });
});
app.post('/form', (req, res, next) => {
  const prova = req.body.prova
  res.status(200).send(prova);
  db.query('INSERT INTO my_table (prova) VALUES (?)',req.body.prova, function (err, rows, fields) {
    if (!err) {
        res.status(200).send(rows);
    } else {
        res.status(200).send('Errore di connesione o query!');
    }

  });


});




app.listen(port, function () {
    console.log('Express server inizializzato sulla porta ' + port);
});
