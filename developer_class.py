class Developer:
    def __init__(self, developer_name) -> None:
        self._developer_name = developer_name
        self.completed_tasks = []
        self.working_days = 0    
        self.total_reward = 0
        self.to_do_tasks = []
        self.seniority = 1

        @property
        def developer_name(self) -> str:
            return self._developer_name


    def calculate_reward(self) -> float:
        """
        a function that calculates the reward
        """
        reward_sum = 0
        for task in self.completed_tasks:
            reward_sum += task.task_reward
        return reward_sum
    
    def get_working_days(self) -> int:
        """
        a function that calculates the working days of the developer
        """
        for task in self.completed_tasks:
            self.working_days += task.working_days
        return self.working_days
    
    def calculate_seniority(self):
        """
        a function that calculates the seniority according to the completed tasks of the developer
        """
        for task in self.completed_tasks:
            self.seniority += task.task_complication
        return self.seniority
    
    def add_new_task(self, task) -> None:
        """
        a function that adds a task to the list of tasks if the task's allotment is equal to self
        """
        if task.allotment == self:
            if task.task_completed:
                self.completed_tasks.append(task)
            else:
                self.to_do_tasks.append(task)


    def completed_task(self, task) -> None:
        """
        a function that adds a task to the completed tasks list and updates the reward and seniority of the developer
        """
        if task in self.to_do_tasks:
            self.to_do_tasks.remove(task)
            self.completed_tasks.append(task)
            self.total_reward = self.calculate_reward()
            self.seniority = self.calculate_seniority()