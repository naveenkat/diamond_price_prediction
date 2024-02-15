import numpy as np 
import pandas as pd
import os,sys
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from utils import save_object
from utils import evaluate_model
from logger import logging
from exception import CustomException
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")
class ModelTrainer:
    def __init__(self):
        self.model_train_config = ModelTrainerConfig()
    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info("splitting data in to independent and dependent variables")
            x_train,y_train,x_test,y_test = (train_array[:,:-1], 
                                              train_array[:,-1],
                                              test_array[:,:-1],
                                              test_array[:,-1]
                  
             )
            models = {"LinearRegression":LinearRegression(),
                      "Lasso":Lasso(),
                      "Ridge":Ridge(),
                      "ElasticNet":ElasticNet(),
                      "DecisionTree":DecisionTreeRegressor(),
                      "RandomForest":RandomForestRegressor()

            }
            model_report:dict = evaluate_model(x_train,y_train,x_test,y_test,models)
            print("\n==================================================================================")
            logging.info(f"model report  :  {model_report}")

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[ list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]
            
            print(f"best model found, model is : {best_model} and score is,r2_score : {best_model_score}")
            print("\n=======================================================")

            logging.info(f"best model found, model is : {best_model} and score is,r2_score : {best_model_score}") 

            save_object(
                file_path = self.model_train_config.trained_model_file_path,
                obj = best_model
            )

            







        except Exception as e:
           raise CustomException(e,sys)
