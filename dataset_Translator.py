import pandas as pd
from deep_translator import GoogleTranslator
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
import os
import time
import random

# Path to the input CSV file
input_path = r"your_csv_inputpath_here.csv"
# Path to the output CSV file
output_path = r"your_csv_outputpath_here.csv.csv"

# Read the input CSV file
data = pd.read_csv(input_path)

# Determine the optimal chunk size and number of processes
num_cores = cpu_count()  # Number of processes in the pool
chunk_size = max(1, len(data) // (5 * num_cores))  # Increase chunk size to reduce number of chunks
batch_size = 200  # Increase batch size to translate more rows at once

# Split the data into chunks
data_chunks = [data.iloc[i:i + chunk_size].copy() for i in range(0, len(data), chunk_size)]

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Function to translate a batch of texts using GoogleTranslator
def translate_batch(texts):
    translator = GoogleTranslator(source='en', target='bho')
    try:
        translated_texts = translator.translate_batch(texts)
        return translated_texts
    except Exception as e:
        print(f"Error translating batch: {e}")
        # Implement exponential backoff
        for attempt in range(5):
            try:
                time.sleep((2 ** attempt) + random.uniform(0, 1))
                translated_texts = translator.translate_batch(texts)
                return translated_texts
            except Exception as e:
                print(f"Retry {attempt + 1} failed: {e}")
        return texts  # Return the original texts if translation fails

# Function to translate a chunk
def translate_chunk(chunk):
    try:
        for column in ['output', 'input', 'instruction']:
            non_null_texts = chunk[column].dropna().tolist()
            for i in range(0, len(non_null_texts), batch_size):
                batch = non_null_texts[i:i + batch_size]
                translated_batch = translate_batch(batch)
                chunk.loc[chunk[column].isin(batch), column] = translated_batch
    except Exception as e:
        print(f"Translation error in chunk: {e}")
    return chunk

# Main execution
if __name__ == "__main__":
    # Create a process pool with the specified number of worker processes
    with Pool(processes=num_cores) as pool:
        # Use tqdm for progress bar, map each chunk to the translate_chunk function
        results = list(tqdm(pool.imap(translate_chunk, data_chunks), total=len(data_chunks)))

    # Combine the translated chunks into a single DataFrame
    translated_data = pd.concat(results, ignore_index=True)
    # Write the translated data to a CSV file
    translated_data.to_csv(output_path, index=False)
    print("Done!")
