# Airline flight delays dataset

Data Source: 
Bureau of Transportation Statistics
[Airline On-Time Performance Data](https://www.transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EFD&DB_URL=)
Data Table: On-Time : Marketing Carrier On-Time Performance (Beginning January 2018)

Columns selected from BTS:
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