# Future Datasets

A list of datasets that seem promising but also might require further processing for future use.

## Data Analysis
| Name                           | Link                          |
|--------------------------------|-------------------------------|
| Quantification of energy and carbon costs for mining cryptocurrencies | [Nature Sustainability](https://www-nature-com.libproxy.berkeley.edu/articles/s41893-018-0152-7) |
| Water intensity benchmarks for sustainable retail stores | [Mendeley](https://data.mendeley.com/datasets/byxt34g25h/1) |
| Dataset from the US Peer-to-peer Lending Platform with Macroeconomic Variables | [Mendeley](https://data.mendeley.com/datasets/wb3ndt69gf/3) |

## Modeling
| Name                           | Link                          | Notes                                                          |
|--------------------------------|-------------------------------|----------------------------------------------------------------|
| Bandwidth Measurement for Conference Call Data Usage<sup>1</sup> | [Mendeley](https://data.mendeley.com/datasets/8sp4nxj8m3/1), [IEEEDataPort](https://ieee-dataport.org/documents/data-bandwidth-measurement-conference-call-data-usage) | Includes notebook with cleaning code and an example model. Unsure whose calls were collected (personal, school-wide, etc.) |
| Seoul Bike Sharing<sup>2</sup>  | [UCI](https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand), [Mendeley](https://data.mendeley.com/datasets/gtfh9z865f/1) | UCI: bike demand, predicting bike supply <br> Mendeley: trip duration; ~1GB (~10m instances, 26 attributes) |
| Wind and solar cost developments | [Mendeley](https://data.mendeley.com/datasets/82nfwvcgdz/1) | Includes code for processing and setting up a LR model. Possibly too technical? |
| Vehicle CO2 emissions          | [Kaggle](https://www.kaggle.com/debajyotipodder/co2-emission-by-vehicles) | Potentially need to convert to US customary units; sparse matrix with car make/model. |
| DataCo supply chain            | [Mendeley](https://data.mendeley.com/datasets/8gx2fvg2k6/5) | Requires translation to English - noticed countries/cities are in Spanish. <br> Pandas encoding: `iso-8859-1` |
| Electricity Price Forecasting  | [OpenML](https://www.openml.org/d/1168), [Kaggle](https://www.kaggle.com/salilchoubey/electrity-prices) | Discrepancy between forecasted and actual price, possible NaNs. |
| Metro Interstate Traffic Volume | [UCI](https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume)| See relevant papers for PPT using dataset on anomaly detection, non-linear models and using an autoencoder |
| Drivers of climate (in)action | [Paper](https://www.sciencedirect.com/science/article/pii/S1462901120303828), [Data](https://data.mendeley.com/datasets/989gp9rhtb/1)| Regression on survey data (vs. observed data), n=499. Seems sociology/policy focused. |
| Winter daily min. temp. and energy consumption in South Korea | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2352340920302961) | Need to match `id` with city, using Fig 1. Would create labels used in Fig 2+3. Concern: used quantile linear reg. rather than OLS. | 

<sup>1</sup>Concerns with data quality/provenance, but overall like this dataset.

<sup>2</sup>If this dataset doesn't clash too much with BayWheels, I think both demand and duration datasets would be great candidates. The trip duration dataset has a rich feature set with weather conditions, holiday, etc. There is also a [Kaggle dataset page](https://www.kaggle.com/saurabhshahane/seoul-bike-trip-duration-prediction).