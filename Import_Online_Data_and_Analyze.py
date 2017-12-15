import pandas as pd
import matplotlib.pyplot as plt
try:
    import wget
except:
    # install wget if needed
    import pip
    pip.main(['install','wget'])
    import wget

# stock ticker symbol
stock = 'GOOG'
url = 'https://apmonitor.com/che263/uploads/Main/goog.csv'
#url = 'http://chart.finance.yahoo.com/table.csv?s='+stock
filename = wget.download(url)

# rename file
from shutil import move
move(filename,stock.lower()+'.csv')

# import data with pandas
data = pd.read_csv(stock+'.csv')
print(data['Close'][0:5])
print('min: '+str(min(data['Close'][0:20])))
print('max: '+str(max(data['Close'][0:20])))

# plot data with pyplot
plt.figure()
plt.plot(data['Open'][0:20])
plt.plot(data['Close'][0:20])
plt.xlabel('days ago')
plt.ylabel('price')
plt.show()
