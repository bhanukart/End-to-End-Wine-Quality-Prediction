from WineQuality import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from WineQuality.entity.config_entity import DataTransformationConfig
import os

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config=config

    def remove_cols(self):
        data = pd.read_csv(self.config.data_path)
        data.drop(columns =['Id'],inplace=True)
        self.data=data
        

    def train_test_splitting(self):
        train,test = train_test_split(self.data)

        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)

        logger.info("Splitted data into training and testing data")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)