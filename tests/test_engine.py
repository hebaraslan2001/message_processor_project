import unittest
from engine.processing_engine import ProcessingEngine

class TestProcessingEngine(unittest.TestCase):
    def test_arithmetic_processing(self):
        message = {"value": 100}
        engine = ProcessingEngine("ATTR + 50 * (ATTR / 10)")
        result = engine.process_message(message)
        self.assertEqual(result, 600.0)

    def test_regex_processing(self):
        message = {"value": "dog123"}
        engine = ProcessingEngine("Regex(ATTR, '^dog')")
        result = engine.process_message(message)
        self.assertTrue(result)

    def test_invalid_regex_processing(self):
        message = {"value": "cat456"}
        engine = ProcessingEngine("Regex(ATTR, '^dog')")
        result = engine.process_message(message)
        self.assertFalse(result)
        
###############################################
## tests for various mathematical operations ##
###############################################

    def test_addition(self):
        """Test simple addition"""
        message = {"value": 10}
        equation = "ATTR + 5"  # 10 + 5
        engine = ProcessingEngine(equation)
        processed_value = engine.process_message(message)
        self.assertEqual(processed_value, 15)

    def test_subtraction(self):
        """Test simple subtraction"""
        message = {"value": 10}
        equation = "ATTR - 5"  # 10 - 5
        engine = ProcessingEngine(equation)
        processed_value = engine.process_message(message)
        self.assertEqual(processed_value, 5)

    def test_multiplication(self):
        """Test simple multiplication"""
        message = {"value": 10}
        equation = "ATTR * 5"  # 10 * 5
        engine = ProcessingEngine(equation)
        processed_value = engine.process_message(message)
        self.assertEqual(processed_value, 50)

    def test_division(self):
        """Test simple division"""
        message = {"value": 10}
        equation = "ATTR / 5"  # 10 / 5
        engine = ProcessingEngine(equation)
        processed_value = engine.process_message(message)
        self.assertEqual(processed_value, 2)

    def test_combined_expression(self):
        """Test a complex arithmetic expression with addition, multiplication, and parentheses"""
        message = {"value": 10}
        equation = "ATTR + 5 * (ATTR / 2)"  # 10 + 5 * (10 / 2)
        engine = ProcessingEngine(equation)
        processed_value = engine.process_message(message)
        self.assertEqual(processed_value, 35)  # (10 / 2) = 5, 5 * 5 = 25, 10 + 25 = 35

    def test_parentheses(self):
        """Test parentheses to alter the order of operations"""
        message = {"value": 10}
        equation = "(ATTR + 5) * 2"  # (10 + 5) * 2
        engine = ProcessingEngine(equation)
        processed_value = engine.process_message(message)
        self.assertEqual(processed_value, 30)  # (10 + 5) = 15, 15 * 2 = 30

    def test_complex_expression(self):
        """Test a more complex expression"""
        message = {"value": 10}
        equation = "ATTR + 5 * (ATTR / 2) - 3"  # 10 + 5 * (10 / 2) - 3
        engine = ProcessingEngine(equation)
        processed_value = engine.process_message(message)
        self.assertEqual(processed_value, 32)  # (10 / 2) = 5, 5 * 5 = 25, 10 + 25 = 35, 35 - 3 = 32

    def test_division_by_zero(self):
        """Test division by zero (should handle error)"""
        message = {"value": 10}
        equation = "ATTR / 0"  # Should raise an error due to division by zero
        engine = ProcessingEngine(equation)
        with self.assertRaises(ZeroDivisionError):
            engine.process_message(message)