from src.logger import logging
from src.exception import CustomException
import sys
from src.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_gcloud("hate-speech-tweets", "dataset.zip", "data/dataset.zip")


# logging.info("===============")
# try:
#     a=1/0
# except Exception as e:
#     raise CustomException(e,sys)


