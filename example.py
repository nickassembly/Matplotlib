import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Real World Example

gas = pd.read_csv('./data/gas_prices.csv')

plt.figure(figsize=(8, 5))

plt.plot(gas.Year, gas.USA, 'b.-', label="USA")
plt.plot(gas.Year, gas.Canada, 'r.-', label="Canada")
plt.plot(gas.Year, gas['South Korea'], 'g.-', label="South Korea")
plt.plot(gas.Year, gas.Australia, 'y.-', label="Australia")

# Another way to plot values
# countries_to_look_at = ['Australia', 'USA', 'Canada', 'South Korea']

# for country in gas:
#     if country in countries_to_look_at:
#         plt.plot(gas.Year, gas[country], marker='.', label=country)

plt.xticks(gas.Year[::3])
plt.xticks(gas.Year[::3])

plt.xlabel('Year')
plt.ylabel('US Dollar')

plt.title('Gas Prices over Time (in USD)', fontdict={
          'fontweight': 'bold', 'fontsize': 18})
plt.ylabel('Dollars/Gallon')
plt.legend()


plt.show()
