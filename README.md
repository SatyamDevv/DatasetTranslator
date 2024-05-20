# DatasetTranslator
This project translates a dataset from English to Bhojpuri using the deep_translator library and pandas. The input is a CSV file containing the dataset, and the output is a translated CSV file.

## Prerequisites
- Python 3.10
- pandas library
- deep_translator library
- multiprocessing library
- tqdm library

## Installation
Install the required libraries using pip

```bash

pip install pandas 
pip install deep-translator 
pip install tqdm

```

## Usage
Setup Paths: Specify the input and output CSV file paths in the script.

```bash

#Path to the input CSV file
input_path = r"your_csv_path_here.csv"
#Path to the output CSV file
output_path = r"your_csv_path_here.csv"

```

## How Code Works

![System Work](https://raw.githubusercontent.com/SatyamDevv/DatasetTranslator/main/Images/diagram.png)

## Issues and Considerations
1. Performance: The script may take a significant amount of time to process large datasets.

2. API Rate Limits: The GoogleTranslator API has a request limit. When translating large datasets, the script may exceed the 200k request limit, causing some translations to fail. This can be mitigated by:

