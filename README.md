# Financial Fraud Intelligence (`financial-fraud`)

Building a financial analysis fraud detection model.

A fraud-risk scoring system for card-not-present transactions, evaluated honestly and explained, with a test of whether transaction-network information helps.

## Research question

> Can transaction-network information improve fraud detection beyond conventional tabular machine learning, particularly when the fraud class is rare and the model must generalize to later transactions?

## Data

IEEE-CIS Fraud Detection (Vesta, 2019). Only the two train files are used (`train_transaction.csv`, `train_identity.csv`), joined on `TransactionID`. Raw data is not stored in this repository.

Download into `data/raw/`:

```
pip install -U huggingface_hub
hf download aliceczr/ieee-fraud-detection --repo-type dataset --include "train_*" --local-dir data/raw
```

The files come from an unofficial Hugging Face copy of the Kaggle competition data; the original competition rules apply. See `reports/dataset_card.md`.

## Evaluation

- Chronological split by `TransactionDT` (train, validation, test); boundaries fixed before any model.
- Headline metric: PR-AUC. Operational metrics: recall at a fixed alert rate and precision at top K.
- Accuracy is never the headline metric.

## Structure

```
data/raw/        raw CSVs (git-ignored)
data/interim/    cleaned, downcast data (git-ignored)
notebooks/       exploration notebooks
src/             reusable code (loading, features, models)
reports/         dataset card, results, figures
tests/           tests for splits, leakage checks and the API
```

## Setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/load.py
```

## Status

Week 1: data understanding and setup.
