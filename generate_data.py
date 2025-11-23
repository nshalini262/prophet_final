import pandas as pd
import random 

# daily dates for 2022
ds = pd.date_range(start="2025-01-01", end="2025-12-31")

# empty list for hours of sleep
y = []

# constraints for hours of sleep
for i in range(365):
    # school break
    if (i < 15) or (120 < i < 233) or (339 < i < 365):
        y.append(random.randint(7, 12))

    # school days
    elif (15 <= i <= 102) or (233 <= i <= 321):
        y.append(random.randint(5, 8))

    # finals
    else:
        y.append(random.randint(0, 5))

# creating data frame + csv file
data = pd.DataFrame({"ds": ds, "y": y})
data.to_csv('prophet_vals.csv', encoding='utf-8', index=False)
