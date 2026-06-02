import pandas as pd

def main():
    df = pd.read_csv("data/Titanic-Dataset.csv")

    print("Dataset: Titanic Dataset")
    print("Shape:", df.shape)
    print("\nColumns:")
    print(list(df.columns))

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nInfo:")
    df.info()

    print("\nStatistical Summary:")
    print(df.describe())

if __name__ == "__main__":
    main()
