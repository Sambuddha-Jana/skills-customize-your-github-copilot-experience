import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score


def load_data(path):
    df = pd.read_csv(path)
    df = df.dropna()
    X = df.drop('target', axis=1).values
    y = df['target'].values
    return X, y


def train_model(X_train, y_train):
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train, y_train)
    return model


def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)
    return {
        'accuracy': float(accuracy_score(y_test, preds)),
        'precision': float(precision_score(y_test, preds, zero_division=0)),
        'recall': float(recall_score(y_test, preds, zero_division=0)),
    }


if __name__ == '__main__':
    X, y = load_data('sample_dataset.csv')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    metrics = evaluate(model, X_test, y_test)
    print('Evaluation:', metrics)
