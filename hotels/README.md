# Hotel booking demand datasets
----

The datasets detail 120,000 anonymized bookings across two different hotels in Portugal between July 2015 and August 2017; H1 is a resort hotel and H2 is a city hotel. 

## Metadata
| Tasks                      | Classification          | Number of Instances  | 39768, 78410<sup>1</sup> |
|:---------------------------|:------------------------|:---------------------|:-----|
| Attribute Characteristics  | Integer, Real, String   | Number of Attributes | 31<sup>2</sup>   |
| Missing Values?            | N/A                     |                      |      |

<sup>1</sup>For H1, H2 respectively. Refer to the [Usage Guide](#usage) for more details.

<sup>2</sup>H2 has an additional attribute - see `attribute_info.md` for more details.

## Materials Overview
| File                      | Description  |
|---------------------------|--------------|
| `processing.ipynb`        | Notebook that contains all processing steps. |
| `models.ipynb`            | Contains example models performing the associated tasks on the dataset. |
| `attribute_info.md`       | Contains descriptions of each attribute within the dataset. |
| `h1_s.csv`, `h2_s.csv`    | Processed csvs for both hotels, H1 and H2. |

## Instructor Notes/Usage Guide<a href="#usage"></a>
#### Number of Instances
No sampling is performed on the data for either hotel, though it is optional if the number of instances is too high. `processing.ipynb` provides code to take a sample from either datasets.

#### Models
For each hotel, two classifiers are provided in `models.ipynb`: decision tree and random forest. Feel free to modify the parameters, however the `ccp_alpha` value (in the decision trees) is chosen so that the resulting decision tree is interpretable.

The models by default use all of the available attributes in the dataset. The models and the attributes used are there to serve as an example of how they can be used in a potential notebook, but you may choose to reduce the number of attributes if there are too many.

## Data Sources
Authors: Nuno Antonio, Ana de Almeida, Luis Nunes. ([DOI](https://doi.org/10.1016/j.dib.2018.11.126))
