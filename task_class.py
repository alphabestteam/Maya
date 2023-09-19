from datetime import datetime
class Task:
    def __init__(self, task_description: str, project, working_days: int, task_complication: int, task_completed: bool) -> None:
        self._task_description = task_description
        self._task_starting_date = datetime.now()
        self._task_due_date = self.task_starting_date + self.working_days #SEE HOW TO ADD THAT
        self._task_project = project
        self._working_days = working_days
        self._task_complication = task_complication
        self._allotment = None
        self.task_reward = 0
        self.task_completed = task_completed

    @property
    def task_description(self):
        return self._task_description

    @property
    def task_starting_date(self):
        return self._task_starting_date
    
    @property
    def task_due_date(self):
        return self._task_due_date
    
    @property
    def task_project(self):
        return self._task_project
    
    @property
    def working_days(self):
        return self._working_days

    @property
    def task_complication(self):
        return self._task_complication
    
    @property
    def allotment(self):
        return self._allotment

    @property
    def task_completed(self):
        return self._task_completed
    
    @allotment.setter
    def allotment(self, developer) -> None:
        self.allotment = developer


    def calculate_task_reward(self, developer) -> float:
        """
        a function that calculates the task reward
        """
        if not self.allotment:
            return 0
        else:
            complication_by_days = self.task_complication / self.working_days
            reward = developer.seniority * complication_by_days
            return reward


    def is_task_completed(self) -> bool:
        """
        a function that checks if a developer finished the task or not
        """
        if not self.allotment == None:
            if self in self.allotment.completed_tasks:
                self.task_completed == True
