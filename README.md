# Student Marks Analyzer

A Python data-analysis project that reads student marks from a CSV file, validates the data, calculates averages and grades, ranks students, and exports reports using pandas.

## Features

- **CSV data loading:** Reads student records from `students.csv`.
- **Data validation:** Identifies missing marks, non-numeric values, and marks outside the valid range of 0–100.
- **Average calculation:** Calculates each valid student's average across Python, Maths, and Database subjects.
- **Grade assignment:** Assigns grades based on configurable average-score boundaries.
- **Student ranking:** Sorts valid students from highest to lowest average.
- **Rejected-record reporting:** Separates records that need correction.
- **CSV report export:** Saves rankings and rejected records to separate CSV files.

## Tech Stack

- Python 3
- pandas
- Python's built-in CSV functionality

## Project Structure

```text
student-marks-analyzer/
├── students.csv
├── main.py
├── pandas_analysis.py
├── student_rankings.csv
├── rejected_students.csv
├── requirements.txt
└── README.md
```

The exported reports are generated when the analysis script runs. They do not need to exist before the first run.

## Installation

1. Install Python 3.
2. Clone this repository or download the project.
3. Open a terminal in the project directory.
4. Create and activate a virtual environment.

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

5. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

If `requirements.txt` has not been created yet, install pandas directly:

```bash
python -m pip install pandas
```

## Input Data

The `students.csv` file must contain these columns:

```csv
name,python,maths,database
Arun,85,90,78
Priya,92,88,95
Ravi,67,72,70
```

Marks must be numeric values between 0 and 100. Records with missing, non-numeric, or out-of-range marks should be reported for correction rather than included in the rankings.

## Usage

Run the pandas analysis script from the project directory:

The script loads the input data, validates marks, calculates averages and grades for valid records, sorts students by average, and displays the ranking.


## Grade Boundaries

| Average | Grade |
|---|---|
| 90 and above | A |
| 80 to below 90 | B |
| 70 to below 80 | C |
| 60 to below 70 | D |
| Below 60 | F |

These are the example grading rules used in this project and can be changed in the code.

## Concepts Practiced

- Python functions and conditional statements
- Lists, dictionaries, and loops
- CSV file handling
- Data type conversion and validation
- pandas DataFrames
- Missing-value detection
- Filtering, sorting, and aggregation
- CSV report generation

## Limitations

- The current analysis expects the subject columns `python`, `maths`, and `database`.
- The grading boundaries are illustrative and may not match an institution's official rules.
- Input validation and error handling should be tested against malformed files and unexpected column names.
- The program is a local command-line application; it does not currently provide a web interface or database.

## Future Improvements

- Add automated unit tests.
- Support configurable subjects and grading rules.
- Improve error messages for malformed CSV files.
- Generate visualizations of subject performance.
- Add a command-line interface for selecting input and output files.

## Author

Developed as a programming and data-analysis learning project.
