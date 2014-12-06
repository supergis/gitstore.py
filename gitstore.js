var ef = require('child_process').execFile;

module.exports =
    (function(){

        var python = '/usr/bin/python';

        var exec = function(cmd0, args, flags, callback){
            cmd = [__dirname + '/' + cmd0].concat(args);
            for(k in flags) {
                args.push('--' + k + '=' + flags[k]);
            }
            ef(python, cmd, callback);
        };

        return {
            init: function(dir, callback){
                exec('init.py', [dir], [], callback)
            },

            put: function(dir, file, data, flags, callback){
                exec('put.py', [dir, file, data], flags, callback)
            },

            get: function(dir, file, flags, callback){
                exec('get.py', [dir, file], flags, callback)
            },
        };
    })()
