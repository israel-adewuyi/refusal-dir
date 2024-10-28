import os
import warnings

from dotenv import load_dotenv
from datasets import load_dataset
from data_config import load_config

# ignore warnings
warnings.filterwarnings('ignore')
# load env variables
load_dotenv()
# hf token
hf_token =  os.getenv("HF_TOKEN")
# get directory of current script
current_dir = os.path.dirname(os.path.abspath(__file__))

def read_harmful_dataset_list():
    # Construct the path to the JSON file in the root directory
    dataset_file_path = os.path.join(current_dir, '..', 'datasets.json')

    dataset = load_config(dataset_file_path)

    harmful_datasets = dataset['dataset']['Harmful']

    return harmful_datasets

def main():
    list_of_harmful_dataset = read_harmful_dataset_list()




if __name__ == '__main__':
    main()