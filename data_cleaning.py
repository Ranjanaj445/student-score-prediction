# ============================================================
# DATA CLEANING USING PYTHON
# ============================================================

import pandas as pd
import numpy as np

print("=" * 60)
print("DATA CLEANING PROGRAM")
print("=" * 60)


# ------------------------------------------------------------
# STEP 1: CREATE DATASET
# ------------------------------------------------------------

data = {
    "Name": [
        "Arun",
        "Priya",
        "Rahul",
        "Ranjana",
        "Divya",
        "Arun"
    ],

    "Age": [
        21,
        22,
        np.nan,
        23,
        21,
        21
    ],

    "Marks": [
        85,
        92,
        76,
        np.nan,
        95,
        85
    ],

    "City": [
        "Trichy",
        "Chennai",
        "Madurai",
        "Trichy",
        np.nan,
        "Trichy"
    ]
}

df = pd.DataFrame(data)


# ------------------------------------------------------------
# STEP 2: DISPLAY ORIGINAL DATASET
# ------------------------------------------------------------

print("\n1. ORIGINAL DATASET")
print("-" * 60)
print(df)


# ------------------------------------------------------------
# STEP 3: DATASET INFORMATION
# ------------------------------------------------------------

print("\n2. DATASET INFORMATION")
print("-" * 60)

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())


# ------------------------------------------------------------
# STEP 4: CHECK MISSING VALUES
# ------------------------------------------------------------

print("\n3. MISSING VALUES")
print("-" * 60)

missing_values = df.isnull().sum()

print(missing_values)


# ------------------------------------------------------------
# STEP 5: HANDLE MISSING VALUES
# ------------------------------------------------------------

print("\n4. HANDLING MISSING VALUES")
print("-" * 60)

# Fill Age missing value with mean
age_mean = df["Age"].mean()
df["Age"] = df["Age"].fillna(age_mean)

# Fill Marks missing value with mean
marks_mean = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(marks_mean)

# Fill City missing value with mode
city_mode = df["City"].mode()[0]
df["City"] = df["City"].fillna(city_mode)

print("Missing numerical values filled using MEAN.")
print("Missing categorical values filled using MODE.")

print("\nDataset after handling missing values:")
print(df)


# ------------------------------------------------------------
# STEP 6: CHECK MISSING VALUES AGAIN
# ------------------------------------------------------------

print("\n5. MISSING VALUES AFTER CLEANING")
print("-" * 60)

print(df.isnull().sum())


# ------------------------------------------------------------
# STEP 7: FIND DUPLICATES
# ------------------------------------------------------------

print("\n6. DUPLICATE RECORDS")
print("-" * 60)

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)

if duplicate_count > 0:
    print("\nDuplicate rows:")
    print(df[df.duplicated()])
else:
    print("No duplicate rows found.")


# ------------------------------------------------------------
# STEP 8: REMOVE DUPLICATES
# ------------------------------------------------------------

print("\n7. REMOVING DUPLICATES")
print("-" * 60)

df = df.drop_duplicates()

print("Duplicate rows removed successfully.")


# ------------------------------------------------------------
# STEP 9: FINAL CLEAN DATASET
# ------------------------------------------------------------

print("\n8. FINAL CLEAN DATASET")
print("-" * 60)

print(df)


# ------------------------------------------------------------
# STEP 10: STATISTICAL SUMMARY
# ------------------------------------------------------------

print("\n9. DATASET STATISTICS")
print("-" * 60)

print(df.describe())


# ------------------------------------------------------------
# STEP 11: MEAN
# ------------------------------------------------------------

print("\n10. MEAN")
print("-" * 60)

print("Age Mean   :", df["Age"].mean())
print("Marks Mean :", df["Marks"].mean())


# ------------------------------------------------------------
# STEP 12: MEDIAN
# ------------------------------------------------------------

print("\n11. MEDIAN")
print("-" * 60)

print("Age Median   :", df["Age"].median())
print("Marks Median :", df["Marks"].median())


# ------------------------------------------------------------
# STEP 13: MINIMUM
# ------------------------------------------------------------

print("\n12. MINIMUM VALUES")
print("-" * 60)

print("Minimum Age   :", df["Age"].min())
print("Minimum Marks :", df["Marks"].min())


# ------------------------------------------------------------
# STEP 14: MAXIMUM
# ------------------------------------------------------------

print("\n13. MAXIMUM VALUES")
print("-" * 60)

print("Maximum Age   :", df["Age"].max())
print("Maximum Marks :", df["Marks"].max())


# ------------------------------------------------------------
# STEP 15: FINAL VALIDATION
# ------------------------------------------------------------

print("\n14. FINAL VALIDATION")
print("-" * 60)

print("Total Rows       :", len(df))
print("Total Columns    :", len(df.columns))
print("Missing Values   :", df.isnull().sum().sum())
print("Duplicate Rows   :", df.duplicated().sum())


output_file = "cleaned_dataset.csv"

df.to_csv(output_file, index=False)

print("\n15. FILE SAVED")
print("-" * 60)

print("Cleaned dataset saved as:", output_file)


# ------------------------------------------------------------
# END
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED SUCCESSFULLY!")
print("=" * 60)