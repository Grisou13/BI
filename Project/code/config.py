#!/usr/bin/python3
import os, sys, glob
from processing.claims import ClaimsProcessor
from processing.flights import FlightProcessor

BASE_FOLDER = os.path.realpath("../data/raw/")

PROCESS_FILE="process.py"

PROCESSING = [
	ClaimsProcessor(),
	FlightProcessor(),
	#processing.flightCount.FlightCountProcessor(),
]
