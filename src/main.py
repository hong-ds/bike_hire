import pandas as pd
import glob
from functools import lru_cache
import seaborn as sns
import matplotlib.pyplot as plt



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

def create_overview_ts(dataframe: pd.DataFrame) -> pd.DataFrame: 
    df = dataframe.copy()
    df.drop(["end_date", "duration_sec"], axis=1, inplace=True)
    return df.set_index("start_date")

df = load_data(FILE_PATTERN)
df = df.loc[
        (df.start_date >= START_DATE) &
        (df.end_date < END_DATE)
    ].reset_index(drop=True)

overview = create_overview_ts(df)

daily_traffic = overview.resample("D")["end_station_code"].count().to_frame("num_of_trips")
sns.lineplot(data=daily_traffic)
plt.show()
count_by_weekday = df.groupby(["year", "weekday"])[['start_date']].count()
count_by_weekday.columns = ["tot_counts"]
count_by_weekday.reset_index(inplace=True)
count_by_month = df.groupby([df.start_date.dt.year, df.start_date.dt.month, df.is_member])[['start_date']].count().reset_index(name="tot_counts")
count_by_day_of_month = df.groupby([df.start_date.dt.year, df.start_date.dt.days_in_month, df.is_member])[['start_date']].count().reset_index(name="tot_counts")