import config
import csv
import os
for proc in config.PROCESSING:
    print("Processing ", proc.name)
    in_ = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/processed/"+proc.name + ".csv") ,'w+')
    writer = csv.DictWriter(in_, fieldnames=proc.fields)
    writer.writeheader()
    for root, dirs, files in os.walk(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/raw/"+proc.name)):
        for f in files:
            print("processing file ",os.path.join(root,f) )
            proc.process(os.path.realpath(os.path.join(root,f)), writer)
