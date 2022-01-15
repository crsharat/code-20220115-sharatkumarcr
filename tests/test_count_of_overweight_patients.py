from unittest import TestCase
from faker import Factory
from random import choice
from code.bmi_cal import count_total_number_of_overweighted_patients


class PatientRecords(Factory):

    def height_cm(self):
        return choice(range(40, 200))

    def weight_kg(self):
        return choice(range(30, 150))

    def gender(self):
        return choice(["MALE", "FEMALE"])

    def get_patient_record(self, total_records=1000):
        return [{"HeightCm": self.height_cm(),
                 "WeightKg": self.weight_kg(),
                 "Gender": self.gender()} for _ in range(total_records)]


class TestCountNumberOfOverWeighted(TestCase):

    def test_total_number_of_overweighted(self):
        patient = PatientRecords()
        records = patient.get_patient_record(1000000)
        count_total_number_of_overweighted_patients(records)
