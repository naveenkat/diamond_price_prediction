import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from logger import logging
from exception import CustomException

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("data ingestion method starts")


        try:
            df = pd.read_csv(r'C:\diamond_price_prediction\\notebooks\\data\\archive (16)\\diamonds.csv')
            logging.info("Dataset raed as pandas dataframe")
            print('*'*100)
            print("RAW")
            print(self.ingestion_config.raw_data_path)
            print("test")
            print(self.ingestion_config.test_data_path)
            print("train")
            print(self.ingestion_config.train_data_path)
            
            print('*'*100)


            print(os.path.dirname(self.ingestion_config.raw_data_path))
            print(os.path.join(self.ingestion_config.raw_data_path))
            print('*'*100)
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("raw data is created")

            train_set,test_set = train_test_split(df,test_size=0.30,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header = True)


            logging.info("data ingestion step is completed")

            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path

            )




        
        except Exception as e:
            print("Error while reading the file")
            logging.info("exception occured at data ingestion step")
            raise CustomException(e,sys)
        




    


