import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, axes = plt.subplots(figsize=(10,10))
    axes.scatter(df["Year"], df['CSIRO Adjusted Sea Level'], label='OG')

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years = pd.Series(range(1880, 2051), name="year")
    axes.plot(years, years * result.slope + result.intercept, color="red")

    # Create second line of best fit
    new = df[df['Year'] >= 2000]
    new_years = pd.Series(range(2000, 2051), name=" new year")
    new_result = linregress(new["Year"], new["CSIRO Adjusted Sea Level"])
    axes.plot(new_years, new_years * new_result.slope + new_result.intercept, color="yellow")

    # Add labels and title
    axes.set_title("Rise in Sea Level")
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
