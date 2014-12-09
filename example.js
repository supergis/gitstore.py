var gs = require('./gitstore.js')

gs.put('db', 'passwd', 'asdads',{}, function(err, stdout){
  console.log(stdout);
})
