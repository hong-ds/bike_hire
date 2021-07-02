import pandas as pd
import os
import glob
from functools import lru_cache

BASE_PATH = "data"
FILE_PATTERN = BASE_PATH + "/*/OD*"
START_STATION = 6184
END_STATION = 6015
START_DATE = "2014-01-01"
END_DATE = "2017-09-01"

@lru_cache
def load_data(path_pattern: str) -> pd.DataFrame:
    filepath = [pd.read_csv(name, parse_dates=["start_date", "end_date"]) for name in glob.glob(path_pattern)]
    df = pd.concat(filepath)
    return df

df = load_data(FILE_PATTERN)
df = df.loc[
        (df.start_station_code == START_STATION) & 
        (df.end_station_code == END_STATION) & 
        (df.start_date >= START_DATE) &
        (df.end_date < END_DATE)
    ].reset_index(drop=True)


count_by_weekday = df.groupby([df.start_date.dt.year, df.start_date.dt.weekday, df.is_member])[['start_date']].count()
count_by_weekday.columns = ["tot_counts"]
count_by_weekday.reset_index(inplace=True)
count_by_month = df.groupby([df.start_date.dt.year, df.start_date.dt.month, df.is_member])[['start_date']].count().reset_index(name="tot_counts")
count_by_day_of_month = df.groupby([df.start_date.dt.year, df.start_date.dt.days_in_month, df.is_member])[['start_date']].count().reset_index(name="tot_counts")