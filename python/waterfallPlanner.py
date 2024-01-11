
class WaterfallPlanner:
    def __init__(self, data, config: dict):
        self.data = data
        self.config = config

    def _plan_phase(self, phase: dict):
        response = phase["title"] + "\n"
        # for task in phase["tasks"]:
        #     response += task["title"] + "\n"
        #     if "tasks" in task:
        #         for subtask in task["tasks"]:
        #             response += subtask["title"] + "\n"
        return response
    def plan(self):
        response = ""
        for phase in self.data:
            response += self._plan_phase(phase)
        return response
        