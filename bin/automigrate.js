// Copyright IBM Corp. 2015,2016. All Rights Reserved.
// Node module: loopback-example-database
// This file is licensed under the MIT License.
// License text available at https://opensource.org/licenses/MIT

var path = require('path');

var app = require(path.resolve(__dirname, '../server/server'));
var ds = app.datasources.genomes;
ds.automigrate('Genomes', function(err) {
  if (err) throw err;


    var jsonfile = require('jsonfile')
    var file = 'files.json'
    jsonfile.readFile(file, function(err, obj) {
        console.log(JSON.stringify(obj))
        var accounts = obj;

        var count = accounts.length;
        accounts.forEach(function(account) {
            app.models.Genomes.create(account, function(err, model) {
            if (err) throw err;

            console.log('Created:', model);

            count--;
            if (count === 0)
                ds.disconnect();
            });
        });
    })

});
