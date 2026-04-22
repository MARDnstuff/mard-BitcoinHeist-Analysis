from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier, plot_tree
from sklearn.ensemble import HistGradientBoostingClassifier
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

def save_preview_tree(clf, X, Y, config) -> None:
        
        processed_path = config["data"]["processed_path"]
        clf.fit(X, Y)
        fig, ax = plt.subplots(figsize=(20, 8))
        plot_tree(
            clf.named_steps["DT"],
            feature_names=X.columns.tolist(),
            class_names=[str(c) for c in Y.unique()],
            filled=True,
            rounded=True,
            fontsize=10,
            ax=ax
        )
        plt.tight_layout()
        plt.savefig(f"src/{processed_path}/decision_tree_DT.png", dpi=150, bbox_inches="tight")
        plt.show()
        logger.info("Tree image saved")

def train_DT(df: pd.DataFrame, config: dict) -> None:
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
        
        # ----- DecisionTreeClassifier
        clf_1 = Pipeline(
            steps=[("scaler", StandardScaler()), ("DT", DecisionTreeClassifier())]
        )

        # ----- HistGradientBoostingClassifier
        clf_2 = Pipeline(
            steps=[("scaler", StandardScaler()), ("HGBC", HistGradientBoostingClassifier())]
        )

        # ----- ExtraTreeClassifier
        clf_3 = Pipeline(
            steps=[("scaler", StandardScaler()), ("ETC", ExtraTreeClassifier())]
        )
        logger.info("Pipelines have been created")


        # Training and Validation
        # Definir validación cruzada estratificada
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
        logger.info("Stratified completed")

        # Ejecutar evaluación
        scoring_m=["balanced_accuracy", "f1", "recall", "precision", "roc_auc"]

        pipelines = {
            "DT": clf_1,
            "HGBC": clf_2,
            "ETC": clf_3
        }

        for id, pipe in pipelines.items():
            res = cross_validate(pipe, X, Y, cv=skf, scoring=scoring_m)
            logger.info("Cross Validation completed: " + id)

            short_id = uuid.uuid4().hex[:8]
            scores_serializable = {
                key: value.tolist() for key, value in res.items()
            }

            with open(f"src/{processed_path}/trees_scores_{short_id}_{id}.json", "w") as f:
                json.dump(scores_serializable, f, indent=4)

            logger.info("Scores have been saved")

            # save_preview_tree(clf_1, X, Y, config)

    except Exception as e:  
        logger.error(e, exc_info=True)
