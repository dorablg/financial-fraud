# Dataset card: IEEE-CIS Fraud Detection

| Field | Value |
| --- | --- |
| Source | Vesta Corporation via the IEEE-CIS Fraud Detection Kaggle competition (2019) |
| Copy used | Hugging Face `aliceczr/ieee-fraud-detection` (unofficial mirror) |
| Downloaded on | 2026-10-11 |
| Files used | `train_transaction.csv`, `train_identity.csv` |
| Licence / terms | Kaggle competition rules; data not redistributed |
| Label | `isFraud` (1 = fraud) |
| Rows | TODO |
| Fraud rate | TODO |
| Time span | TODO days (`TransactionDT` is seconds from a hidden reference) |

## Split boundaries (fixed before any model)

| Set | `TransactionDT` from | to | Rows | Fraud rate |
| --- | --- | --- | --- | --- |
| Train | TODO | TODO | TODO | TODO |
| Validation | TODO | TODO | TODO | TODO |
| Test | TODO | TODO | TODO | TODO |

## Known quirks

- Many columns are mostly missing; only some transactions have an identity row.
- Most columns are anonymised (C, D, M, V, id_*).
