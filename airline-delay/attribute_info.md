# Attribute Description Table

Notes:
- CRS stands for Computer Reservation System

| Variable  | Type | Description        |
|:----------|:-----|:------------------------------|
| year      | Integer | Year       |
| month     | Categorical | Month | 
| day_of_week | Integer | Day of week flight occurred | 
| crs_dep_time | Integer | CRS departure time (local time: hhmm) | 
| dep_delay | Integer | Departure delay (minutes) - negative if departure is early |  
| taxi_out  | Integer | Taxi out time (minutes) | 
| taxi_in   | Integer | Taxi out time (minutes) | 
| crs_arr_time | Integer | CRS arrival time (local time: hhmm) | 
| arr_delay | Integer | Arrival delay (minutes) - negative if early | 
| arr_del15 | Categorical | Indicator if arrival is delayed | 
| crs_elapsed_time | Integer | CRS flight duration (minutes) | 
| distance  | Integer | Distance between airports (miles) | 
| origin_ca | Categorical | Indicator if origin state is California | 
| is_weekday| Categorical | Indicator if flight occurred on a weekday or not | 
| external_cause | Categorical | Indicator if there was a recorded external cause for delay (based on carrier, weather, etc. from above) | 
| max_temp  | Integer | Maximum recorded temperature (Fahrenheit) |
| min_temp  | Integer | Minimum recorded temperature (Fahrenheit) |
| avg_temp  | Integer | Average temperature (Fahrenheit) |
| precip    | Real | Precipitation (inches) |
| avg_wind_spd | Real | Average wind speed (miles per hour) |
| wsf2      | Real | Fastest 2-min wind speed  (miles per hour) |
| fog       | Categorical | Indicator if there was fog |
| haze      | Categorical | Indicator if there was smog or haze |