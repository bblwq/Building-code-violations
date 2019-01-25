# Load the helper library
import pandas as pd

# Import data
df = pd.read_csv('C4C-dev-challenge-2018.csv', parse_dates=['violation_date'])

# Select columns needed
category_with_date = df[['violation_category', 'violation_date']]

# Group dates by category
date_by_category = category_with_date.groupby('violation_category')['violation_date'].apply(list)

# Calculate the number of violations in each category
num_of_violations = date_by_category.apply(len)

# Find the earliest date in each category
earliest_dates = date_by_category.apply(min)

# Find the latest date in each category
latest_dates = date_by_category.apply(max)

# Merge the results
output = pd.concat([num_of_violations.rename('Count'), earliest_dates.rename('Earliest_Date'), latest_dates.rename('Latest_Date')], axis=1)

# Print out the results
print(output)