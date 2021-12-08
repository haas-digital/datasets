# Airline flight delays dataset

The dataset describes on-time performance for flights arriving at San Francisco International Airport along with the corresponding weather information for that day between June 2020 and August 2021.

This repository contains the Python code and Jupyter notebooks created for processing and modeling the raw datasets from the Bureau of Transportation Statistics under the Department of Transportation.

## Contents
- [Metadata](#metadata)
- [Materials Overview](#files)
- [Usage Guide](#usage)
    - [Raw Data](#rd)
    - [Number of Instances](#instances)
    - [Using `weather.py`](#weather)
    - [Classroom Usage](#class)
- [Miscellaneous](#misc)
    - [Concatenation](#concatenation)
    - [Selecting Columns](#selection)
- [Data Sources](#sources)

## Metadata <a href="#metadata"></a>
| Tasks                      | Regression, Classification | Number of Instances  | 100195<sup>1</sup> |
|:---------------------------|:---------------------------|:---------------------|:--------|
| Attribute Characteristics  | Integer, Real, String      | Number of Attributes | 24      |
| Missing Values?            | N/A            |           |   |

<sup>1</sup>The number of instances can be modified. Check the [Usage Guide](#usage) section for more details.

## Materials Overview<a href="#files"></a>
| File                  | Description  |
|-----------------------|--------------|
| `clean.py`            | Python script to process data from the BTS portal. |
| `weather.py`          | Python script to obtain data through the NOAA CDO API. Requires an API token. |
| `example.ipynb`       | Contains examples of how to use the scripts listed above. |
| `models.ipynb`        | Contains example models performing the associated tasks on the dataset. |
| `attribute_info.md`   | Contains descriptions of each attribute within the dataset. |
| `ca_airports.json`    | Contains California airport IDs. Required for `clean.py`. |

## Instructor Notes/Usage Guide<a href="#usage"></a>

#### Raw data<a href="#rd"></a>
If you'd like to avoid downloading each month's data individually from the BTS website, you can download a [zip archive](https://drive.google.com/file/d/1dhAY4_fpHktShMtGORWdy8MOwniL7MyK/view?usp=sharing) of the raw data between June 2020 and August 2021. 

Otherwise, if you're downloading from the BTS database, a list of the attributes selected from the data portal is below under the [Selecting Columns](#selection) section. There are a few tips when obtaining the flight data this way:
- In the `Filter Geography` drop down menu, select California. Because the dataset only contains flights arriving into SFO, choosing to only download CA flight data will reduce the memory load when processing the monthly flight data.
- After download the zip, rename the csv file in the zip to `YYYYMM.csv`. See [Concatenation](#concatenation) for more details on renaming the csvs.

#### Number of instances<a href="#instances"></a>
By default, the dataset uses all available flights for each month. If you'd like to reduce the size of the dataset, there is a parameter `n_sample` when using `Airline.process()`, but there are two cases in which no sampling occurs:
    - (Default) when `n_sample` is `None`
    - `n_sample` is greater than the number of flights present (in that particular month after processing)
Otherwise, a sample of size `n_sample` will be returned when the dataset is processed. 

#### Using `weather.py`<a href="#weather"></a>
In order to use the `NOAAApi` class provided in `weather.py`, you must have a Climate Data Online web services token. You may request one [here](https://www.ncdc.noaa.gov/cdo-web/token). Refer to the section "Getting Weather Data" in `example.ipynb` on more information about obtaining and storing data from the API. 

#### Classroom usage<a href="#class"></a>


## Miscellaneous<a href="#misc"></a>

#### Concatenation<a href="#concatenation"></a>
For ease of naming and use when concatenating the tables for each month, it is recommended to re-name each month's flight data csv file to `YYYYMM.csv`. There is code provided in `example.ipynb` that performs the concatenation for all months (for one single dataset) which takes advantage of the weather csv filenames which are saved as `YYYY-MM.csv`. 

#### Selecting Columns from BTS TranStats<a href="#selection"></a>
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
    
## Data Sources<a href="#sources"></a>
Bureau of Transportation Statistics
- [Airline On-Time Performance Data](https://www.transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EFD&DB_URL=). Data Table: On-Time : Marketing Carrier On-Time Performance (Beginning January 2018)

NOAA - National Climatic Data Center 
- [Climate Data Online](https://www.ncdc.noaa.gov/cdo-web/webservices/)

