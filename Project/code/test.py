from helpers import processedPath as r, tidyPath as t
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
claimsDf = pd.read_csv(r("claims.csv"))
flightsDf = pd.read_csv(r("flights.csv"))

d1 = claimsDf.groupby(["month","airline"]).count()
d2 = flightsDf.groupby(["month","airline"]).agg({"delay":np.sum,"cancelled":np.sum})
# plot airline delays
flightsDf.groupby(["airline"]).agg({"delay":np.sum}).plot(kind="bar").get_figure().show()
# mean average
flightsDf.groupby(["airline"]).agg({"delay":np.mean}).plot(kind="bar").get_figure().show()

#max amount lost
claimsDf.groupby("airline").agg({"Claim Amount":np.max}).plot(kind="bar").get_figure().show()

# conc = pd.concat(
#     [d1.filter(["month", "airline", "Item"], axis=1), d2.filter(["month", "airline", "delay"], axis=1)]
# )
# flightsDf.groupby(["airline"]).agg({"delay":np.sum})["delay"].plot().get_figure().show()
# pd.concat(     [claimsDf.groupby("month").count().filter(["month", "airline", "Item"], axis=1), flightsDf.groupby("month").agg({"delay",np.sum}).filter(["month", "airline", "delay"], axis=1)] )
# #
# print(pd.concat([d1,d2]))
# pd.concat([d1.filter(["date", "airline", "Item"], axis=1), d2.filter(["date", "airline", "delay"], axis=1)]).to_csv(t("all.csv"))