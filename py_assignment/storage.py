import json
import os
from task_manager import Task

class Storage:
	def __init__(self, file_path="tasks.json"):
		self.file_path = file_path
		self.tasks = self.load_tasks()

	def save_task(self, task):
		self.tasks.append(self.task_to_dict(task))
		self._save_to_file()

	def update_task(self, updated_task):
		updated_task_dict = self.task_to_dict(updated_task)
		for i, task in enumerate(self.tasks):
			if task["title"] == updated_task_dict["title"]:
				self.tasks[i] = updated_task_dict
				break
		self._save_to_file()

	def get_task(self, title):
		for task in self.tasks:
			if task["title"] == title:
				return self.dict_to_task(task)
		return None

	def get_all_tasks(self):
		return [self.dict_to_task(task) for task in self.tasks]

	def clear_all_tasks(self):
		self.tasks = []
		self._save_to_file()

	def load_tasks(self):
		if os.path.exists(self.file_path):
			try:
				with open(self.file_path, 'r') as f:
					return json.load(f)
			except (json.JSONDecodeError, ValueError):
				return []
		return []

	def _save_to_file(self):
		with open(self.file_path, 'w') as f:
			json.dump(self.tasks, f, indent=4)

	def task_to_dict(self, task):
		return {
			"title": task.title,
			"description": task.description,
			"completed": task.completed,
			"created_at": task.created_at
		}

	def dict_to_task(self, task_dict):
		task = Task(task_dict["title"], task_dict["description"])
		task.completed = task_dict["completed"]
		task.created_at = task_dict["created_at"]
		return task
