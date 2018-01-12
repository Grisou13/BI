#!/usr/bin/python
import os
class ClaimsProcessor(Processor):
    name = "claims"
    def process(self, folder):
        for root, dirs, files in os.walk(folder):
            for f in files:
    def _cumulateFile(self, )
