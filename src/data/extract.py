import pandas as pd
from scipy.io import arff
import logging

logger = logging.getLogger(__name__)

def extract_data(path: str) -> pd.DataFrame:
    """
    Extract data from raw data path
    """
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        logger.error(e, exc_info=True)

def extract_data_arff(path: str) -> pd.DataFrame:
    """
    Extract data from a raw data path with arff format
    """
    try:
        data, meta = arff.loadarff(path)
        
        return pd.DataFrame(data)
    except Exception as e:
        logger.error(e, exc_info=True)


def show_data_summary(df: pd.DataFrame, config: dict) -> None:
    """
    Show a brief summary of the loades dataset
    """
    logger.info("General overview")
    logger.info("\n -------- INFO --------")
    df.info()
    target = config["data"]["target_column"]
    logger.info(f"\n -------- Classes -------- \n{df[target].value_counts()}")
    logger.info(f"\n -------- Null values? --------\n{df.isnull().sum()}")