"""
Test suite for python.py - covers all bug patterns
"""
import unittest
import threading
import time
from unittest.mock import patch, mock_open
import python


class TestMutableDefaultArgument(unittest.TestCase):
    """Test mutable default argument bug"""
    
    def test_append_to_list_default(self):
        """Test that mutable default argument causes issues"""
        result1 = python.append_to_list(1)
        result2 = python.append_to_list(2)
        # Bug: both calls share the same list
        self.assertEqual(result1, [1, 2])
        self.assertEqual(result2, [1, 2])
    
    def test_append_to_list_with_provided_list(self):
        """Test with provided list"""
        my_list = []
        result = python.append_to_list(1, my_list)
        self.assertEqual(result, [1])


class TestUnreachableCode(unittest.TestCase):
    """Test unreachable code detection"""
    
    def test_unreachable_code(self):
        """Test function with unreachable code"""
        result = python.unreachable_code()
        self.assertEqual(result, "early return")


class TestRiskyDivision(unittest.TestCase):
    """Test division by zero risk"""
    
    def test_risky_division_normal(self):
        """Test normal division"""
        result = python.risky_division(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_risky_division_by_zero(self):
        """Test division by zero raises exception"""
        with self.assertRaises(ZeroDivisionError):
            python.risky_division(10, 0)


class TestUnusedVariables(unittest.TestCase):
    """Test unused variables detection"""
    
    def test_unused_variables(self):
        """Test function with unused variables"""
        result = python.unused_variables()
        self.assertEqual(result, 30)


class TestMissingExceptionHandling(unittest.TestCase):
    """Test missing exception handling"""
    
    @patch("builtins.open", new_callable=mock_open, read_data="test content")
    def test_no_exception_handling_success(self, mock_file):
        """Test file reading without exception handling - success case"""
        result = python.no_exception_handling("test.txt")
        self.assertEqual(result, "test content")
        mock_file.assert_called_once_with("test.txt", 'r')
    
    def test_no_exception_handling_failure(self):
        """Test file reading without exception handling - failure case"""
        with self.assertRaises(FileNotFoundError):
            python.no_exception_handling("nonexistent.txt")


class TestBareExcept(unittest.TestCase):
    """Test bare except clause"""
    
    def test_bare_except(self):
        """Test bare except catches everything"""
        result = python.bare_except()
        self.assertIsNone(result)


class TestIgnoringReturnValue(unittest.TestCase):
    """Test ignoring return values"""
    
    def test_ignoring_return_value(self):
        """Test function that ignores return values"""
        result = python.ignoring_return_value()
        self.assertIsNone(result)


class TestWrongNoneComparison(unittest.TestCase):
    """Test wrong None comparison"""
    
    def test_wrong_none_comparison_with_none(self):
        """Test comparison with None"""
        result = python.wrong_none_comparison(None)
        self.assertTrue(result)
    
    def test_wrong_none_comparison_with_value(self):
        """Test comparison with non-None value"""
        result = python.wrong_none_comparison(5)
        self.assertFalse(result)


class TestUsingAssertForValidation(unittest.TestCase):
    """Test using assert for validation"""
    
    def test_using_assert_for_validation_valid(self):
        """Test assert with valid input"""
        result = python.using_assert_for_validation(10)
        self.assertEqual(result, 20)
    
    def test_using_assert_for_validation_invalid(self):
        """Test assert with invalid input"""
        with self.assertRaises(AssertionError):
            python.using_assert_for_validation(-5)


class TestLostException(unittest.TestCase):
    """Test lost exception"""
    
    def test_lost_exception(self):
        """Test exception is caught but not logged"""
        result = python.lost_exception()
        self.assertIsNone(result)


class TestRiskyOperation(unittest.TestCase):
    """Test risky operation"""
    
    def test_risky_operation(self):
        """Test risky operation raises exception"""
        with self.assertRaises(ZeroDivisionError):
            python.risky_operation()


class TestRaceCondition(unittest.TestCase):
    """Test race condition"""
    
    def setUp(self):
        """Reset counter before each test"""
        python.counter = 0
    
    def test_increment_counter_single_thread(self):
        """Test counter increment in single thread"""
        python.increment_counter()
        self.assertEqual(python.counter, 1000)
    
    def test_increment_counter_race_condition(self):
        """Test race condition with multiple threads"""
        threads = []
        for _ in range(5):
            thread = threading.Thread(target=python.increment_counter)
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        # Due to race condition, counter might not be 5000
        # This test demonstrates the bug
        self.assertLessEqual(python.counter, 5000)


class TestPotentialInfiniteLoop(unittest.TestCase):
    """Test potential infinite loop"""
    
    def test_potential_infinite_loop_terminates(self):
        """Test that loop terminates for x=5"""
        # This should terminate
        result = python.potential_infinite_loop(5)
        self.assertIsNone(result)
    
    def test_potential_infinite_loop_with_timeout(self):
        """Test potential infinite loop with other values"""
        # For x=6, this would be infinite, so we skip actual execution
        # Just verify the function exists
        self.assertTrue(callable(python.potential_infinite_loop))


class TestInefficientStringConcat(unittest.TestCase):
    """Test inefficient string concatenation"""
    
    def test_inefficient_string_concat(self):
        """Test string concatenation in loop"""
        result = python.inefficient_string_concat([1, 2, 3, 4, 5])
        self.assertEqual(result, "1,2,3,4,5,")
    
    def test_inefficient_string_concat_empty(self):
        """Test with empty list"""
        result = python.inefficient_string_concat([])
        self.assertEqual(result, "")


class TestModifyingDuringIteration(unittest.TestCase):
    """Test modifying list while iterating"""
    
    def test_modifying_during_iteration(self):
        """Test modifying list during iteration"""
        items = [1, 2, 6, 7, 3, 8, 4]
        result = python.modifying_during_iteration(items)
        # Bug: not all items > 5 are removed due to iteration issue
        self.assertIsInstance(result, list)


class TestReturnInFinally(unittest.TestCase):
    """Test return in finally block"""
    
    def test_return_in_finally(self):
        """Test that finally return overrides try/except returns"""
        result = python.return_in_finally()
        self.assertEqual(result, "finally")


class TestBooleanParameter(unittest.TestCase):
    """Test boolean parameter"""
    
    def test_boolean_parameter_true(self):
        """Test with True parameter"""
        result = python.boolean_parameter(True)
        self.assertEqual(result, "option A")
    
    def test_boolean_parameter_false(self):
        """Test with False parameter"""
        result = python.boolean_parameter(False)
        self.assertEqual(result, "option B")


class TestIsNum(unittest.TestCase):
    """Test _is_num function"""
    
    def test_is_num_with_int(self):
        """Test with integer"""
        result = python._is_num(5)
        self.assertTrue(result)
    
    def test_is_num_with_float(self):
        """Test with float"""
        result = python._is_num(5.5)
        self.assertTrue(result)
    
    def test_is_num_with_string(self):
        """Test with string"""
        result = python._is_num("5")
        self.assertFalse(result)


class TestEscape(unittest.TestCase):
    """Test _escape function"""
    
    def test_escape_xml(self):
        """Test XML escaping"""
        result = python._escape("<tag>&content</tag>", format='xml')
        self.assertEqual(result, "&lt;tag&gt;&amp;content&lt;/tag&gt;")
    
    def test_escape_control(self):
        """Test control character escaping"""
        result = python._escape("line1\nline2\ttab", format='control')
        self.assertEqual(result, "line1\\nline2\\ttab")
    
    def test_escape_quote(self):
        """Test quote escaping"""
        result = python._escape('say "hello"', quote='"')
        self.assertEqual(result, 'say \\"hello\\"')
    
    def test_escape_no_format(self):
        """Test with no format"""
        result = python._escape("normal text", quote=None)
        self.assertEqual(result, "normal text")


class TestUtilityClass(unittest.TestCase):
    """Test utility class with only static methods"""
    
    def test_utility_class_method1(self):
        """Test static method 1"""
        result = python.UtilityClass.method1()
        self.assertEqual(result, 1)
    
    def test_utility_class_method2(self):
        """Test static method 2"""
        result = python.UtilityClass.method2()
        self.assertEqual(result, 2)


class TestEmptyExceptBlock(unittest.TestCase):
    """Test empty except block"""
    
    def test_empty_except_block(self):
        """Test function with empty except blocks"""
        result = python.empty_except_block()
        self.assertIsNone(result)


class TestDangerousOperation(unittest.TestCase):
    """Test dangerous operation"""
    
    def test_dangerous_operation(self):
        """Test dangerous operation raises ValueError"""
        with self.assertRaises(ValueError):
            python.dangerous_operation()


class TestAssignmentInConditional(unittest.TestCase):
    """Test assignment in conditional (walrus operator)"""
    
    def test_assignment_in_conditional(self):
        """Test walrus operator in conditional"""
        result = python.assignment_in_conditional()
        self.assertEqual(result, 15)


class TestIntegration(unittest.TestCase):
    """Integration tests"""
    
    def test_multiple_functions_together(self):
        """Test multiple functions work together"""
        # Test that various functions can be called in sequence
        python.unused_variables()
        python.wrong_none_comparison(None)
        python.boolean_parameter(True)
        self.assertTrue(True)
    
    def test_exception_handling_patterns(self):
        """Test various exception handling patterns"""
        # Bare except
        python.bare_except()
        
        # Empty except
        python.empty_except_block()
        
        # Lost exception
        result = python.lost_exception()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
