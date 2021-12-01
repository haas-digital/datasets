# Airline flight delays dataset

The dataset describes on-time performance for flights arriving at San Francisco International Airport along with the corresponding weather information for that day between June 2020 and August 2021.

This repository contains the Python code and Jupyter notebooks created for processing and modeling the raw datasets from the Bureau of Transportation Statistics under the Department of Transportation.


## Metadata
| Tasks                      | Regression, Classification | Number of Instances  | 11250<sup>1</sup> |
|:---------------------------|:---------------------------|:---------------------|:--------|
| Attribute Characteristics  | Integer, Real, String      | Number of Attributes | 37      |
| Missing Values?            | Yes<sup>2</sup>            |           |   |

<sup>1</sup>The number of instances is not static and can be modified. 
<sup>2</sup>Missing values are contained to five columns.
See [Miscellaneous](#misc) for more details.

## Materials Overview
| File                  | Description  |
|-----------------------|--------------|
| `clean.py`            | Python script to process data from the BTS portal. |
| `weather.py`          | Python script to obtain data through the NOAA CDO API. Requires an API token. |
| `example.ipynb`       | Contains examples of how to use the scripts listed above. |
| `modeling.ipynb`      | Contains example models performing the associated tasks on the dataset. |
| `attribute_info.md`   | Contains descriptions of each attribute within the dataset. |
| `ca_airports.json`    | Contains California airport IDs. Required for `clean.py`. |

## Instructor Notes/Usage Guide
- 

## Data Sources
Bureau of Transportation Statistics
- [Airline On-Time Performance Data](https://www.transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EFD&DB_URL=). Data Table: On-Time : Marketing Carrier On-Time Performance (Beginning January 2018)

NOAA - National Climatic Data Center 
- [Climate Data Online](https://www.ncdc.noaa.gov/cdo-web/webservices/)

## Miscellaneous 
#### Number of Instances

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
    - DepDel15
    - TaxiOut
- Arrival Performance
    - TaxiIn
    - CRSArrTime
    - ArrTime
    - ArrDelay
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