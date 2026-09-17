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

#oppgave 6
df6 = df.loc["2026-01-01 03:00:00 +01:00"]
df6.plot(kind= "bar", figsize=(10,5))
plt.title("Produksjon og consumption 01.01.2026 kl 03:00:00")
plt.grid(True)

plt.savefig("Oving4/Observasjonkl0300.png")

plt.show()

df61 = df.loc["2026-01-01 00:00:00 +01:00": "2026-01-01 23:00:00 +01:00"]
df61.plot(figsize=(10,5))
plt.title("Produksjon og consumption 01.01.2026 kl 00:00 til kl 23:00 +01:00")
plt.grid(True)

plt.savefig("Oving4/ObservasjonEnLastProfil.png")

plt.show()

#oppgave 7
df["Netto"] = (df["Production"] - df["Consumption"])
print(df["Netto"])
