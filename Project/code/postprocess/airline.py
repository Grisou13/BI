#!/usr/bin/python

import csv
from postprocess import Processor
from cleanco import cleanco
from processing.claims import ClaimsProcessor
from processing.flights import FlightProcessor
from helpers import processedPath, tidyPath
def getRawPath(*args, **kwargs):
    return os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../../data/raw/",*args))

class DictWriterWrapper():
    rows = []

    def writerow(self, r):
        self.rows.append(r)
class AirlinePostProcessor(Processor):
    fields = ["id","airline"]
    files = ["flights.csv","claims.csv"]
    out = "airlines.csv"
    airlines = []
    def add(self, csv):
        for r in csv:
            if r["airline"] not in self.airlines:
                self.airlines.append(r["airline"])
    def process(self):
        for f in self.files:
            f_ = open(processedPath(f),"r+")
            csv_ = csv.DictReader(f_)
            self.add(csv_)
        f_ = open(tidyPath(self.out),"w+")
        out = csv.DictWriter(f_, fieldnames = self.fields)
        out.writeheader()
        for k, airline in enumerate(self.airlines):
            out.writerow({"id":k, "airline": airline})
