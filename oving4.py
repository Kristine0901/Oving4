import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Oppgave 4
df = pd.read_csv("Oving4/load_data.csv", decimal=",")

# Gjør indeksen om til DatetimeIndex
df.columns = df.columns.str.strip()
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"],dayfirst = True, utc=True)
df = df.set_index("Time(Local)")
df = df.sort_index()
df = df.tz_convert("Europe/Oslo")

print(df.head())

# Oppgave 5
print(df.index[0])
