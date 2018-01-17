import config
import csv
import os
def f_(f, ot, in_):
    for root, dirs, files in os.walk(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/raw/"+in_)):
        for fi in files:
            print("processing file ",os.path.join(root,fi) )
            f(os.path.realpath(os.path.join(root,fi)), ot)
for proc in config.PROCESSING:
    print("Processing ", proc.name)
    out_ = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/processed/"+proc.out + ".csv") ,'w+')
    writer = csv.DictWriter(out_, fieldnames=proc.fields)
    writer.writeheader()
    if isinstance(proc.input, str):
        f_(proc.process, writer, proc.input)
    else:
        for i in proc.input:
            f_(proc.process, writer, i)
