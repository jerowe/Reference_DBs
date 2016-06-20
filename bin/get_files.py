#!/usr/bin/env python3


import subprocess
import sys
import json

class MyClass():

    def __init__(self):
        self.extension = ""
        self.host = "jdr400@butinah.abudhabi.nyu.edu"
        # self.command="cd /scratch/Reference_Genomes/Public; find -name \"%s\"" % self.extension
        self.command="cd /scratch/Reference_Genomes/Public; find -name \"*fa\" -o -name \"*fasta\" -o -name \"*fna\""
        self.ssh = subprocess.Popen(
                                    ["ssh", "%s" % self.host, self.command],
                                    shell=False,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE
                                    )
        self.result = []
        self.line = []
        self.records = []

    def set_extension(self, extension):
        self.extension = extension
        self.command="cd /scratch/Reference_Genomes/Public; find -name \"%s\"" % self.extension

    def run(self):
        self.result = self.ssh.stdout.readlines()

        if self.result == []:
            error = self.ssh.stderr.readlines()
            print(sys.stderr, "ERROR: %s" % error)

    def process(self):
        for res in self.result:
            res = res.strip()
            res = res.decode('utf-8')
            # res = str(res).decode('utf-8')
            self.line = res.split('/')
            self.build_json()

    def build_json(self):

        self.line[0] = ''
        self.line[1].replace(".", "")

        filePath = '/'.join(self.line)
        filePath = '/scratch/Reference_Genomes' + filePath

        if len(self.line) == 3:
            record = {'Category': self.line[1], 'Species': self.line[1], 'Release':
                      self.line[1], 'Name': self.line[2]}
        elif len(self.line) == 4:
            record = {'Category': self.line[1], 'Species': self.line[1], 'Release':
                      self.line[3], 'Name': self.line[3]}
        elif self.line[4] == 'transcriptome_data':
            record = {
                'Category': self.line[1],
                'Species': self.line[2],
                'Type': 'transcriptome',
                'Release': self.line[3],
                'Name': self.line[5]
            }
        else:
            record = {
                'Category': self.line[1],
                'Species': self.line[2],
                'Type': 'DNA',
                'Release': self.line[3],
                'Name': self.line[4]
            }
        record['FilePath'] = filePath
        self.records.append(record)

if __name__ == "__main__":

    c = MyClass()
    # c.set_extension("*fa")
    c.run()
    c.process()
    print(json.dumps(c.records))
