#!/usr/bin/python
import os
import csv
from processing import Processor

class FlightProcessor(Processor):
    name="flights"
    fields = ["date","carrier_name","carrier_delay","weather_delay","late_aircraft_delay","cancelled"]
    def process(self, in_, out):
        reader = csv.DictReader(open(in_,"r"), delimiter = ",")
        print(reader)
        for row in reader:
            print(row)
            row["date"] = row["year"]+row["month"]
            out.writerow(row)
