#!/usr/bin/python3
import os, sys, glob
from processing.claims import ClaimsProcessor
from processing.flights import FlightProcessor
from processing.airline import AirlineProcessor
from postprocess.normalise import NormaliseProcessor
BASE_FOLDER = os.path.realpath("../data/raw/")

PROCESSING = [
	# ClaimsProcessor(),
	# FlightProcessor(),
	AirlineProcessor()
	#processing.flightCount.FlightCountProcessor(),
]

POSTPROCESS = [
	NormaliseProcessor()
]