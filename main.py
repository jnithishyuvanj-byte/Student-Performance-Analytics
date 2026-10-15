import pandas as pd
import numpy as np

SUBJECTS = ["Python", "Maths", "Physics", "English", "Data_Structures"]


def get_grade(avg):
    """Grading rule: 90+ A+, 80+ A, 70+ B, 60+ C, 50+ D, 40+ E, else F."""
    for mark, grade in [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D"), (40, "E")]:
        if avg >= mark:
            return grade
    return "F"


def get_result(row):
    """Pass only if every subject is 40 or more."""
    return "Pass" if (row[SUBJECTS] >= 40).all() else "Fail"


def process(df):
    """Add Total, Average, Grade and Result columns."""
    marks = df[SUBJECTS].to_numpy()
    df["Total"] = np.sum(marks, axis=1)
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    df["Grade"] = [get_grade(a) for a in df["Average"]]
    df["Result"] = df.apply(get_result, axis=1)
    return df


df = pd.read_csv("students.csv")
print(df)
print("\nRecords:", len(df), "| Columns:", list(df.columns))
df.info()

df = process(df)
print("\n--- RESULTS ---")
print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]])

print("\nPassed:", (df["Result"] == "Pass").sum(), "| Failed:", (df["Result"] == "Fail").sum())
print("Class Highest:", df.loc[df["Average"].idxmax(), "Name"], df["Average"].max())
print("Class Lowest :", df.loc[df["Average"].idxmin(), "Name"], df["Average"].min())
print("Class average:", round(np.mean(df["Average"]), 2))

print("\n--- SUBJECT-WISE AVERAGE ---")
for subject in SUBJECTS:
    print(subject, ":", round(np.mean(df[subject]), 2))
print("Best subject:", df[SUBJECTS].mean().idxmax())

print("\n--- TOP 5 STUDENTS ---")
print(df.nlargest(5, "Average")[["Student_ID", "Name", "Average", "Grade"]])