import config
import csv
import os
import pandas as pd
import numpy as np

r = lambda x : os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/processed/",x))
t = lambda x : os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/tidy/",x))

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
    df = pd.read_csv(r("flights.csv"))
    # df['delay'] = df.apply(lambda x: x['late_aircraft_delay'] + x['carrier_delay'], axis=1)
    df.groupby(["date","airline"]).agg({"delay":np.sum,"cancelled":np.sum}).to_csv(t("airline_delays.csv"))
    df.groupby(["date","airline"]).count().to_csv(t("airline_count.csv"))

    df = pd.read_csv(r("claims.csv"))
    df.groupby(["date","airline"]).count().to_csv(t("claims_count.csv"))

    # with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/processed/airlines.csv") ,'r+') as f:
    #     reader = csv.DictReader(f, fieldnames = ["id","airline"])
    #     for line in reader:
    #         pass
if __name__ == '__main__':
    main()
