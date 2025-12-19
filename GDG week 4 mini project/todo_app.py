import json
import os

# Task Class
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        """Convert Task object to dictionary (for JSON serialization)"""
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        """Create Task object from dictionary (JSON deserialization)"""
        return Task(
            data["id"],
            data["title"],
            data["completed"]
        )



# Todo Manager Class
class TodoManager:
    FILE_NAME = "todos.json"

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)  # converts JSON to dictionary (diserialization)
                self.tasks = []
                for task in data:
                    self.tasks.append(Task.from_dict(task))

    def save_tasks(self):
        with open(self.FILE_NAME, "w") as file:
            task_list = []
            for task in self.tasks:
                task_list.append(task.to_dict())
            json.dump(task_list, file, indent=4)


    def add_task(self, title):
        if len(self.tasks) == 0:
            task_id = 1
        else:
            task_id = self.tasks[-1].id + 1

        task = Task(task_id, title)
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.\n")
            return
        print("\nTodo List:")

        for task in self.tasks:
            if task.completed == True:
                status = "Completed"
            else:
                status = "Not Completed"

            print(f"ID: {task.id} | Title: {task.title} | Status: {status}")
        print()

    def update_task(self, task_id, new_title=None, completed=None):
        for task in self.tasks:
            if task.id == task_id:
                if new_title is not None:
                    task.title = new_title
                if completed is not None:
                    task.completed = completed
                self.save_tasks()
                return
        print("Task not found.")

    def delete_task(self, task_id):
        new_task_list = []

        for task in self.tasks:
            if task.id != task_id:
                new_task_list.append(task)
            else:
                print(f"Task with ID {task_id} has been deleted.")

        self.tasks = new_task_list
        self.save_tasks()



# CLI Application Class
class TodoApp:
    def __init__(self):
        self.manager = TodoManager()

    def run(self):
        while True:
            print("==== Todo App ====\n")
            print("1. Add Todo")
            print("2. View Todos")
            print("3. Update Todo")
            print("4. Delete Todo")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter task title: ")
                self.manager.add_task(title)

            elif choice == "2":
                self.manager.view_tasks()

            elif choice == "3":
                task_id = int(input("Enter task ID: "))
                new_title = input("New title (leave empty to skip): ")
                status_input = input("Mark as completed? (yes/no/skip): ")

                new_title = new_title if new_title else None
                completed = None
                if status_input.lower() == "yes":
                    completed = True
                elif status_input.lower() == "no":
                    completed = False

                self.manager.update_task(task_id, new_title, completed)

            elif choice == "4":
                task_id = int(input("Enter task ID to delete: "))
                self.manager.delete_task(task_id)

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice!")


# Program Entry Point
if __name__ == "__main__":
    app = TodoApp()
    app.run()
