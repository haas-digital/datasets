# Attribute Description Table

Notes:
- CRS stands for Computer Reservation System

| Variable  | Type | Description        |
|:----------|:-----|:------------------------------|
| year      | Integer | Year       |
| month     | Integer | Month | 
| day_of_week | Integer | Day of week flight occurred | 
| fl_date   | String | Date of flight (YYYY-MM-DD) | 
| mkt_unique_carrier | String | Unique carrier code | 
| origin_airport_id | Integer | Origin airport ID (assigned by US DOT) | 
| dest_airport_id | Integer | Destination airport ID (assigned by US DOT) | 
| crs_dep_time | Integer | CRS departure time (local time: hhmm) | 
| dep_time  | Integer | Actual departure time (local time: hhmm) | 
| dep_delay | Integer | Departure delay (minutes) - negative if departure is early | 
| del_del15 | Integer | Indicator if flight departure is delayed (1 yes, 0 no) |  
| taxi_out  | Integer | Taxi out time (minutes) | 
| taxi_in   | Integer | Taxi out time (minutes) | 
| crs_arr_time | Integer | CRS arrival time (local time: hhmm) | 
| arr_time  | Integer | Actual arrival time (local time: hhmm) | 
| arr_delay | Integer | Arrival delay (minutes) - negative if early | 
| arr_del15 | Integer | Indicator if arrival is delayed | 
| crs_elapsed_time | Integer | CRS flight duration (minutes) | 
| actual_elapsed_time | Integer | Actual time of flight (minutes) | 
| distance  | Integer | Distance between airports (miles) | 
| carrier_delay | Integer | Carrier delay (minutes) | 
| weather_delay | Integer | Weather delay (minutes)
| nas_delay | Integer | National Airspace System delay (minutes) | 
| security_delay | Integer | Security delay (minutes) | 
| late_aircraft_delay | Integer | Late aircraft delay (minutes) | 
| origin_ca | Integer | Indicator if origin state is California | 
| is_weekday| Integer | Indicator if flight occurred on a weekday or not | 
| external_cause | Integer | Indicator if there was a recorded external cause for delay (based on carrier, weather, etc. from above) | 
| TMAX   | Integer | Maximum recorded temperature (Fahrenheit) |
| TMIN   | Integer | Minimum recorded temperature (Fahrenheit) |
| TAVG   | Integer | Average temperature (Fahrenheit) |
| PRCP   | Real | Precipitation (inches) |
| AWND   | Real | Average wind speed (miles per hour) |
| WSF2   | Real | Fastest 2-min wind speed  (miles per hour) |
| WT01   | Integer | Indicator if there was fog |
| WT08   | Integer | Indicator if there was smog or haze |