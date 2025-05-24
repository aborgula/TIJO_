import unittest
from src.task_list import TaskList



class TaskListTestCase(unittest.TestCase):
    def test_add_task_should_add_task_to_list(self):

        #given
        task_list = TaskList()

        #when
        task_list.add_task("Buy milk")

        #then
        self.assertEqual(task_list.tasks(), ["Buy milk"])

    def test_delete_task_should_delete_task(self):

        #given
        task_list = TaskList()
        task_list.add_task("buy bread")

        #when
        task_list.delete_task("buy bread")

        #then
        self.assertEqual(task_list.tasks(), [])

    def test_add_multiple_tasks_should_add_list_of_tasks(self):

        #given
        task_list = TaskList()

        #when
        task_list.add_multiple_tasks(["buy bread", "wash the dishes"])

        #then
        self.assertEqual(task_list.tasks(), ["buy bread", "wash the dishes"])


if __name__ == '__main__':
    unittest.main()