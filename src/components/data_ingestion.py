import os
import sys
from src.exeception import customException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import dataTransformation
from src.components.data_transformation import dataTransformationConfig
from src.components.model_trainer import modelTrainer
from src.components.model_trainer import modelTrainerConfig


@dataclass
class dataIngestionConfig:
  train_data_path: str = os.path.join('artifacts', 'train.csv')
  test_data_path: str = os.path.join('artifacts','test.csv')
  raw_data_path: str = os.path.join('artifacts', 'data.csv')
  
class dataIngestion:
  def __init__(self):
    self.ingestion_config = dataIngestionConfig()
  
  
  def initiate_data_ingestion(self):
    logging.info("Entered the data ingestion method or component")
    
    try:
      df = pd.read_csv('notebook\data\stud.csv')
      logging.info('Read the dataset as dataframe')
      
      os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
      
      df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)
      
      logging.info("Train and test data initiated")
      
      train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
      
      train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
      test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
      
      logging.info("Ingestion of the data is completed")
      
      return (
        
        self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path
      )
      
      
    except Exception as e:
      raise customException(e, sys)
    
if __name__=="__main__":
  obj = dataIngestion()
  train_data, test_data=obj.initiate_data_ingestion()
  
  
  data_transformation = dataTransformation()
  
  train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
  
  modeltrainer = modelTrainer()
  print(modeltrainer.initiate_model_train(train_arr, test_arr))
  
  
  
  