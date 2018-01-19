import config
import csv
import os
import pandas as pd
import numpy as np

def runPostProcess(f, ot, in_):
    pass


def runProcess(f, ot, in_):
    for root, dirs, files in os.walk(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/raw/"+in_)):
        for fi in files:
            print("processing file ",os.path.join(root,fi) )
            f(os.path.realpath(os.path.join(root,fi)), ot)

def main():

    for proc in config.PROCESSING:
        print("Processing ", proc.name)
        out_ = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/processed/"+proc.out + ".csv") ,'w+')
        writer = csv.DictWriter(out_, fieldnames=proc.fields)
        writer.writeheader()
        if isinstance(proc.input, str):
            runProcess(proc.process, writer, proc.input)
        else:
            for i in proc.input:
                runProcess(proc.process, writer, i)


    print()
    print("Post processing to tidy up data")
    print()

    for proc in config.POSTPROCESS:
        proc.process()


        

    # with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/processed/airlines.csv") ,'r+') as f:
    #     reader = csv.DictReader(f, fieldnames = ["id","airline"])
    #     for line in reader:
    #         pass
if __name__ == '__main__':
    main()
