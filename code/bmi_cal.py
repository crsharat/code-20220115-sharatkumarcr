import sys
from json import loads
from code.constants import BMI_CATALALOG


def calculate_bmi(patient_weight: int, patient_height: int):
    """
    Cacluate the BMI based on the weight and height of a patient
    param patient_weight: Patients weight in Kg eg: 120
    param patient_height: Patient's heighy in cm eg: 172
    return type: float
    """
    return round(float(patient_weight / ((patient_height / 100) ** 2)), 2)


def is_overweight(bmi: float):
    """
    Check whether bmi value is in overweight category or not
    param bmi: BMI value eg: 24.49
    return type: boolean
    """
    return True if bmi > BMI_CATALALOG['OVER']['start_range'] \
        and bmi <= BMI_CATALALOG['OVER']['end_range'] else False


def count_total_number_of_overweighted_patients(json_records: list):
	"""
	Count the total number of overweighted patients using json records
	param json_record: records should be in following format
	{"WeightKg": <int>, "HeightCm": <int>}
	return type: int
	"""
	return len(list(filter(lambda patient_record: is_overweight(patient_record['bmi']) == True, 
						   get_bmi_of_all_patients(json_records))))


def get_bmi_of_all_patients(json_records: list):
	"""
	Will update the each patient record with respective bmi value
	param json_record: records should be in following format
	{"WeightKg": <int>, "HeightCm": <int>}
	return type: list
	eg: {"WeightKg": <int>, "HeightCm": <int>, "bmi": <float>}
	"""
	return list(map(lambda patient_record: {**patient_record,
											"bmi": calculate_bmi(patient_record['WeightKg'], 
														         patient_record['HeightCm'])},
					json_records))
