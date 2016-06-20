# My Application

The project is generated by [LoopBack](http://loopback.io).

Run as bin/get_files.py > genomes.json

node bin/automigrate.js

http://0.0.0.0:3000/api/Genomes?filter[where][Species]=ERCC

Returns

`json
    [
        {
            "Category": "ERCC",
            "Species": "ERCC",
            "Release": "ERCC",
            "Name": "ERCC92.fa",
            "FilePath": "/scratch/Reference_Genomes/ERCC/ERCC92.fa",
            "id": "5767a86acf35c7b70451452b"
        }
    ]
`

