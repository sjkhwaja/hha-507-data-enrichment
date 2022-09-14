import pandas as pd


### load data
sparcs = pd.read_csv('data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv')
neighborhood = pd.read_csv('data/adi-download/US_2019_ADI_Census Block Group_v3.1.csv', low_memory=False)

### show df in format
print(sparcs.head(5).to_markdown())
print(neighborhood.head(5).to_markdown())

### list column names
sparcs.columns
neighborhood.columns
## clean column names
sparcs.columns = sparcs.columns.str.replace('[^A-Za-z0-9]+', '_')
neighborhood.columns = neighborhood.columns.str.replace('[^A-Za-z0-9]+', '_')
sparcs.columns
neighborhood.columns

### create smaller datasets for merge
sparcs_small = sparcs[['Health_Service_Area', 'Hospital_County', 'Facility_Id', 'Zip_Code_3_digits']]
neighborhood_small = neighborhood[['ADI_NATRANK', 'ADI_STATERNK']]


### merge datasets
sparcs_combined = sparcs_small.merge(neighborhood_small, how='left', left_on='Health_Service_Area', right_on='ADI_NATRANK')

sparcs_combined.to_csv('data/sparcs_combined.csv')
