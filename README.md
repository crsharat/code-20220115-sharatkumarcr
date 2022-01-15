# BMI Calculator
A custom cli to calculate BMI for n number of patients

### Prerequisites
____

1. Python package Fire https://github.com/google/python-fire
2. Python package Faker https://github.com/joke2k/faker (To run the test)

Note: Please use a virtual env and install the prerequisites listed above

### Basic Usage
____

#### NAME
    app.py

#### SYNOPSIS
    app.py --patient_records=PATIENT_RECORDS get_bmi

#### DESCRIPTION
    A custom cli to calculate BMI for n number of patients

#### ARGUMENTS
    PATIENT_RECORDS
        Type: str
        eg: "[{\"Gender\": \"Male\", \"HeightCm\": 171, \"WeightKg\": 96 }]"

#### COMMANDS
    available commands:

    * get_bmi
    * get_overweighted_patients

#### Examples

* Get BMI for respective patients

```python app.py --patient_records="[{\"Gender\": \"Male\", \"HeightCm\": 171, \"WeightKg\": 96 }, {\"Gender\": \"Male\", \"HeightCm\": 171, \"WeightKg\": 100 }]" get_bmi```

Output

    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96, "bmi": 32.83}
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 100, "bmi": 34.2}

* Count number of overweighted patients

```python app.py --patient_records="[{\"Gender\": \"Male\", \"HeightCm\": 171, \"WeightKg\": 96 }, {\"Gender\": \"Male\", \"HeightCm\": 175, \"WeightKg\": 85 }]" get_bmi```

Output

    1
