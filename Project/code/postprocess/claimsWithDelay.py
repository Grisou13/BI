from postprocess import Processor
import pandas as pd
import numpy as np
from helpers import processedPath as r, tidyPath as t

class ClaimsWithDelayPostProcessor(Processor):
    def process(self):
        claimsDf = pd.read_csv(r("claims.csv"), index_col=("date","airline","Item"))

        d1 = claimsDf.groupby(["date","airline"]).count()

        flightsDf = pd.read_csv(r("flights.csv"), index_col=("date","airline","delay"))
        d2 = flightsDf.groupby(["date","airline"]).count()

        print(pd.concat([d1,d2]))
        pd.concat([d1.loc[:, 'date':'airline',"Item"],d2.loc[:, 'date':'airline',"delay"]]).to_csv(t("all.csv"))