# Airline flight delays dataset

This repository contains Python code and Jupyter notebooks created for processing and modeling flight delays at San Francisco International Airport.

## Metadata
| Tasks                      | Regression, Classification | Instances       |   |
|----------------------------|----------------------------|-----------------|---|
| Attribute Characteristics  | Integer, Real, String      | Number of Attributes |   |
| Missing Values?            | Yes (See Miscellaneous)    |           |   |

## Materials Overview
| File                  | Description  |
|-----------------------|--------------|
| `clean.py`            | Python script to process data from the BTS portal. |
| `weather.py`          | Python script to obtain data through the NOAA CDO API. Requires an API token. |
| `example.ipynb`       | Contains examples of how to use the scripts listed above. |
| `modeling.ipynb`      | Contains example models performing the associated tasks on the dataset. |
| `attribute_info.md`   | Contains descriptions of each attribute within the dataset. |
| `ca_airports.json`    | Contains California airport IDs. Required for `clean.py`.

## Instructor Notes/Usage Guide
- 

## Data Sources
Bureau of Transportation Statistics
- [Airline On-Time Performance Data](https://www.transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EFD&DB_URL=). Data Table: On-Time : Marketing Carrier On-Time Performance (Beginning January 2018)

NOAA - National Climatic Data Center 
- [Climate Data Online](https://www.ncdc.noaa.gov/cdo-web/webservices/)

## Miscellaneous 
#### Missing values in dataset

#### Obtaining a NOAA CDO API Token

#### Columns selected from BTS:
- Summaries
    - Year
- Time Period
    - Month
    - DayOfMonth
    - DayOfWeek
    - FlightDate
- Airline
    - Marketing_Airline_Network
- Origin
    - OriginAirportID
- Destination
    - DestAirportID
- Departure Performance
    - CRSDepTime
    - DepTime
    - DepDelay
    - DepDelayMinutes
    - DepDel15
    - TaxiOut
- Arrival Performance
    - TaxiIn
    - CRSArrTime
    - ArrTime
    - ArrDelay
    - ArrDelayMinutes
    - ArrDel15
- Cancellations and Diversions
    - Cancelled
    - Diverted
- Flight Summaries
    - CRSElapsedTime
    - ActualElapsedTime
    - Distance
- Cause of Delay
    - CarrierDleay
    - WeatherDelay
    - NASDelay
    - SecurityDelay
    - LateAircraftDelay