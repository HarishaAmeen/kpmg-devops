import unittest
from script.run import get_key

my_obj = {
    "1": 1,
    "2": {
        "3": {
            "4": 4
        },
        "5": 5
    }
}

class TestGetKeyFunc(unittest.TestCase):
    def test_basic1(self):
        res1 = get_key(my_obj, "1")
        self.assertEqual(res1, 1)
    
    def test_when_key_or_obj_not_passed(self):
        res = get_key(my_obj)
        self.assertEqual(res, "Pass nested obj and key")
    
    def test_nested_key1(self):
        res1 = get_key(my_obj, "2/5")
        self.assertEqual(res1, 5)
    
    def test_nested_key2(self):
        res1 = get_key(my_obj, "2/3/4")
        self.assertEqual(res1, 4)
    
    def test_exception_when_incorrect_key_path(self):
        self.assertRaises(Exception, lambda: get_key(my_obj, "2/3/5"))
    
    