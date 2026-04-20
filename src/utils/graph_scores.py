import matplotlib.pyplot as plt

def graph_score_kNN(scores: dict) -> None:
    plt.figure()
    plt.plot(scores["k"], scores["balanced_accuracy"], label="Balanced Accuracy")
    plt.plot(scores["k"], scores["f1"], label="F1 Score")
    plt.plot(scores["k"], scores["recall"], label="Recall")
    plt.plot(scores["k"], scores["precision"], label="Precision")
    plt.plot(scores["k"], scores["roc_auc"], label="Roc_auc")


    plt.xlabel("Número de vecinos (k)")
    plt.ylabel("Score")
    plt.title("Desempeño de KNN (Pipeline) vs k")

    plt.legend()
    plt.grid()

    plt.show()