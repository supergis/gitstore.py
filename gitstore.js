var ef = require('child_process').execFile;


module.exports =
    (function(){

        var python = '/usr/bin/python';

        var pushFlags = function(args, flags) {
            for(k in flags) {
                args.push('--' + k + '=' + flags[k]);
            }
        }
        var resolvePath = function(cmd) {
            return __dirname + '/' + cmd;
        }

        return {
            init: function(dir, cb){
                ef(python, [resolvePath('init.py'), dir], cb);
            },

            put: function(dir, file, data, flags, cb){
                var args = [resolvePath('put.py'), dir, file, data]
                pushFlags(args, flags);
                ef(python, args, cb);
            },

            get: function(dir, file, flags, cb){
                var args = [resolvePath('get.py'), dir, file]
                pushFlags(args, flags);
                ef(python, args, cb);
            },
        }
    })()
