#!/usr/bin/python
import os
import csv
from . import Processor
from cleanco import cleanco


class FlightProcessor(Processor):
    input = "flights"
    out = "flights"
    fields = []
    def process(self, in_, out):
        #f = ["year","month","carrier","carrier_name","airport","airport_name","arr_flights","arr_del15","carrier_ct","weather_ct","nas_ct","security_ct","late_aircraft_ct","arr_cancelled","arr_diverted"," arr_delay"," carrier_delay","weather_delay","nas_delay","security_delay","late_aircraft_delay"]
        reader = csv.DictReader(open(in_,"r"), delimiter = ",")
        print(reader)
        for row in reader:
            row["date"] = row["year"] + "-" +row["month"]
            row["airline"] = cleanco(row["carrier_name"]).clean_name()
            out_r = {}
            for k in self.fields:
                try:
                    out_r[k] = row[k]
                except KeyError:
                    pass

            out.writerow(out_r)
