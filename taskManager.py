import unittest

class Task:
    """Задача"""
    def __init__(self, title, description):
        if not title:
            raise ValueError("Title cannot be empty")
        self.title = title
        self.description = description
        self.completed = False
    
    def mark_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        return task
    
    def get_tasks(self):
        return self.tasks
    
    def get_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
    
    def test_add_task(self):
        """Проверяет, что задача добавляется правильно и имеет ожидаемые атрибуты."""
        task = self.manager.add_task("Test Task", "This is a test task")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task")
        self.assertFalse(task.completed)
    
    def test_get_tasks(self):
        """Проверяет, что get_tasks возвращает правильное количество задач."""
        self.manager.add_task("Task 1", "Description 1")
        self.manager.add_task("Task 2", "Description 2")
        self.assertEqual(len(self.manager.get_tasks()), 2)
    
    def test_get_task_by_title(self):
        """Проверяет, что поиск задачи по заголовку работает корректно."""
        self.manager.add_task("Unique Task", "Unique Description")
        task = self.manager.get_task_by_title("Unique Task")
        self.assertIsNotNone(task)
        self.assertEqual(task.title, "Unique Task")
    
    def test_mark_task_completed(self):
        """Проверяет, что задача правильно отмечается как выполненная."""
        task = self.manager.add_task("Complete Task", "Needs to be completed")
        task.mark_completed()
        self.assertTrue(task.completed)
    
    def test_add_task_empty_title(self):
        """Проверяет, что нельзя добавить задачу с пустым заголовком."""
        with self.assertRaises(ValueError):
            self.manager.add_task("", "No title task")

if __name__ == "__main__":
    unittest.main(verbosity=2)
