# 📘 Assignment: Intro to Machine Learning — Supervised Models

## 🎯 Objective

Students will build a complete supervised machine learning pipeline: load a dataset, preprocess features, train a classifier with scikit-learn, evaluate model performance, and write a short summary of results.

## 📝 Tasks

### 🛠️	Prepare the data

#### Description
Load the provided CSV dataset and apply simple preprocessing steps (handle missing values, separate features and target, and perform a train/test split).

#### Requirements
Completed program should:

- Load the dataset from `sample_dataset.csv` in the assignment folder.
- Return feature matrix `X` and target vector `y` from a `load_data(path)` function.
- Handle missing values by dropping rows with missing entries.
- Split the data into train and test sets (use an 80/20 split).

### 🛠️	Train a classifier

#### Description
Implement a `train_model(X_train, y_train)` function that fits a scikit-learn classifier and returns the trained model.

#### Requirements
Completed program should:

- Use scikit-learn's `LogisticRegression` (or another classifier) with a fixed `random_state` for reproducibility.
- Return a fitted model object with a `predict` method.

### 🛠️	Evaluate and report

#### Description
Evaluate the trained model on the test set and compute common metrics. Write a short (2–4 sentences) summary of the results in `RESULTS.md` or the README.

#### Requirements
Completed program should:

- Implement an `evaluate(model, X_test, y_test)` function that returns a dictionary with `accuracy`, `precision`, and `recall`.
- Print or save the evaluation metrics.
- Include a brief explanation of the results and possible next steps for improvement.

---

## Setup & Running

Install dependencies (recommended in a virtual environment):

```
pip install -r requirements.txt
```

Run the example pipeline:

```
python starter-code.py
```

## Autograding notes

The included tests (in `tests/`) will import and call `load_data`, `train_model`, and `evaluate`. Keep function signatures intact for automatic grading.
