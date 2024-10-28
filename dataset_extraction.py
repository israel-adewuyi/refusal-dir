import os
import warnings
from dotenv import load_dotenv
from datasets import load_dataset

warnings.filterwarnings('ignore')

load_dotenv()

hf_token =  os.getenv("HF_TOKEN")

def main():
    # adv_dataset = load_dataset("walledai/AdvBench")

    # print(adv_dataset.keys())
    # print(adv_dataset['train']['prompt'])

    tdc_dataset = load_dataset("walledai/TDC23-RedTeaming")

    print(tdc_dataset.keys())
    print(tdc_dataset['train']['prompt'])




if __name__ == '__main__':
    main()