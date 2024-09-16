from datetime import datetime


class Task:

	def __init__(self, title, description):
		self.title = title
		self.description = description
		self.completed = False
		self.created_at = datetime.now().isoformat()


class TaskManager:

	def __init__(self, storage):
		self.storage = storage

	def add_task(self, title, description):
		task = Task(title, description)
		self.storage.save_task(task)
		return task

	def complete_task(self, title):
		task = self.storage.get_task(title)
		if task:
			task.completed = True
			self.storage.update_task(task)
			return True
		return False

	def list_tasks(self, include_completed=False):
		tasks = self.storage.get_all_tasks()
		if include_completed:
			return tasks
		return [task for task in tasks if not task.completed]

	def generate_report(self):
		tasks = self.storage.get_all_tasks()
		total_tasks = len(tasks)
		completed_tasks = [task for task in tasks if task.completed]

		report = {
			"total": total_tasks,
			"completed": len(completed_tasks),
			"pending": total_tasks - len(completed_tasks)
		}

		return report

