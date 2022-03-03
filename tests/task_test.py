import unittest

from src.task import Task

class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = Task("Washing Dishes", 15)

    def test_task_has_description(self):
        self.assertEqual("Washing Dishes", self.task.description)

    def test_task_has_duration(self):
        self.assertEqual(15, self.task.duration)