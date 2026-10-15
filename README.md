# Student Performance Analytics System – Project Documentation

## 1. Project Title

**Student Performance Analytics System**: a Python, NumPy and Pandas program that turns raw student marks into totals, averages, grades and pass/fail results.

[Field]       [Details]
Student name  Nithish J 
Programme     B.Tech CSE (AI & ML)
Institution   Hindustan Institute of Technology & Science, Chennai
Course        EWB Courses, Python with AI 

## 2. Objective

The project replaces manual mark calculation with a script that processes a whole class in one run.

Calculating totals, averages, grades and pass/fail status by hand is slow and easy to get wrong, especially across several subjects and many students. This system automates that work and also answers class-level questions: who topped the class, which subject is strongest, and how many students passed. It was built to practise loading data, vectorised NumPy calculations and Pandas analysis on a realistic dataset.

## 3. Technologies Used

The project uses only Python and two libraries.

[Tool]    [Purpose in this project] 
Python 3  Core language: functions, loops, conditions 
NumPy     Row-wise total and mean of the marks array, rounding, class average 
Pandas    Reading the CSV, DataFrame columns, filtering, `nlargest`, `idxmax`, `idxmin` 
CSV file  Storage for the student records (`students.csv`) 

## 4. Dataset Description

The dataset is `students.csv`: 20 student records across 9 columns, with no missing values. Students come from five departments (CSE, IT, ECE, EEE and CIVIL).

[Column]           [Type]    [Meaning] 
Student_ID         Text      Unique ID, F101 to F120 
Name               Text      Student name 
Department         Text      CSE, IT, ECE, EEE or CIVIL 
Python             Integer   Marks out of 100 
Maths              Integer   Marks out of 100 
Physics            Integer   Marks out of 100 
English            Integer   Marks out of 100 
Data_Structures    Integer   Marks out of 100 
Attendance         Integer   Attendance percentage 

The five subject columns are the inputs for every calculation. Attendance is stored in the file but is not used in the grading logic.

## 5. Implementation

The program lives in one file, `main.py`, and runs in six steps.

1. **Import libraries and define subjects.** Pandas and NumPy are imported, and a `SUBJECTS` list holds the five subject columns so every calculation uses the same names.
2. **Load the data.** `pd.read_csv("students.csv")` creates the DataFrame. The program prints the table, the record count and column names, and calls `df.info()` to confirm data types and that no values are missing.
3. **Process the marks** in the `process(df)` function. The five subject columns are converted to a NumPy array with `to_numpy()`. `np.sum(marks, axis=1)` gives each student's Total, and `np.round(np.mean(marks, axis=1), 2)` gives the Average to two decimals.
4. **Assign the grade** with `get_grade(avg)`. It checks the average against the cut-offs in order and returns the first grade that fits.
5. **Assign the result** with `get_result(row)`. A student passes only if every subject mark is 40 or more, so one weak subject means Fail even when the average is high. Applying it with `df.apply(get_result, axis=1)` adds the Result column.
6. **Analyse the class.** Pandas and NumPy calculate the pass and fail counts, highest and lowest average (`idxmax`, `idxmin`), class average, subject-wise averages, the best subject, and the top 5 students (`nlargest`).

Grading rule used in `get_grade`:

[Average]      [Grade]
90 and above      A+
80 to 89.99       A 
70 to 79.99       B 
60 to 69.99       C 
50 to 59.99       D 
40 to 49.99       E 
Below 40          F  

## 6. Key Features

- `get_grade(avg)`: converts an average into a grade from A+ to F.
- `get_result(row)`: marks Pass only when all five subjects are 40 or above.
- `process(df)`: adds the Total, Average, Grade and Result columns in one call.
- Vectorised NumPy calculations of total and average for all students at once.
- Class statistics: pass and fail counts, highest and lowest scorer, and class average.
- Subject-wise averages and the best-performing subject.
- Top 5 students ranked by average.
- Data inspection at the start (record count, columns, data types) to confirm the file loaded correctly.
## 8. Final Outcome

The system processes all 20 students in one run and reports 18 passes and 2 failures, a class average of 71.76, and Lakshana Devi as the top scorer with 94.8.

The project met its goals: it loads a CSV file, adds Total, Average, Grade and Result columns with NumPy and Pandas, and produces class-level insights without any manual calculation. Elango Pandian and Jeeva Anand failed because at least one subject mark fell below 40 (Maths 39 for Elango; Python 37 and Data_Structures 36 for Jeeva). English is the strongest subject, with a class average of 76.5.

## 9. Challenges & Learning

**Challenges and how they were solved**

- **Pass/fail logic.** A student with a high average can still fail one subject. I solved this by checking every subject with `(row[SUBJECTS] >= 40).all()` instead of using the average alone.
- **Assigning grades cleanly.** A long chain of `if` and `elif` statements was repetitive. A list of (cut-off, grade) pairs checked in order made `get_grade` short and easy to change.
- **Repeating column names.** Typing subject names in many places invited typos, so a single `SUBJECTS` list is reused everywhere.
- **Applying a function to every row.** Pandas `apply` with `axis=1` let `get_result` run on each student, while NumPy handled the totals and averages.

**What I learned**

- Loading and inspecting data with `read_csv` and `info()` before using it.
- NumPy axis operations: `axis=1` works across subjects for each student.
- Using Pandas tools such as `idxmax`, `idxmin` and `nlargest` to answer questions quickly.
- Writing small functions with one job each, which keeps the program readable and easy to test.

## 10. GitHub Repository

Repository link: ____________________________________________

(Paste the final GitHub repository URL here before submitting.)

## How to Run

1. Install the requirements:

   ```
   pip install numpy pandas
   ```

2. Keep `main.py` and `students.csv` in the same folder.

3. Run the program:

   ```
   python main.py
   ```
