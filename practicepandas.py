import pandas as pd

import matplotlib.pyplot as plt


air_quality = pd.read_csv("./air_quality_no2.csv", index_col=0, parse_dates=True)

# air_quality.head()


# I want to express the NO2 concentration of the station in London in mg/m

air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

# I want to check the ratio of the values in Paris versus Antwerp and save the result in a new column.

air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]


# I want to rename the data columns to the corresponding station identifiers used by OpenAQ.
rename_air_quality = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)

rename_air_quality = rename_air_quality.rename(columns=str.lower)


print(rename_air_quality.head())


