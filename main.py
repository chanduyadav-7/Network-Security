import os
import sys

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging


from Network_Security.entity.config_entity import TrainingPipelineConfig
from Network_Security.entity.config_entity import DataIngestionConfig


from Network_Security.components.data_ingestion import DataIngestion




if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)


    except Exception as e:
        raise NetworkSecurityException(e,sys)