import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('billionaires.csv')
df = data[['name', 'year','wealth.worth in billions']]
gates = df[df.name == 'Bill Gates']
buff = df[df.name == 'Warren Buffett']
print(gates)
print(buff)
#plt.plot(gates[x = 'year', y = 'wealth.worth in billions'])
#plt.plot.line(buff['year', 'wealth.worth in billions'])

fig, ax = plt.subplots(1, figsize=(8, 6))

# Set the title for the figure
fig.suptitle('Multiple Lines in Same Plot', fontsize=15)

# Draw all the lines in the same plot, assigning a label for each one to be
# shown in the legend.
plt.plot('year', 'wealth.worth in billions', color="red", label="My Line 1")
plt.plot('year', 'wealth.worth in billions', color="green", label="My Line 2")

# Add a legend, and position it on the lower right (with no box)
plt.legend(loc="lower right", title="Legend Title", frameon=False)

plt.show()
