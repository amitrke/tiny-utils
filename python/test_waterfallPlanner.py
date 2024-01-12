from waterfallPlanner import WaterfallPlanner

def strip_whitespace(s):
    return s.strip().replace('\n', '').replace('  ', '')

def test_waterfall_planner():
    # # Test case 1: Empty data and config
    # data = []
    # config = {}
    # planner = WaterfallPlanner(data, config)
    # result = planner.plan()
    # assert result == '\n        \n        '  # Replace None with the expected result

    # Test case 2: Non-empty data and config
    data = [
        {
            "title": "Phase 1",
            "tasks": [
                {
                    "title": "Task 1",
                    "duration": 1,
                    "status": "Completed"
                },
                {
                    "title": "Task 2",
                    "duration": 2,
                    "status": "In Progress"
                },
                {
                    "title": "Task 3",
                    "duration": 3,
                    "status": "Not Started",
                    "tasks": [
                        {
                            "title": "Subtask 1",
                            "duration": 1,
                            "status": "Not Started"
                        },
                        {
                            "title": "Subtask 2",
                            "duration": 2,
                            "status": "Not Started"
                        },
                        {
                            "title": "Subtask 3",
                            "duration": 3,
                            "status": "Not Started"
                        }
                    ]
                }
            ]
        },
        {
            "title": "Phase 2",
            "startDate": "2024-01-10",
            "tasks": [
                {
                    "title": "Task 1",
                    "duration": 1,
                    "status": "Completed"
                },
                {
                    "title": "Task 2",
                    "duration": 2,
                    "status": "In Progress"
                },
                {
                    "title": "Task 3",
                    "duration": 3,
                    "status": "Not Started",
                    "tasks": [
                        {
                            "title": "Subtask 1",
                            "duration": 1,
                            "status": "Not Started"
                        },
                        {
                            "title": "Subtask 2",
                            "duration": 2,
                            "status": "Not Started"
                        },
                        {
                            "title": "Subtask 3",
                            "duration": 3,
                            "status": "Not Started"
                        }
                    ]
                }
            ]
        }
    ]
    config = {"key": "value"}
    planner = WaterfallPlanner(data, config)
    result = planner.plan()
    expectedResult = """
        <table>
    <tbody>
        <tr>
            <th>Phase </th>
            <th>S.No </th>
            <th>Task </th>
            <th>Start Date </th>
            <th>End Date </th>
            <th>Status </th>
            <th>Notes </th>
        </tr>
        <tr>
            <td><strong> Phase 1</strong> </td> <td><br /> </td>
            <td><br /> </td>
            <td><br /> </td>
            <td><br /> </td>
            <td><br /> </td>
            <td><br /> </td>
        </tr>
        <tr>
            <td><br /> </td>
            <td><strong> 1</strong> </td>
            <td><strong> Task 1</strong> </td>
            <td><strong></strong> </td>
            <td><strong></strong> </td>
            <td><strong> Completed</strong> </td>
            <td> </td>
        </tr>
        <tr>
            <td><br /> </td>
            <td><strong> 2</strong> </td>
            <td><strong> Task 2</strong> </td>
            <td><strong></strong> </td>
            <td><strong></strong> </td>
            <td><strong> In Progress</strong> </td>
            <td> </td>
        </tr>
        <tr>
            <td><br /> </td>
            <td><strong> 3</strong> </td>
            <td><strong> Task 3</strong> </td>
            <td><strong></strong> </td>
            <td><strong></strong> </td>
            <td><strong> Not Started</strong> </td>
            <td> </td>
        </tr>
        <tr>
            <td><br /> </td>
            <td>3.1 </td>
            <td>Subtask 1 </td>
            <td> </td>
            <td> </td>
            <td>Not Started </td>
            <td> </td>
        </tr>
        <tr>
            <td><br /> </td>
            <td>3.2 </td>
            <td>Subtask 2 </td>
            <td> </td>
            <td> </td>
            <td>Not Started </td>
            <td> </td>
        </tr>
        <tr>
            <td><br /> </td>
            <td>3.3 </td>
            <td>Subtask 3 </td>
            <td> </td>
            <td> </td>
            <td>Not Started </td>
            <td> </td>
        </tr>
        <tr>
            <td><strong> Phase 2</strong> </td> } <td><br /> </td>
            <td><br /> </td>
            <td><br /> </td>
            <td><br /> </td>
            <td><br /> </td>
            <td><br /> </td>
        </tr>
        <tr>
            <td><br /> </td>
            <td><strong> 1</strong> </td>
            <td><strong> Task 1</strong> </td>
            <td><strong> 2024-01-10</strong> </td>
            <td><strong> 2024-01-11</strong> </td>
            <td><strong> Completed</strong> </td>
            <td> </td>
        </tr>
        <tr>
            <td><br /> </td>
            <td><strong> 2</strong> </td>
            <td><strong> Task 2</strong> </td>
            <td><strong> 2024-01-11</strong> </td>
            <td><strong> 2024-01-15</strong> </td>
            <td><strong> In Progress</strong> </td>
            <td> </td>
        </tr>
        <tr>
            <td><br /> </td>
            <td><strong> 3</strong> </td>
            <td><strong> Task 3</strong> </td>
            <td><strong> 2024-01-15</strong> </td>
            <td><strong> 2024-01-22</strong> </td>
            <td><strong> Not Started</strong> </td>
            <td> </td>
        </tr>
        <tr>
            <td><br /> </td>
            <td>3.1 </td>
            <td>Subtask 1 </td>
            <td>2024-01-15 </td>
            <td>2024-01-16 </td>
            <td>Not Started </td>
            <td> </td>
        </tr>
        <tr>
            <td><br /> </td>
            <td>3.2 </td>
            <td>Subtask 2 </td>
            <td>2024-01-16 </td>
            <td>2024-01-18 </td>
            <td>Not Started </td>
            <td> </td>
        </tr>
        <tr>
            <td><br /> </td>
            <td>3.3 </td>
            <td>Subtask 3 </td>
            <td>2024-01-18 </td>
            <td>2024-01-22 </td>
            <td>Not Started </td>
            <td> </td>
        </tr>
    </tbody>
</table>"""
    strippedResult = strip_whitespace(result)
    strippedExpectedResult = strip_whitespace(expectedResult)
    assert strippedResult == strippedExpectedResult  # Replace None with the expected result

    # Add more test cases as needed

    print("All test cases pass")

test_waterfall_planner()