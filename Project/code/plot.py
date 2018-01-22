import datetime

from helpers import processedPath as r, tidyPath as t
import pandas as pd
import numpy as np
import sys
import matplotlib
import matplotlib.pyplot as plt
claimsDf = pd.read_csv(r("claims.csv"))
flightsDf = pd.read_csv(r("flights.csv"))

d1 = claimsDf.groupby(["month","airline"]).count()
d2 = flightsDf.groupby(["month","airline"]).agg({"delay":np.sum,"cancelled":np.sum})

e = lambda x: "../figures/exploratory/"+x
f = lambda x: "../figures/final/"+x
# 1. number of claims
plt.figure()
ax = claimsDf.groupby(["month"])["item"].count().plot()
plt.tight_layout(pad = 7)
ax.get_figure().savefig(e("1"))

# # 2. plot airline delays
plt.figure()
ax = flightsDf.groupby(["airline"]).agg({"delay":np.sum}).plot(kind="bar", figsize=(19, 10),label="Delay sum")
ax.set_ylabel("Delay sum")
plt.tight_layout(pad = 7)
ax.get_figure().savefig(e("2"))

plt.figure()
ax = flightsDf.groupby(["airline"]).agg({"delay":np.sum})["delay"].sort_values().nlargest(10).plot(kind="bar", figsize=(19, 10),label="Delay sum")
ax.set_ylabel("Delay sum")
plt.tight_layout(pad = 7)
ax.get_figure().savefig(f("2"))

# # 2-bis. plot delay by airline
plt.figure()
ax = flightsDf.groupby(["month","airline"]).agg({"delay":np.sum}).unstack().plot(figsize=(24, 15))
ax.set_ylabel("Delay sum")
ax.legend(bbox_to_anchor=(-1.2, 1))
ax.get_figure().legend(bbox_to_anchor=(-1.2, 1))
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1))
plt.tight_layout(pad=7)
ax.get_figure().savefig(e("2-bis"))

# # 3. claim amount count
plt.figure()
ax = claimsDf.groupby("airline")["claim_amount"].count().plot(kind="bar", figsize=(19, 10),label="Claim count")
ax.set_ylabel("Claim amount")
plt.tight_layout(pad = 7)
ax.get_figure().savefig(e("3"))
plt.figure()
ax = claimsDf.groupby("airline")["claim_amount"].count().sort_values().nlargest(20).plot(kind="bar", figsize=(19,10), title="last")
ax.set_ylabel("Claim count")
ax.legend(bbox_to_anchor=(1.1, 1))
plt.tight_layout(pad = 7)
ax.get_figure().savefig(f("3"))
# 4. mean average
plt.figure()
ax = flightsDf.groupby(["airline"]).agg({"delay":np.mean}).plot(kind="bar", figsize=(19, 10)).legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout(pad = 7)
ax.get_figure().savefig(e("4"))
# 5. max amount lost
plt.figure()
ax = claimsDf.groupby("airline").agg({"claim_amount":np.max}).plot(kind="bar", figsize=(35, 10))
plt.tight_layout(pad=7)
ax.get_figure().savefig(e("5"))
plt.figure()

ax = claimsDf.groupby("airline").agg({"claim_amount":np.max}).sort_values(by=["claim_amount"])["claim_amount"].nlargest(10).plot(kind="bar", figsize=(35, 10))
ax.set_ylabel("claim max value per airline")
plt.tight_layout(pad = 7)
ax.get_figure().savefig(f("5"))


# 6. Combine all
df = flightsDf.groupby(["month","airline"]).agg({"delay":np.sum})

df = df.unstack()
print(df)
ax = df.plot(figsize=(24, 15))
ax.set_ylabel("Delay sum / month")
ax.legend(bbox_to_anchor=(-1.2, 1))
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(-1,1))
plt.tight_layout(pad=7)

# ax.get_figure().savefig(e("2-bis"))

# claimsDf.groupby("airline")["claim_amount"].count().plot(kind="bar", figsize=(19, 10)).get_figure().savefig(f("3"))
ax = claimsDf.groupby("airline")["claim_amount"].count().sort_values().nlargest(10).plot(kind="bar", secondary_y = True, figsize=(19,10))
ax.set_ylabel("Claim count")
ax.legend(bbox_to_anchor=(1.1, 1))
plt.tight_layout(pad = 7)
ax.get_figure().savefig(f("6"), tight_layout=False)


# 6. (todo) Total amount of items lost, with total amount of delays per airline, per month
# conc = pd.concat([d1["item"], d2["delay"]])
# conc.plot().get_figure().savefig("test")
# conc.to_csv("test.csv")
# conc.unstack().plot().get_figure().show()

# apple_fplot = d2['delay']
# plot_df = apple_fplot.unstack('airline').loc[:, 'delay']
# plot_df.index = pd.PeriodIndex(plot_df.index.tolist(), freq='American Airline')
# plot_df.plot().get_figure().show()


# conc = pd.concat(
#     [d1.filter(["month", "airline", "item"], axis=1), d2.filter(["month", "airline", "delay"], axis=1)]
# )
# fig, ax = plt.subplots()
# width=0.3
#
# ax.bar(conc.index, conc.item, width=width, color='red', label='col1_data')
# ax.legend(loc='best')
# ax2 = ax.twinx()
# ax2.line(conc.index+width, conc.delay, width=width, color='blue', label='col2_data')
# ax2.legend(loc='best')


# flightsDf.groupby(["airline"]).agg({"delay":np.sum})["delay"].plot().get_figure().show()
# pd.concat(     [claimsDf.groupby("month").count().filter(["month", "airline", "Item"], axis=1), flightsDf.groupby("month").agg({"delay",np.sum}).filter(["month", "airline", "delay"], axis=1)] )
# #
# print(pd.concat([d1,d2]))
# pd.concat([d1.filter(["date", "airline", "Item"], axis=1), d2.filter(["date", "airline", "delay"], axis=1)]).to_csv(t("all.csv"))