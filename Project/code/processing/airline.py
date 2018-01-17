#!/usr/bin/python
import os
import csv
from processing import Processor
from cleanco import cleanco
from processing.claims import ClaimsProcessor
from processing.flights import FlightProcessor

def getRawPath(*args, **kwargs):
    return os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../../data/raw/",*args))

class DictWriterWrapper():
    rows = []

    def writerow(self, r):
        self.rows.append(r)
class AirlineProcessor(Processor):
    input=["claims","flights"]
    out = "airlines"
    fields = ["id","airline"]
    wrapper = DictWriterWrapper()

    def process(self, in_, out):
        #f = ["year","month","carrier","carrier_name","airport","airport_name","arr_flights","arr_del15","carrier_ct","weather_ct","nas_ct","security_ct","late_aircraft_ct","arr_cancelled","arr_diverted"," arr_delay"," carrier_delay","weather_delay","nas_delay","security_delay","late_aircraft_delay"]
        wrapper = self.wrapper
        proc = None

        if in_.startswith(getRawPath("flights")):
            proc = FlightProcessor()
        elif in_.startswith(getRawPath("claims")):
            proc = ClaimsProcessor()

        proc.process(in_, wrapper)

        airlines = []
        for r in wrapper.rows:
            if r["airline"] not in airlines:
                airlines.append(r["airline"])
        for k, airline in enumerate(airlines):
            out.writerow({"id":k, "airline": airline})
