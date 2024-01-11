
from jinja2 import Template
import datetime
class WaterfallPlanner:
    def __init__(self, data, config: dict):
        self.data = data
        self.config = config
        self.template = Template("""
        {% macro macro_status(status) -%}
        <div class="content-wrapper">
            <p>{{ status }}</p>
        </div>
        {%- endmacro %}
        {% macro macro_date(date) -%}
        <div class="content-wrapper">
            <p><time datetime="{{ date }}" /></p>
        </div>
        {%- endmacro %}
        <table>
            <tbody>
                <tr>
                    <th>Phase</th>
                    <th>S.No</th>
                    <th>Task</th>
                    <th>Start Date</th>
                    <th>End Date</th>
                    <th>Status</th>
                </tr>
            {% for phase in data %}
                <tr>
                    <td><strong>{{ phase.title }}</strong></td>
                    <td><br /></td>
                    <td><br /></td>
                    <td><br /></td>
                    <td><br /></td>
                    <td><br /></td>
                </tr>
                {% for task in phase.tasks %}
                {% set taskIndex = loop.index %}
                <tr>
                    <td><br /></td>
                    <td><strong>{{taskIndex}}</strong></td>
                    <td><strong>{{ task.title }}</strong></td>
                    <td>{{ macro_date(task.startDate) }}</td>
                    <td>{{ macro_date(task.endDate) }}</td>
                    <td>{{ macro_status(task.status) }}</td>
                </tr>
                {% if task.tasks %}
                    {% for subtask in task.tasks %}
                        <tr>
                            <td><br /></td>
                            <td>{{taskIndex}}.{{loop.index}}</td>
                            <td>{{ subtask.title }}</td>
                            <td>{{ macro_date(subtask.startDate) }}</td>
                            <td>{{ macro_date(subtask.endDate) }}</td>
                            <td>{{ macro_status(subtask.status) }}</td>
                        </tr>
                    {% endfor %}
                {% endif %}
                {% endfor %}
            {% endfor %}
            </tbody>
        </table>
        """)

    def _datePlusDuration(self, date, duration):
        """Returns a new date that is the given date plus the given duration"""
        """Date format: YYYY-MM-DD"""
        """Skips weekends"""
        parsedDate = datetime.datetime.strptime(date, "%Y-%m-%d")
        newDate = parsedDate + datetime.timedelta(days=duration)
        #Skip weekends
        if newDate.weekday() == 5:
            newDate = newDate + datetime.timedelta(days=2)
        elif newDate.weekday() == 6:
            newDate = newDate + datetime.timedelta(days=1)
        return newDate.strftime("%Y-%m-%d")

    def _updateTaskStartAndEndDates(self):
        for phase in self.data:
            #The start date of the phase is the start date of the first task in the phase
            #Date format: YYYY-MM-DD
            phaseStartDate = phase["startDate"]
            for taskidx, task in enumerate(phase["tasks"]):
                #If this is the first task in the phase, then the start date is the phase start date
                if taskidx == 0:
                    task["startDate"] = phaseStartDate
                else:
                    #Otherwise, the start date is the end date of the previous task
                    task["startDate"] = phase["tasks"][taskidx-1]["endDate"]

                #The end date is the start date plus the duration
                #If task duration is missing, then default to 1
                if "duration" not in task:
                    task["duration"] = 1
                task["endDate"] = self._datePlusDuration(task["startDate"], task["duration"])

                #If there are subtasks, then the end date is the end date of the last subtask
                if "tasks" in task:
                    for subtaskidx, subtask in enumerate(task["tasks"]):
                        #If this is the first subtask, then the start date is the start date of the parent task
                        if subtaskidx == 0:
                            subtask["startDate"] = task["startDate"]
                        else:
                            #Otherwise, the start date is the end date of the previous subtask
                            subtask["startDate"] = task["tasks"][subtaskidx-1]["endDate"]

                        #The end date is the start date plus the duration
                        #If task duration is missing, then default to 1
                        if "duration" not in subtask:
                            subtask["duration"] = 1
                        subtask["endDate"] = self._datePlusDuration(subtask["startDate"], subtask["duration"])
                    task["endDate"] = task["tasks"][-1]["endDate"]

    def plan(self):
        self._updateTaskStartAndEndDates()
        return self.template.render(data=self.data, config=self.config)
        