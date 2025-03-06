import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

# Training and running a linear model using SciKit-Learn

# This function just merges the OECD's life satisfaction data and the IMF's GDP per capita data.


def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"]
    oecd_bli = oecd_bli.pivot(
        index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]


# Initially loading the data (Assumes files are in same directory)
oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=',')
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t',
                             encoding='latin1', na_values="n/a")

# Prepare the data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]

# Select a linear model
model = sklearn.linear_model.LinearRegression()

# Train the model
model.fit(X, y)

# Generate a Trend Line
X_range = np.linspace(X.min(), X.max(), 1000).reshape(-1, 1)
y_range = model.predict(X_range)

# Visualize the data
country_stats.plot(kind='scatter', x="GDP per capita",
                   y='Life satisfaction')
plt.plot(X_range, y_range, color='blue', linestyle="-",
         label="Linear function that best fits training data set")
plt.show()

# Make a prediction for Cyprus
X_new = [[22587]]
print(model.predict(X_new))
