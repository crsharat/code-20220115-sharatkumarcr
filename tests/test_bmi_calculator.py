from unittest import TestCase
from code.bmi_cal import calculate_bmi, is_overweight, \
    count_total_number_of_overweighted_patients, get_bmi_of_all_patients


class TestBMICalculator(TestCase):

    def test_bmi_for_any_patient(self):
        patient_height = 175
        patient_weight = 75
        expected_bmi = 24.49
        test_result = calculate_bmi(patient_weight, patient_height)
        self.assertEqual(expected_bmi, test_result)
    
    def test_bmi_is_overweight(self):
        patient_height = 175
        patient_weight = 85
        expected_bmi = 24.49
        test_result = calculate_bmi(patient_weight, patient_height)
        bmi_type = is_overweight(test_result)
        self.assertTrue(bmi_type)
    
    def test_count_number_of_overweighted_patients(self):
        patient_records = [
            {"HeightCm": 175, "WeightKg": 85}
        ]
        test_result = count_total_number_of_overweighted_patients(patient_records)
        self.assertEqual(1, test_result)
    
    def test_get_bmi_of_patients(self):
        patient_records = [
            {"HeightCm": 175, "WeightKg": 85}
        ]
        expected_results = [
            {"HeightCm": 175, "WeightKg": 85, "bmi": 27.76}
        ]
        test_result = get_bmi_of_all_patients(patient_records)
        self.assertEqual(expected_results, test_result)