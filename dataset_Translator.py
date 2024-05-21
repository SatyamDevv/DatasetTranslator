import pandas as pd
from deep_translator import GoogleTranslator
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import os

# Path to the input CSV file
input_path = r"Alpaca English/alpaca_data_cleaned_15.csv"
# Path to the output CSV file
output_path = r"Alpaca Bhojpuri/alpaca_data_cleaned_bhojpuri_15.csv"

# Read the input CSV file
data = pd.read_csv(input_path)

# Determine the optimal chunk size and number of threads
# These values can be adjusted based on your machine's capabilities and the dataset size
num_cores = os.cpu_count()*2
num_threads = num_cores  # Number of threads in the pool
print(num_threads)
chunk_size = len(data) // (10 * num_threads)  # Adjust chunk size based on the number of threads

# Split the data into chunks
data_chunks = [data.iloc[i:i + chunk_size].copy() for i in range(0, len(data), chunk_size)]

# Function to translate a single text using GoogleTranslator
def translate_text(text, source_lang='en', target_lang='bho'):
    if pd.notnull(text):
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    return 'NaN'

# Function to translate a chunk
def translate_chunk(chunk):
    try:
        chunk['output'] = chunk['output'].apply(translate_text)
        chunk['input'] = chunk['input'].apply(translate_text)
        chunk['instruction'] = chunk['instruction'].apply(translate_text)
    except Exception as e:
        print(f"Translation error: {e}")
    return chunk

# Main execution
if __name__ == "__main__":
    # Create a thread pool with the specified number of worker threads
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Use tqdm for progress bar, map each chunk to the translate_chunk function
        results = list(tqdm(executor.map(translate_chunk, data_chunks), total=len(data_chunks)))

    # Combine the translated chunks into a single DataFrame
    translated_data = pd.concat(results, ignore_index=True)
    # Write the translated data to a CSV file
    translated_data.to_csv(output_path, index=False)
    print("Done!")
