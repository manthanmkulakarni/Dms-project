var express = require('express');
var app = express();

app.use(express.static('public'));


app.get('/process_get', function (req, res) {
   // Prepare output in JSON format
	
   response = {
      first_num:req.query.num1,
      last_num:req.query.num2,
      path:req.query.path
   };
   callpython(response);
   console.log(response);
   res.end(JSON.stringify(response));
})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})


function callpython(list)
{
var spawn = require('child_process').spawn,
    py    = spawn('python', ['encode.py']),
    data = [1,2,3,4,5,6,7,8,9],
    dataString = '';

py.stdout.on('data', function(data){
  dataString += data.toString();
});
py.stdout.on('end', function(){
  console.log('Python output=',dataString);
});

py.stdin.write(JSON.stringify(list));
py.stdin.end();

}
