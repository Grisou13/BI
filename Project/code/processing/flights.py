#!/usr/bin/python
import os
import csv
from processing import Processor
from cleanco import cleanco
from calendar import monthrange
def mk_float(s):
    s = s.strip()
    return float(s) if s else 0

def mk_int(s):
    s = s.strip()
    return int(s) if s else 0

class FlightProcessor(Processor):
    name = "flights"
    input = "flights"
    out = "flights"
    fields = ["date","month","airline","arr_flights","delay","carrier_delay","weather_delay","late_aircraft_delay","cancelled"]
    def process(self, in_, out):
        #f = ["year","month","carrier","carrier_name","airport","airport_name","arr_flights","arr_del15","carrier_ct","weather_ct","nas_ct","security_ct","late_aircraft_ct","arr_cancelled","arr_diverted","arr_delay"," carrier_delay","weather_delay","nas_delay","security_delay","late_aircraft_delay"]
        reader = csv.DictReader(open(in_,"r"), delimiter = ",")
        for row in reader:

            row["date"] = row["year"] + "-" +row["month"]
            row["month"] = row["year"] + "-" +row["month"]
            row["airline"] = cleanco(row["carrier_name"]).clean_name()
            row["cancelled"] = row["arr_cancelled"]
            row["delay"] = mk_float(row['late_aircraft_delay']) + mk_float(row['carrier_delay'])+mk_float(row["arr_delay"])
            out_r = {}
            for k in self.fields:
                try:
                    out_r[k] = row[k]
                except KeyError:
                    pass
            out_r["date"] = out_r["date"]+"-01"
            out.writerow(out_r)
            continue
            # for day in  monthrange(row["year"], row["month"])[1]:
            #     out_r["date"] = out_r["date"]+ "-" + '{0:02d}'.format(day)
            #     out.writerow(out_r)
