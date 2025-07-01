import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parameters
num_workstreams = 6
num_workpackages_per_workstream = 8
num_tasks_per_workpackage = 8
project_start_date = datetime(2022, 1, 3)

# Generate task durations
durations = np.random.choice(np.arange(11, dtype=np.int32), num_workstreams * num_workpackages_per_workstream * num_tasks_per_workpackage, p= [0.05] + [0.095] * 10)

# Choose which workstreams run in parallel
parallel_workstreams = np.random.choice([True, False], num_workstreams)

# Assign start and finish dates to tasks
start_dates = []
finish_dates = []
current_dates = [project_start_date] * num_workstreams

for ws in range(num_workstreams):
    for wp in range(num_workpackages_per_workstream):
        for task in range(num_tasks_per_workpackage):
            duration = durations[ws * num_workpackages_per_workstream * num_tasks_per_workpackage + wp * num_tasks_per_workpackage + task]
            start_date = current_dates[ws]
            finish_date = start_date + timedelta(days=int(duration))
            start_dates.append(start_date)
            finish_dates.append(finish_date)
            current_dates[ws] = finish_date + timedelta(days=1)  # Sequential tasks within workstream
        if not parallel_workstreams[ws]:
            # If workstream is not parallel, update the start date for the next workstream
            current_dates = [max(current_dates)] * num_workstreams

# Generate random data for PV, EV, and AC
np.random.seed(42)
PV = np.random.uniform(1000, 5000, num_workstreams * num_workpackages_per_workstream * num_tasks_per_workpackage).round(2)
EV = np.random.uniform(1000, 5000, num_workstreams * num_workpackages_per_workstream * num_tasks_per_workpackage).round(2)
AC = np.random.uniform(1000, 5000, num_workstreams * num_workpackages_per_workstream * num_tasks_per_workpackage).round(2)

# Calculate earned value metrics CV, SV, SPI and CPI
SV = (EV - PV).round(2)
CV = (EV - AC).round(2)
SPI = (EV / PV).round(2)
CPI = (EV / AC).round(2)

# Create the dataframe
data = {
    'Workstream': np.repeat(np.arange(1, num_workstreams + 1, dtype=np.int32), num_workpackages_per_workstream * num_tasks_per_workpackage),
    'Work Package': np.tile(np.repeat(np.arange(1, num_workpackages_per_workstream + 1, dtype=np.int32), num_tasks_per_workpackage), num_workstreams),
    'Task': np.tile(np.arange(1, num_tasks_per_workpackage + 1, dtype=np.int32), num_workstreams * num_workpackages_per_workstream),
    'Planned Value (PV)': PV,
    'Earned Value (EV)': EV,
    'Actual Cost (AC)': AC,
    'Schedule Variance (SV)': SV,
    'Cost Variance (CV)': CV,
    'Schedule Performance Index (SPI)': SPI,
    'Cost Performance Index (CPI)': CPI,
    'Start Date': start_dates,
    'Finish Date': finish_dates
}

df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('ev_data_01.csv', index=False)
print("Earned value data has been generated and written to 'ev_data_01.csv'")
