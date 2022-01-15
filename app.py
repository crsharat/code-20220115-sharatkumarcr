from copy import deepcopy as DC
import fire
import logging
from code.bmi_cal import get_bmi_of_all_patients, \
    count_total_number_of_overweighted_patients

LOGGER = logging.getLogger()


class BMICalculator:
    """
    A custom cli to calculate BMI for n number of patients
    """

    def __init__(self, patient_records: str):
        self.patient_records = patient_records

    def get_bmi(self):
        self.patient_records = DC(get_bmi_of_all_patients(self.patient_records))
        return self.patient_records

    def get_overweighted_patients(self):
        total_patients = count_total_number_of_overweighted_patients(self.patient_records)
        return total_patients


if __name__ == "__main__":
    fire.Fire(BMICalculator)
