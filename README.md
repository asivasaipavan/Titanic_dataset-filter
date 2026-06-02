# Titanic_dataset-filter
    # Titanic Dataset Exploration

    This repository contains a basic exploratory data analysis of the Kaggle Titanic Dataset.

    ## Dataset
    - **Name:** Titanic Dataset
    - **Source:** Kaggle
    - **Objective:** Understand the structure of the data, identify columns and data types, check dataset size, and inspect missing values.

    ## Dataset Overview
    - **Rows:** 891
    - **Columns:** 12

    ## Columns
    - PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked

    ## Key Observations
    - The dataset contains both numerical and categorical columns.
    - Missing values are present mainly in `Age`, `Cabin`, and `Embarked`.
    - The target column is `Survived`.

    ## Files
    - `data/Titanic-Dataset.csv` — the dataset
    - `src/analyze_titanic.py` — Python script to explore the dataset

    ## How to Run
    1. Install Python 3 and pandas:
       ```bash
       pip install pandas
       ```
    2. Run the analysis script:
       ```bash
       python src/analyze_titanic.py
       ```

    ## Notes
    If you want to upload this directly to GitHub, keep the folder structure as-is.

    ## License
    For learning and educational use.
