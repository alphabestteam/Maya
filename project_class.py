from datetime import datetime, timedelta

class Project:
    def __init__(self, project_description) -> None:
        self._project_description = project_description
        self.starting_date = datetime.now()
        self.due_date = self.starting_date + timedelta(days=self.calculate_days())
        self._tasks_list = []
        self.developers_list = []
        self.to_do_tasks = []
        self.completed_tasks = [] 
        self.project_cost = 0
        self.is_done = self.is_project_done()
    
    @property
    def project_description(self):
        return self._project_description

    @property
    def tasks_list(self):
        return self._tasks_list
    

    def calculate_days(self) -> int:
        """
        a function that calculates the days to complete of the project based on the working days of the tasks
        """
        days_to_complete = 0
        for task in self.tasks_list:
            days_to_complete += task.working_days
        return days_to_complete

    
    def is_project_done(self) -> bool:
        """
        a function that returns wether a project is done or not
        """
        return self.to_do_tasks == []


    def calculate_project_cost(self) -> float:
        """
        a function that calculates how much the project costs based on the rewards of the completed tasks
        """
        reward_sum = 0
        for task in self.completed_tasks:
            reward_sum += task.task_reward
        return reward_sum

    def add_new_task(self, new_task) -> None:
        """
        a function that adds a new task to a project
        """
        if not new_task in self.tasks_list: 
            self.tasks_list.append(new_task)
            self.developers_list.append(new_task.allotment)
            if new_task.task_completed:
                self.completed_tasks.append(new_task)
            else:
                self.to_do_tasks.append(new_task)
    

    def remove_task(self, task) -> None:
        """
        a function that removes tasks from lists of tasks
        """
        if task in self.tasks_list:
            if task in self.to_do_tasks:
                self.to_do_tasks.remove(task)
                self.tasks_list.remove(task)
                self.developers_list.remove(task.allotment)


    def search_task(self, task_description: str):
        """
        a function that gets a task descriptions and returns the task if there is one
        """
        for task in self.tasks_list:
            if task.task_description == task_description:
                return task
        else:
            return "Task is not found"
        

    def tasked_finished(self, task):
        """
        a function that moves a task to completed tasks if it's finished
        """
        if task in self.to_do_tasks and task.task_completed:
            self.to_do_tasks.remove(task)
            self.completed_tasks.append(task)
