'''
#1
-There is an obvious dip in number of flights during the 2008 financial crisis due to the significant less amount
    of people having spare money to buy tickets for vacations
-There is a seasonal trend of every year having four peaks around during the middle of every single season due to
    the high number of familys either vacationing or visiting relatives during this time
-Ever since the 2008 financial crisis there has been a continual drop in flights in comparison to the year before
    likely due to a bad economic climate

#2
-Over a fouth of all Airport trafic comes from three airports alone, ATL, ORD, DFW
-The most used airports are high in trafic due to there positioning within the USA, for some being on a coast close to
    either europe or asia or others that are within the MID USA for hubs which have high number of connecting flights
    to smaller airports accross the mainland
-When I made this I much expected there to be more airports within the North east of the USA. But nont of them crack
    even the top 5, this is likely due to within the NE United States being so compact there is no requirements for
    connecting flights and people instead use other modes of transportation
'''

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------
# CSCI 127, Project 5                                 |
# June 23, 2020                                       |
# Adam Wulfing                                        |
# -----------------------------------------------------

def create_viz1(df, filename):
    #first visualization line chart
    data = df.groupby(['Time.Label'])["Statistics.Flights.Total"].sum()
    data.plot.line(x='Time.Label', y='Statistics.Flights.Total',title='Number of Flights In Major US Airports Over Time')
    plt.xlabel("Number of Flights")
    plt.ylabel("Time by Month")
    #plt.savefig(filename)

def create_viz2(df, filename):
    #second visualization pie chart
    data = df.groupby(['Airport.Code']).sum()
    data.plot.pie(y='Statistics.Flights.Total',figsize=(12, 7), startangle=90, title='Percentage Of Flights Through The USA Per Airport', autopct='%1.0f%%', pctdistance=.9,)
    plt.ylabel("Airports")
    plt.show()
    #plt.savefig(filename)

def main():
    #load data
    df = pd.read_csv("airlines.csv")
    df.drop(["Airport.Name","Statistics.# of Delays.Carrier","Statistics.# of Delays.Late Aircraft","Statistics.# of Delays.National Aviation System",
             "Statistics.# of Delays.Security","Statistics.# of Delays.Weather","Statistics.Carriers.Names","Statistics.Carriers.Total",
             "Statistics.Flights.Cancelled","Statistics.Flights.Delayed","Statistics.Flights.Diverted","Statistics.Flights.On Time",
             "Statistics.Minutes Delayed.Carrier","Statistics.Minutes Delayed.Late Aircraft","Statistics.Minutes Delayed.National Aviation System",
             "Statistics.Minutes Delayed.Security","Statistics.Minutes Delayed.Total"],axis=1).head()
    create_viz1(df, "visualization1.png")
    create_viz2(df, "visualization2.png")

# -----------------------------------------------------

main()
