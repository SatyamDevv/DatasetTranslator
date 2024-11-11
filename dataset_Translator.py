import pandas as pd
from deep_translator import GoogleTranslator
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import os

# Input configuration
input_path = r"Alpaca English/alpaca_data_cleaned_13.csv"
output_path = r"Alpaca Hindi/alpaca_data_cleaned_Hindi_13.csv"
source_lang = 'en'  # Source language code (e.g., 'en' for English)
target_lang = 'hi'  # Target language code (e.g., 'hi' for Hindi)

# Read the input CSV file
data = pd.read_csv(input_path)

# Determine the optimal chunk size and number of threads
num_cores = os.cpu_count()*2
num_threads = num_cores  # Number of threads in the pool
print(f"Using {num_threads} threads")
chunk_size = len(data) // (10 * num_threads)  # Adjust chunk size based on the number of threads

# Split the data into chunks
data_chunks = [data.iloc[i:i + chunk_size].copy() for i in range(0, len(data), chunk_size)]

# Function to translate a single text using GoogleTranslator
def translate_text(text, src_lang=source_lang, tgt_lang=target_lang):
    if pd.notnull(text):
        return GoogleTranslator(source=src_lang, target=tgt_lang).translate(text)
    return 'NaN'

# Function to translate a chunk
def translate_chunk(chunk):
    try:
        # Get all columns from the chunk
        for column in chunk.columns:
            # Check if the column contains string data
            if chunk[column].dtype == object:
                chunk[column] = chunk[column].apply(lambda x: translate_text(x, source_lang, target_lang))
    except Exception as e:
        print(f"Translation error in column {column}: {e}")
    return chunk

# Main execution
if __name__ == "__main__":
    print(f"Translating from {source_lang} to {target_lang}")
    print(f"Input file: {input_path}")
    print(f"Output file: {output_path}")
    
    # Create a thread pool with the specified number of worker threads
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Use tqdm for progress bar, map each chunk to the translate_chunk function
        results = list(tqdm(executor.map(translate_chunk, data_chunks), total=len(data_chunks)))
    
    # Combine the translated chunks into a single DataFrame
    translated_data = pd.concat(results, ignore_index=True)
    
    # Write the translated data to a CSV file
    translated_data.to_csv(output_path, index=False)
    print("Translation completed successfully!")