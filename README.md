# DatasetTranslator

This project translates a dataset from English (or any other Language) to Bhojpuri (or any other Language) using the deep_translator library and pandas. The input is a CSV file containing the dataset, and the output is a translated CSV file.

## Prerequisites

- Python 3.10
- pandas library
- deep_translator library
- multiprocessing library
- tqdm library

## Where it used

- Alpaca Data Cleaned Bhojpuri - https://huggingface.co/datasets/SatyamDev/alpaca_data_cleaned_bhojpuri
- I used this Repository to Convert the Alpaca-Cleaned Dataset English to Bhojpuri
- It Takes 3 minutes to convert 3X3000 Alpaca-Cleaned Dataset to Bhojpuri using 4 core CPU laptop on lighting.ai Studio

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

Change Language: According to Your Input and ouput language use the code given in list at last

```bash
# change 'en' to your dataset language code and 'bho' to output dataset language code
def translate_text(text, source_lang='en', target_lang='bho'):
    if pd.notnull(text):
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    return 'NaN'

```

## How Code Works

![System Work](https://raw.githubusercontent.com/SatyamDevv/DatasetTranslator/main/Images/CSV%20Translation%20Process.png)

## Issues and Considerations

1. Performance: The script may take a significant amount of time to process large datasets.

2. API Rate Limits: The GoogleTranslator API has a request limit. When translating large datasets, the script may exceed the 200k request limit, causing some translations to fail make sure to translate between 2500-3500 line of Alpaca-Cleaned Dataset.

## Supported Language

| Language              | Code     |
| --------------------- | -------- |
| Afrikaans             | af       |
| Albanian              | sq       |
| Amharic               | am       |
| Arabic                | ar       |
| Armenian              | hy       |
| Assamese              | as       |
| Aymara                | ay       |
| Azerbaijani           | az       |
| Bambara               | bm       |
| Basque                | eu       |
| Belarusian            | be       |
| Bengali               | bn       |
| Bhojpuri              | bho      |
| Bosnian               | bs       |
| Bulgarian             | bg       |
| Catalan               | ca       |
| Cebuano               | ceb      |
| Chichewa              | ny       |
| Chinese (Simplified)  | zh-CN    |
| Chinese (Traditional) | zh-TW    |
| Corsican              | co       |
| Croatian              | hr       |
| Czech                 | cs       |
| Danish                | da       |
| Dhivehi               | dv       |
| Dogri                 | doi      |
| Dutch                 | nl       |
| English               | en       |
| Esperanto             | eo       |
| Estonian              | et       |
| Ewe                   | ee       |
| Filipino              | tl       |
| Finnish               | fi       |
| French                | fr       |
| Frisian               | fy       |
| Galician              | gl       |
| Georgian              | ka       |
| German                | de       |
| Greek                 | el       |
| Guarani               | gn       |
| Gujarati              | gu       |
| Haitian Creole        | ht       |
| Hausa                 | ha       |
| Hawaiian              | haw      |
| Hebrew                | iw       |
| Hindi                 | hi       |
| Hmong                 | hmn      |
| Hungarian             | hu       |
| Icelandic             | is       |
| Igbo                  | ig       |
| Ilocano               | ilo      |
| Indonesian            | id       |
| Irish                 | ga       |
| Italian               | it       |
| Japanese              | ja       |
| Javanese              | jw       |
| Kannada               | kn       |
| Kazakh                | kk       |
| Khmer                 | km       |
| Kinyarwanda           | rw       |
| Konkani               | gom      |
| Korean                | ko       |
| Krio                  | kri      |
| Kurdish (Kurmanji)    | ku       |
| Kurdish (Sorani)      | ckb      |
| Kyrgyz                | ky       |
| Lao                   | lo       |
| Latin                 | la       |
| Latvian               | lv       |
| Lingala               | ln       |
| Lithuanian            | lt       |
| Luganda               | lg       |
| Luxembourgish         | lb       |
| Macedonian            | mk       |
| Maithili              | mai      |
| Malagasy              | mg       |
| Malay                 | ms       |
| Malayalam             | ml       |
| Maltese               | mt       |
| Maori                 | mi       |
| Marathi               | mr       |
| Meiteilon (Manipuri)  | mni-Mtei |
| Mizo                  | lus      |
| Mongolian             | mn       |
| Myanmar               | my       |
| Nepali                | ne       |
| Norwegian             | no       |
| Odia (Oriya)          | or       |
| Oromo                 | om       |
| Pashto                | ps       |
| Persian               | fa       |
| Polish                | pl       |
| Portuguese            | pt       |
| Punjabi               | pa       |
| Quechua               | qu       |
| Romanian              | ro       |
| Russian               | ru       |
| Samoan                | sm       |
| Sanskrit              | sa       |
| Scots Gaelic          | gd       |
| Sepedi                | nso      |
| Serbian               | sr       |
| Sesotho               | st       |
| Shona                 | sn       |
| Sindhi                | sd       |
| Sinhala               | si       |
| Slovak                | sk       |
| Slovenian             | sl       |
| Somali                | so       |
| Spanish               | es       |
| Sundanese             | su       |
| Swahili               | sw       |
| Swedish               | sv       |
| Tajik                 | tg       |
| Tamil                 | ta       |
| Tatar                 | tt       |
| Telugu                | te       |
| Thai                  | th       |
| Tigrinya              | ti       |
| Tsonga                | ts       |
| Turkish               | tr       |
| Turkmen               | tk       |
| Twi                   | ak       |
| Ukrainian             | uk       |
| Urdu                  | ur       |
| Uyghur                | ug       |
| Uzbek                 | uz       |
| Vietnamese            | vi       |
| Welsh                 | cy       |
| Xhosa                 | xh       |
| Yiddish               | yi       |
| Yoruba                | yo       |
| Zulu                  | zu       |
