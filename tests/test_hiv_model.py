import unittest
import numpy as np
from src.hiv_model_student import HIVModel, load_hiv_data
#from solutions.hiv_model_solution import HIVModel, load_hiv_data

class TestHIVModel(unittest.TestCase):
    def test_model_initialization(self):
        model = HIVModel(A=1000, alpha=0.5, B=500, beta=0.1)
        self.assertIsNotNone(model)

    def test_viral_load_calculation(self):
        model = HIVModel(A=1000, alpha=0.5, B=500, beta=0.1)
        time = np.linspace(0, 10, 100)
        result = model.viral_load(time)
        self.assertEqual(len(result), 100)

    def test_data_loading(self):
        time, load = load_hiv_data('data/HIVseries.csv')
        self.assertGreater(len(time), 0)
        self.assertGreater(len(load), 0)

if __name__ == "__main__":
    unittest.main()