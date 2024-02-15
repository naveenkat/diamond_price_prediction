import os
import sys
import pandas as pd
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation
from components.model_trainer import ModelTrainer




if __name__ == '__main__':
    obj = DataIngestion()
    print("IT Started")
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)
    data_transformation = DataTransformation()
    train_arr,test_arr,obj_path = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_arr,test_arr)
    
    
