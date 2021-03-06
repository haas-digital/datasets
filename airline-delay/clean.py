import pandas as pd
import numpy as np
import json

SFO_id = 14771
RANDOM_SEED = 1

class Airline:
    def __init__(self, json_fp):
        #self.dir = dir
        # specify json filepath
        with open(json_fp) as f:
            self.ca_airports = json.load(f)
        
    def process(self, df_fp, n_sample=None):
        df = pd.read_csv(df_fp)
        
        df = self._drop_unnamed_col(df)
        df = self._sfo_only(df)
        df = self._remove_delay_nans(df)
        df = self._create_origin_ca_var(df)
        df = self._create_weekday_var(df)
        df = self._create_external_cause_var(df)
        df = self._lowercase_cols(df)
        
        if n_sample == None:
            return df
        elif n_sample > 0 and n_sample < df.shape[0]:
            return self._sample(df, n_sample)
        elif n_sample > df.shape[0]:
            return df
        else:
            raise ValueError('n_sample must be 0 < n <= {}.'.format(df.shape[0]))
    
    def join(self, df, weather_fp):
        weather_df = pd.read_csv(weather_fp)
        df = df.merge(weather_df, left_on='fl_date', right_on='date')
        df = df.rename(columns={'TMAX':'max_temp', 'TMIN':'min_temp', 
                          'TAVG':'avg_temp', 'PRCP':'precip', 
                          'AWND':'avg_wind_spd', 'WSF2':'wsf2', 'WT01':'fog', 'WT08':'haze'})
        df = df.drop(columns=['fl_date', 'date', 'origin_airport_id', 'dest_airport_id'])
        return df 
        
    def _drop_unnamed_col(self, df):
        return df.drop(columns=df.columns[df.columns.str.contains(':')])
    
    def _sfo_only(self, df):
        return df[df['DEST_AIRPORT_ID'] == SFO_id]

    def _remove_delay_nans(self, df):
        df = df[(df['CANCELLED'] != 1) & (df['DIVERTED'] != 1)]
        return df.drop(columns=['CANCELLED', 'DIVERTED'])
    
    def _create_origin_ca_var(self, df):
        df['origin_ca'] = np.where(df['ORIGIN_AIRPORT_ID'].astype(str).isin(self.ca_airports.keys()), 1, 0)
        return df
    
    def _create_weekday_var(self, df):
        df['is_weekday'] = np.where(df['DAY_OF_WEEK'] <  6, 1, 0)
        return df
    
    def _create_external_cause_var(self, df):
        df['external_cause'] = np.where(df['CARRIER_DELAY'].isna(), 0, 1)
        df = df.drop(columns=['CARRIER_DELAY'])
        return df

    def _lowercase_cols(self, df):
        return df.rename(columns=dict(zip(df.columns, df.columns.str.lower())))
    
    def _sample(self, df, n):
        return df.sample(n, random_state=RANDOM_SEED)