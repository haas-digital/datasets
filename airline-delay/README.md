# Airline flight delays dataset

The dataset describes on-time performance for flights arriving at San Francisco International Airport along with the corresponding weather information for that day between June 2020 and August 2021.

This repository contains the Python code and Jupyter notebooks created for processing and modeling the raw datasets from the Bureau of Transportation Statistics under the Department of Transportation.


## Metadata
| Tasks                      | Regression, Classification | Number of Instances  | <sup>100195</sup> |
|:---------------------------|:---------------------------|:---------------------|:--------|
| Attribute Characteristics  | Integer, Real, String      | Number of Attributes | 24      |
| Missing Values?            | Yes<sup>2</sup>            |           |   |

<sup>1</sup>The number of instances can be modified. 

<sup>2</sup>Missing values are contained to five columns.

Check the [Usage Guide](#usage) section for more details.

## Materials Overview
| File                  | Description  |
|-----------------------|--------------|
| `clean.py`            | Python script to process data from the BTS portal. |
| `weather.py`          | Python script to obtain data through the NOAA CDO API. Requires an API token. |
| `example.ipynb`       | Contains examples of how to use the scripts listed above. |
| `models.ipynb`      | Contains example models performing the associated tasks on the dataset. |
| `attribute_info.md`   | Contains descriptions of each attribute within the dataset. |
| `ca_airports.json`    | Contains California airport IDs. Required for `clean.py`. |

## Instructor Notes/Usage Guide<a href="#usage"></a>

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
- Origin
    - OriginAirportID
- Destination
    - DestAirportID
- Departure Performance
    - CRSDepTime
    - DepDelay
    - TaxiOut
- Arrival Performance
    - TaxiIn
    - CRSArrTime
    - ArrDelay
    - ArrDel15
- Cancellations and Diversions
    - Cancelled
    - Diverted
- Flight Summaries
    - Distance
- Cause of Delay
    - CarrierDleay

## Data Sources
Bureau of Transportation Statistics
- [Airline On-Time Performance Data](https://www.transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EFD&DB_URL=). Data Table: On-Time : Marketing Carrier On-Time Performance (Beginning January 2018)

NOAA - National Climatic Data Center 
- [Climate Data Online](https://www.ncdc.noaa.gov/cdo-web/webservices/)

