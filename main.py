from src.config.logging import setUpLogging
from src.utils.config_loader import load_config
from src.data.extract import extract_data
import logging


logger = logging.getLogger(__name__)

def main():
    setUpLogging()
    config = load_config()
    logger.info("Configuration has been loaded")

    # Extract data
    df = extract_data(config["data"]["raw_path"])
    logger.info(f"Datos originales: {df.shape}")


if __name__ == "__main__":
    main()