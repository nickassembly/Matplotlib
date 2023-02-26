import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('./data/fifa_data.csv')
# print(fifa.head(5))

# Histograms

# bins = [40, 50, 60, 70, 80, 90, 100]

# plt.hist(fifa.Overall, bins=bins, color='#abcdef')

# plt.xticks(bins)

# plt.ylabel('Number of Players')
# plt.xlabel('Skill Level')
# plt.title('Distribution of Player Skills in FIFA 2018')

# plt.show()

# Pie Charts

# left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
# right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

# labels = ['Left', 'Right']
# colors = ['#abcdef', '#aabbcc']

# plt.pie([left, right], labels=labels, colors=colors, autopct='%.2f %%')

# plt.title('Foot Preference of FIFA Players')

# plt.show()

# fifa.Weight = [int(x.strip('lbs')) if type(
#     x) == str else x for x in fifa.Weight]

# plt.style.use('ggplot')

# light = fifa.loc[(fifa.Weight < 125)].count()[0]
# light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
# medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
# medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
# heavy = fifa.loc[(fifa.Weight >= 200)].count()[0]

# weights = [light, light_medium, medium, medium_heavy, heavy]
# labels = ['Under 125', '125-150', '150-175', '175-200', 'Over 200']
# explode = (.4, .1, 0, 0, 0.4)

# plt.title('Weight Distribution of FIFA Players (in libs)')

# plt.pie(weights, labels=labels, autopct='%.2f %%',
#         pctdistance=0.8, explode=explode)  # pct distance and explode distances can be used to letting the graph become more readable

# plt.show()
plt.style.use('default')

plt.figure(figsize=(5, 8))

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']

labels = ['FC Barcelona', 'Real Madrid', 'NE Revolution']

boxes = plt.boxplot([barcelona, madrid, revs],
                    labels=labels, patch_artist=True, medianprops={'linewidth': 2})

for box in boxes['boxes']:
    # Set edge color
    box.set(color='#4286f4', linewidth=2)

    # change fill color
    box.set(facecolor='#e0e0e0')

plt.title('Professional Soccer Team Comparison')
plt.ylabel('FIFA Overall Rating')

plt.show()
