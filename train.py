import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv('./data/202309-baywheels-tripdata.csv')

df.dropna(subset=['start_station_id', 'end_station_id'], inplace=True)
df = df.drop(columns=['start_lat', 'start_lng', 'end_lat', 'end_lng', 'start_station_id', 'end_station_id'])

df.member_casual = (df.member_casual == 'member').astype(int)

df['started_at'] = pd.to_datetime(df['started_at']).dt.floor('H')
df['start_hour_of_day'] = df['started_at'].dt.hour
df['start_weekday'] = df['started_at'].dt.weekday

df.columns = df.columns.str.lower().str.replace(' ', '_')

string_columns = list(df.dtypes[df.dtypes == 'object'].index)

for col in string_columns:
    df[col] = df[col].str.lower().str.replace(' ', '_')

# df_train_full, df_test = train_test_split(df, test_size=0.2, random_state=1)

categorical = ['rideable_type', 'start_station_name']
numerical = ['start_hour_of_day', 'start_weekday']

dv = DictVectorizer(sparse=False)

df_train_full, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_train_full, test_size=0.33, random_state=11)
train_dict = df_train[categorical + numerical].to_dict(orient='records')

y_train = df_train.member_casual.values
y_val = df_val.member_casual.values

X_train = dv.fit_transform(train_dict)
y_train = df_train['member_casual']

model = LogisticRegression(solver='liblinear', C=10, max_iter=1000, random_state=42)
model.fit(X_train, y_train)

with open('model.bin','wb') as f_out:
    pickle.dump((dv,model),f_out)