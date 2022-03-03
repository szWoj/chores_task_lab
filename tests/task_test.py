import unittest

from src.task import Task
from task_decider import *

class TestTask(unittest.TestCase):

    def setUp(self):
        self.task1 = Task("Washing Dishes", 15)
        self.task2 = Task("Cooking Dinner", 60)
        self.task3 = Task("Cleaning Windows", 50)
        self.task4 = Task("Do dishes", 30)
        self.task5 = Task(None, 0)



    def test_task_has_description(self):
        self.assertEqual("Washing Dishes", self.task1.description)

    def test_task_has_duration(self):
        self.assertEqual(15, self.task1.duration)

    def test_task_decider_washing_over_cooking(self):
        result = get_preffered_option(self.task1, self.task2)
        self.assertEqual("Washing Dishes", result)
    
    def test_task_decider_cooking_cleaning(self):
        result = get_preffered_option(self.task2, self.task3)
        self.assertEqual("Cooking Dinner", result)
    
    def test_task_cleaning_over_washing(self):
        result = get_preffered_option(self.task1, self.task3)
        self.assertEqual("Cleaning Windows", result)

    def test_does_task_exist(self):
        result = does_task_exist(self.task1)
        self.assertEqual(True, result)
    
    def test_does_task_exist_fail(self):
        result = does_task_exist(self.task5)
        self.assertEqual(False, result)

    def test_one_task_description_unmatched(self):
        result = get_preffered_option(self.task1, self.task4)
        self.assertEqual("This task does not exist", result)
    
    def test_longest_task(self):
        result = get_longest_task(self.task1, self.task2)
        self.assertEqual("Cooking Dinner", result)

        
    

    