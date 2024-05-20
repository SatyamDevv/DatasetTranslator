# DatasetTranslator
This project translates a dataset from English to Bhojpuri using the deep_translator library and pandas. The input is a CSV file containing the dataset, and the output is a translated CSV file.

# Prerequisites
1. Python 3.10
2. pandas library
3. deep_translator library
4. multiprocessing library
5. tqdm library

# Installation
Install the required libraries using pip:
'''
pip install pandas deep-translator tqdm
'''

# Usage
Setup Paths: Specify the input and output CSV file paths in the script.
'''
#Path to the input CSV file
input_path = r"your_csv_path_here.csv"
#Path to the output CSV file
output_path = r"your_csv_path_here.csv"

'''
# Issues and Considerations
1. Performance: The script may take a significant amount of time to process large datasets.

2. API Rate Limits: The GoogleTranslator API has a request limit. When translating large datasets, the script may exceed the 200k request limit, causing some translations to fail. This can be mitigated by:

