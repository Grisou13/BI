from postprocess import Processor
import pandas as pd
import numpy as np
from helpers import processedPath as r, tidyPath as t

class ClaimsWithDelayPostProcessor(Processor):
    def process(self):
        claimsDf = pd.read_csv(r("claims.csv"))

        d1 = claimsDf.groupby(["month","airline"]).count()

        flightsDf = pd.read_csv(r("flights.csv"))
        d2 = flightsDf.groupby(["month","airline"]).agg({"delay":np.sum,"cancelled":np.sum})

        print(pd.concat([d1,d2]))
        pd.concat(
            [d1.filter(["month", "airline", "Item"], axis=1), d2.filter(["month", "airline", "delay"], axis=1)]
        ).to_csv(t("all.csv"))
