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


def get_sample_data(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    """
    Clean up data
    """
    try:
        TARGET_COLUMN = config["data"]["target_column"]
        SAMPLE_PERCENTAGE: float = 0.03
        RANDOM_SEED = 42
        logger.info(f"\nTomando muestra estratificada ({SAMPLE_PERCENTAGE*100:.2f}%)...")

        sampled_df = (
            df.groupby(TARGET_COLUMN, group_keys=False)
            .apply(
                lambda x: x.sample(
                    frac=SAMPLE_PERCENTAGE,
                    random_state=RANDOM_SEED
                )
            )
            .reset_index(drop=True)
        )

        output_path = f"src/{config['data']['processed_path']}/dataset_processed_sample.csv"
        sampled_df.to_csv(output_path, index=False)
        logger.info(f"CSV procesado guardado en: {output_path}")    

        logger.info(f"Sample: \n{df.head()}")

        return sampled_df

    except Exception as e:
        logger.error(e, exc_info=True)
        return {}