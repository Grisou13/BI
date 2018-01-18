#!/usr/bin/python3
import os, sys, glob
from processing.claims import ClaimsProcessor
from processing.flights import FlightProcessor
from postprocess.airline import AirlineProcessor

PROCESSING = [
	ClaimsProcessor(),
	FlightProcessor(),
	AirlineProcessor()
]
