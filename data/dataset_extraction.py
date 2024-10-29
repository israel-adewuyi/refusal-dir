import os
import random
import warnings
import requests
import pandas as pd

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


def read_malicious_instruct_repo():
    url = 'https://raw.githubusercontent.com/Princeton-SysML/Jailbreak_LLM/refs/heads/main/data/MaliciousInstruct.txt'

    response = requests.get(url)

    return response.text


def read_harmbench_val():
    url = 'https://raw.githubusercontent.com/centerforaisafety/HarmBench/refs/heads/main/data/behavior_datasets/harmbench_behaviors_text_val.csv'

    val_df = pd.read_csv(url)

    return val_df
    # response = requests.get(url)

    # return response.text


def read_harmful_dataset_list():
    # Construct the path to the JSON file in the root directory
    dataset_file_path = os.path.join(current_dir, '..', 'datasets.json')
    
    dataset = load_config(dataset_file_path)

    harmful_datasets = dataset['dataset']['Harmful']

    return harmful_datasets

def select_train_harmful_prompts():
    list_of_harmful_dataset = read_harmful_dataset_list()

    LIST = []

    for harmful_dataset in list_of_harmful_dataset:
        data = load_dataset(harmful_dataset)['train']['prompt']
        LIST.extend(data)

    malicious_instruct_data = read_malicious_instruct_repo()
    malicious_instruct_data = malicious_instruct_data.split('\n')

    LIST.extend(malicious_instruct_data)

    selected_prompts = random.sample(LIST, 128)
    selected_prompts = [f"{prompt}\n" for prompt in selected_prompts]

    with open('train_harmful_prompts.txt', 'w') as file:
        file.writelines(selected_prompts)


def select_val_harmful_prompts():
    dataframe = read_harmbench_val()

    dataframe = dataframe[dataframe['FunctionalCategory'] == 'standard']

    val_set = dataframe.sample(n=32, random_state=42)

    selected_prompts = val_set['Behavior'].tolist()

    selected_prompts = [f"{prompt}\n" for prompt in selected_prompts]

    with open("val_harmful_prompts.txt", "w") as file:
        file.writelines(selected_prompts)
    

def main():
    # select_random_harmful_prompts()
    # print(read_malicious_instruct_repo())
    select_val_harmful_prompts()
    # data = read_harmbench_val()
    # print(data.head())




if __name__ == '__main__':
    main()