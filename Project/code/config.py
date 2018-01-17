#!/usr/bin/python3
import os, sys, glob
from processing.claims import ClaimsProcessor
from processing.flights import FlightProcessor
from processing.airline import AirlineProcessor
BASE_FOLDER = os.path.realpath("../data/raw/")

PROCESS_FILE="process.py"

PROCESSING = [
	# ClaimsProcessor(),
	# FlightProcessor(),
	AirlineProcessor()
	#processing.flightCount.FlightCountProcessor(),
]
