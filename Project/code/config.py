#!/usr/bin/python3
import os, sys, glob
import processing
BASE_FOLDER = os.path.realpath("../data/raw/")

PROCESS_FILE="process.py"

PROCESSING = [
	processing.claims.ClaimsProcessor(),
	processing.flights.FlightProcessor(),
	processing.flightCount.FlightCountProcessor(),
]
