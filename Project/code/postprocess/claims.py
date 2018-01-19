from postprocess import Processor
import pandas as pd
import numpy as np
from helpers import processedPath as r, tidyPath as t
class ClaimsPostProcessor(Processor):
    def process(self):
        df = pd.read_csv(r("claims.csv"))
        df.groupby(["date","airline"]).count().to_csv(t("claims_count.csv"))
