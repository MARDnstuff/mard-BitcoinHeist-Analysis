import pandas as pd
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