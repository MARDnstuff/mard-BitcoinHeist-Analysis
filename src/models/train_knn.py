from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.model_selection import train_test_split
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


def train_kNN(df: pd.DataFrame, config: dict) -> dict:
    try:
        # Loading data
        target = config["data"]["target_column"]
        processed_path = config["data"]["processed_path"]
        df = df.copy()
        X = df.drop(columns=[target])
        Y = df[target]
        
        
        scoring_m={
            "balanced_accuracy": "balanced_accuracy",
            "f1": "f1",
            "recall": "recall",
            "precision": "precision",
            "roc_auc": "roc_auc"
        }

        results = {
            "k": [],
            "balanced_accuracy": [],
            "f1": [],
            "recall": [],
            "precision": [],
            "roc_auc": []
        }

        for k in range(1, 38):
            logger.info(f"{k}-NN: Processing")
            clf = Pipeline(
                steps=[("scaler", StandardScaler()), ("knn", KNeighborsClassifier(n_neighbors=k ,weights="distance"))]
            )
            skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)

            scores = cross_validate(clf, X, Y, cv=skf, scoring=scoring_m, n_jobs=-1)
            logger.info(f"----> {k}-NN: Completed")

            results["k"].append(k)
            results["balanced_accuracy"].append(scores["test_balanced_accuracy"].mean())
            results["f1"].append(scores["test_f1"].mean())
            results["recall"].append(scores["test_recall"].mean())
            results["precision"].append(scores["test_precision"].mean())
            results["roc_auc"].append(scores["test_roc_auc"].mean())

        
        short_id = uuid.uuid4().hex[:8]
        with open(f"src/{processed_path}/scores_{short_id}_k1to37.json", "w") as f:
            json.dump(results, f, indent=4)

        logger.info("Scores have been saved")

        return results

    except Exception as e:  
        logger.error(e, exc_info=True)