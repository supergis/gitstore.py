var cp = require('child_process');


module.exports =
    (function(){

        var python = '/usr/bin/python';

        var pushFlags = function(args, flags) {
            for(k in flags) {
                args.push('--' + k + '=' + flags[k]);
            }
        }

        return {
            init: function(dir, cb){
                cp.execFile(python, ['init.py', dir], cb);
            },

            put: function(dir, file, data, flags, cb){
                var args = ['put.py', dir, file, data]
                pushFlags(args, flags);
                cp.execFile(python, args, cb);
            },

            get: function(dir, file, flags, cb){
                var args = ['get.py', dir, file]
                pushFlags(args, flags);
                cp.execFile(python, args, cb);
            },

        }
    })()
