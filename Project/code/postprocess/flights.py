from postprocess import Processor
import pandas as pd
import numpy as np
from helpers import processedPath as r, tidyPath as t
class FlightsPostProcessor(Processor):
    def process(self):
        df = pd.read_csv(r("flights.csv"))
        # df['delay'] = df.apply(lambda x: x['late_aircraft_delay'] + x['carrier_delay'], axis=1)
        df.groupby(["date","airline"]).agg({"delay":np.sum,"cancelled":np.sum}).to_csv(t("airline_delays.csv"))
        df.groupby(["date","airline"]).count().to_csv(t("airline_delay_count.csv"))
