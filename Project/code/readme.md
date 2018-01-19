# Bi processing

These scripts tidy up all the data present in [the raw data folder](../data/raw).


## Requirements


- python3
- pip

## Installation

```
python3 -m pip install -r requirements.txt
```

## Usage

```
python3 app.py
```

## How it works

The app.py script will launch multiple processes in a couple of stages

1. Processing
  This creates the processed data, and sanitizes it
2. Post PROCESSING
  This creates the tidy data with all the necessary groupings

The data is processed by multiple processors, each one handles a specific file in the raw/** folder.

### List of processors

| file                   | class                | Input folder                                         | output                                                   | Description                                                                                                                           | Input columns                                                                                                                                  | Output columns                                                                             |
|------------------------|----------------------|------------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| processing/flights.py  | FlightProcessor      | data/raw/flights/**.*.csv                            | data/processed/flights.csv                               | Filters out all unwanted columns, and adds up all the delays that are caused by carriers                                              | "year","month","carrier_name","arr_flights","arr_cancelled","arr_diverted"," arr_delay"," carrier_delay","weather_delay","late_aircraft_delay" | "date","airline","delay","carrier_delay","weather_delay","late_aircraft_delay","cancelled" |
| processing/claims.py   | ClaimsProcessor      | data/raw/claims/**.*.xls*                            | data/processed/claims.csv                                | Adds up all the files, and filters only wanted columns. This processor is mainly just an aggreagator                                  | "Incident Date","Airline Name","Item","Claim Amount"                                                                                           | "date", "airline", "Item", "Claim Amount"                                                  |
| postprocess/flights.py | FlightsPostProcessor | data/processed/flights.csv                           | data/tidy/airline_delays.csv data/tidy/airline_count.csv | Tidies up the data, and groups by the data. Spits out the same columns than the input but with counting the number of entries present | "date","airline","delay","carrier_delay","weather_delay","late_aircraft_delay","cancelled"                                                     | "date","airline","delay","carrier_delay","weather_delay","late_aircraft_delay","cancelled" |
| postprocess/claims.py  | ClaimsPostProcessor  | data/processed/claims.csv                            | data/tidy/claims_count.csv                               | Tidies up the data, and groups by the data. Spits out the same columns than the input but with counting the number of entries present | "date", "airline", "Item", "Claim Amount"                                                                                                      | "date", "airline", "Item", "Claim Amount"                                                  |
| postprocess/airline.py | AirlinePostProcessor | data/processed/flights.csv data/processed/claims.csv | data/tidy/airlines.csv                                   | Creates a pivot table to link airlines.                                                                                               | *                                                                                                                                              | *                                                                                          |
