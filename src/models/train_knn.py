from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import get_scorer_names
import matplotlib.pyplot as plt
import pandas as pd
import uuid
import json
import logging

logger = logging.getLogger(__name__)


def train(df: pd.DataFrame, config: dict) -> None:
    try:
        # Loading data
        target = config["data"]["target_column"]
        processed_path = config["data"]["processed_path"]
        df = df.copy()
        X = df.drop(columns=[target])
        Y = df[target]
        
        # StandarScaler: convierte las variables para que esten en la misma escala 
        # para que el modelo no se sesgue por magnitudes grandes

        # Pipeline:  allows you to sequentially apply a list of transformers to preprocess the data and, 
        # if desired, conclude the sequence with a final predictor for predictive modeling.
        
        # ----- KNeighborsClassifier, k = 11
        clf_1 = Pipeline(
            steps=[("scaler", StandardScaler()), ("knn", KNeighborsClassifier(n_neighbors=11, weights="distance"))]
        )

        # ----- KNeighborsClassifier, k = 13
        clf_2 = Pipeline(
            steps=[("scaler", StandardScaler()), ("knn", KNeighborsClassifier(n_neighbors=13, weights="distance"))]
        )

        # ----- KNeighborsClassifier, k  = 37
        clf_3 = Pipeline(
            steps=[("scaler", StandardScaler()), ("knn", KNeighborsClassifier(n_neighbors=37, weights="uniform"))]
        )
        logger.info("Pipelines have been created")


        # Training and Validation
        # Definir validación cruzada estratificada
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
        logger.info("Stratified completed")

        # Ejecutar evaluación
        scoring_m=["balanced_accuracy", "f1", "recall", "precision", "roc_auc"]

        pipelines = [
            clf_3,
        ]

        results = []
        for pipe in pipelines:
            results.append(cross_validate(pipe, X, Y, cv=skf, scoring=scoring_m))
        logger.info("Cross Validation completed")

        for r in results:
            short_id = uuid.uuid4().hex[:8]
            scores_serializable = {
                key: value.tolist() for key, value in r.items()
            }

            with open(f"src/{processed_path}/scores_{short_id}.json", "w") as f:
                json.dump(scores_serializable, f, indent=4)

        logger.info("Scores have been saved")

    except Exception as e:  
        logger.error(e, exc_info=True)