#!/usr/bin/python
import os
from processing import Processor

class FlightCountProcessor(Processor):
    def process(self, folder):
        for root, dirs, files in os.walk(folder):
            for f in files:
                pass
    def _cumulateFile(self, s):
        pass
