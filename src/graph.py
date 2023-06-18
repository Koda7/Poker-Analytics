import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# hands = [
#     'AAo', 'AQs', 'KJs', 'A5s', 'K9o', 'K6s', 'K4s', 'J9o', 'K3o', 'J5s',
#     '87s', '86s', '96o', '95o', '94o', '43s', '73o', '32o'
# ]

hands = [
    'AAo', 'KKo', 'QQo', 'JJo', 'TTo', '99o', '88o', 'AKs', '77o', 'AQs',
]

# hands = [
#     'AAo', 'AQs'
# ]

# read preflop_equity.csv
df = pd.read_csv('preflop_equity.csv', header=None)

# x axis will be the number of players  1 to 10
x = np.arange(2, 11)

selected_rows = df[df[0].isin(hands)]

# remove the first column and store it separately
# this is the hand name

# separate out first column of selected rows
hands2 = selected_rows.iloc[:, 0]

# convert hands to a list
hands2 = hands2.tolist()

print(hands2)

y = np.array(selected_rows.iloc[:, 1:])


# remove first column
y = y[:, 1:]

# print(y)

# remove the % sign from the end of each value and convert to float
y = np.array([list(map(lambda x: float(x[:-1]), row)) for row in y])

# axes titles 
plt.xlabel('Number of Players')
plt.ylabel('Income Rate')

# plot title 
plt.title('Preflop Income Rate vs. Number of Players')

# change y-axis labels intervals
plt.yticks(np.arange(0, 101, 5))

# plot line graphs for each hand
for i in range(len(hands2)):
    plt.plot(x, y[i], linestyle=('-' if y[i][0] > 50 else '--'),label=hands2[i], marker='o')

# make a legend
plt.legend()

plt.show()
