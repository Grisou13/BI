#!/usr/bin/python3
import os, sys, glob
from processing.claims import ClaimsProcessor
from processing.flights import FlightProcessor
from postprocess.airline import AirlinePostProcessor
from postprocess.claims import ClaimsPostProcessor
from postprocess.flights import FlightsPostProcessor
from postprocess.claimsWithDelay import ClaimsWithDelayPostProcessor

PROCESSING = [
	ClaimsProcessor(),
	FlightProcessor(),
]

POSTPROCESS = [
	# AirlinePostProcessor(),
	# FlightsPostProcessor(),
	# ClaimsPostProcessor(),
	ClaimsWithDelayPostProcessor()
]
