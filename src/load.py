"""Load the IEEE-CIS train files, join them, shrink memory and save a parquet copy."""
from pathlib import Path

import pandas as pd

RAW = Path("data/raw")
INTERIM = Path("data/interim")


def memory_mb(df: pd.DataFrame) -> float:
    return df.memory_usage(deep=True).sum() / 1024**2


def downcast(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes("float64"):
        df[col] = df[col].astype("float32")
    for col in df.select_dtypes("int64"):
        df[col] = pd.to_numeric(df[col], downcast="integer")
    for col in df.select_dtypes("object"):
        df[col] = df[col].astype("category")
    return df


def load_train() -> pd.DataFrame:
    tx = pd.read_csv(RAW / "train_transaction.csv")
    ident = pd.read_csv(RAW / "train_identity.csv")
    return tx.merge(ident, on="TransactionID", how="left")


def main() -> None:
    df = load_train()
    before = memory_mb(df)
    df = downcast(df)
    after = memory_mb(df)

    print(f"rows: {len(df):,}  columns: {df.shape[1]}")
    print(f"fraud rate: {df['isFraud'].mean():.4f}")
    print(f"time span: {df['TransactionDT'].max() / 86400:.0f} days")
    print(f"memory: {before:,.0f} MB -> {after:,.0f} MB")

    INTERIM.mkdir(parents=True, exist_ok=True)
    df.to_parquet(INTERIM / "train.parquet")
    print(f"saved {INTERIM / 'train.parquet'}")


if __name__ == "__main__":
    main()
