import requests 
import pandas as pd
import time
import copy

NOAA_BASE_URL = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'

# Max temperature; min temp; precipitation; average wind speed; fastest 2-min wind speed
data_types = ['TMAX', 'TMIN', 'TAVG', 'PRCP', 'AWND', 'WSF2']

# Fog; smog/haze 
incomplete_data_types = ['WT01', 'WT08']

# Params:
# - daily summary stats
# - for SFO
# - standard (imperial) units
# - 31 results
base_params = {
    'datasetid': 'GHCND',
    'stationid':'GHCND:USW00023234',
    'units':'standard',
    'limit': 31
}

class NOAAApi:
    
    def __init__(self, token, save_dir='./'):
        self.auth_header = {'token': token}
        self.path = save_dir
        
    def get_data(self, start='2021-01-01', end='2021-01-31'):
        if pd.Period(start).year > pd.Period(end).year:
            raise ValueError('Years must be in chronological order.')
            
        elif pd.Period(start).year <= pd.Period(end).year:
            for date in pd.period_range(start=start, end=end, freq="m"):
                self._get_month(date)
            print('Weather data successfully saved in {}.'.format(self.path))
    
    def _get_month(self, start):
        format_start = start.strftime('%Y-%m-01')
        format_end = start.strftime('%Y-%m-{}'.format(start.days_in_month))
        fn = self.path + start.strftime('%Y-%m') + '.csv'

        params = copy.deepcopy(base_params)
        params['startdate'] = format_start
        params['enddate'] = format_end
        
        params['datatypeid'] = data_types[0]
        
        r = requests.get(NOAA_BASE_URL, params=params, headers=self.auth_header)
        # Error check if returned response is valid (200)
        df = pd.DataFrame(r.json()['results'])
        # Add the rest of the variables in data_types to df
        for col in data_types[1:]:
            params['datatypeid'] = col
            r = requests.get(NOAA_BASE_URL, params=params, headers=self.auth_header)
            df[col] = [i['value'] for i in r.json()['results']]
            time.sleep(0.3)
            
        # get "incomplete" types
        new_date_range = pd.date_range(start=format_start, end=format_end, freq="D")
        for t in incomplete_data_types:
            params['datatypeid'] = t
            r = requests.get(NOAA_BASE_URL, params=params, headers=self.auth_header)
            res = r.json()['results']
            s = pd.Series([i['value'] for i in res], pd.to_datetime([i['date'] for i in res]))
            filled = s.asfreq('d', fill_value=0)
            
            filled = filled.reindex(new_date_range, fill_value=0)
            df[t] = filled.values
            time.sleep(0.2)
        
        df['date'] = df['date'].str.extract(r'([-\d]*)T')
        
        df.rename(columns={'value':'TMAX'}).drop(columns=['datatype', 'station', 'attributes']).to_csv(fn, index=False)
        
        print('Weather for {month} written to {file}.'.format(month=start.strftime('%B'), file=fn))