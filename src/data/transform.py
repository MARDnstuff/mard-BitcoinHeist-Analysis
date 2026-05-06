import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

def transform_data(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    """
    Clean up data
    """
    try:
        # Se agrega la columna target, siendo White: 0 vs Ransomeware: 1
        target = config["data"]["target_column"]
        df[target] = (df["label"] != "white").astype(int)
        df = df.drop(columns=["address", "label"])
        df = df.drop_duplicates()
        df = df.dropna(subset=[target])

        output_path = f"src/{config['data']['processed_path']}/dataset_processed.csv"
        df.to_csv(output_path, index=False)
        logger.info(f"CSV procesado guardado en: {output_path}")    

        logger.info(f"Sample: \n{df.head()}")

        return df

    except Exception as e:
        logger.error(e, exc_info=True)
        return {}