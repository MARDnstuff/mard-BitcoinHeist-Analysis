from src.config.logging import setUpLogging
from src.utils.config_loader import load_config
from src.utils.graph_scores import graph_score_kNN
from src.data.extract import extract_data, show_data_summary
from src.data.transform import transform_data
from src.models.train_knn import train, train_kNN
import logging
import json


logger = logging.getLogger(__name__)

def main():
    setUpLogging()
    config = load_config()
    logger.info("Configuration has been loaded")

    # Extract data
    df = extract_data(config["data"]["raw_path"])
    logger.info(f"Datos originales: {df.shape}")

    # Transform data (remove unsufficiente samples)
    df = transform_data(df, config)

    # Información general
    show_data_summary(df, config)

    # Train and plot
    # train(df, config)
    # res = train_kNN(df, config)

    # with open("src/data/processed/scores_43c60e63_k1to37.json", "r") as f:
    #     res = json.load(f)
    # graph_score_kNN(res)

    

if __name__ == "__main__":
    main()