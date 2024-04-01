import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
sh_raw = pd.read_csv('movies.csv', 
   header = None, 
   names = ['Year','Title','Comic','IMDB','RT','','OpeningWeekendBoxOffice','AvgTicketPriceThatYear','EstdOpeningAttendance','USPopThatYear'])

sh = sh_raw[np.isfinite(sh_raw.OpeningWeekendBoxOffice)]
# print(sh.head(5))


imdb_normalized = sh.IMDB / 10     
sh.insert(10,'IMDBNormalized',imdb_normalized)
rt_normalized = sh.RT/100
sh.insert(11, 'RTNormalized', rt_normalized)
sh.plot.scatter(x ='RTNormalized', y ='IMDBNormalized')
# plt.show()

# print(sh[['RTNormalized','IMDBNormalized']].corr())
# print(sh[['RTNormalized','IMDBNormalized']].describe())

#RQ1  Define a command to print the Series rows for the 'DC' comic movies from the sh DataFrame. There should be 18 rows.
DCRows = sh
DCRows = DCRows[sh.Comic == "DC"]
# print(DCRows)

#RQ2  Define a command to print just 2 columns - the Year and Title columns of only 'DC' movies from the sh DataFrame.
Marvels = sh
Marvels = Marvels[sh.Comic == "Marvel"]
desiredCols = ['Year', 'Title']
Marvels = Marvels[desiredCols]
# print(Marvels)

#RQ3  Define a command to print just 2 columns - the Year and Title columns of only 'Marvel' movies from the sh DataFrame
DCRows = DCRows[desiredCols] #Use RQ1 data.
# print(DCRows)

#RQ4  Define a command to plot a scatterplot  for the AvgTicketPriceThatYear on the y-axis and with Year on the x axis.
sh.plot.scatter(x ='Year', y ='AvgTicketPriceThatYear')
# plt.show()

#RQ5  Define a command to print the correlation for the Year versus the AvgTicketPriceThatYear.
print(sh[['Year','AvgTicketPriceThatYear']].corr())

#RQ6  Define a command to print the summary statistics for OpeningWeekendBoxOffice.
print(sh[['OpeningWeekendBoxOffice']].describe()) # I think this is what they want

