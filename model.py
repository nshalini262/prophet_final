import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

df = pd.read_csv('prophet_vals.csv')

m = Prophet()
m.fit(df)

# generating dates till may 5th 
future = m.make_future_dataframe(periods = 125)

# forecasting
forecast = m.predict(future)
forecast[['ds', 'yhat']].tail()
print(forecast.tail())

# plots
fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)
plt.show()