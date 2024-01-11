from waterfallPlanner import WaterfallPlanner

def strip_whitespace(s):
    return s.strip().replace('\n', '').replace(' ', '')

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
                    <td><strong>Phase1</strong></td>
                    <td></td>
                </tr>
                <tr>
                    <td>1</td>
                    <td><strong>Task1</strong></td>
                    <td>Completed</td>
                    <td>2024-01-10</td>
                    <td>2024-01-11</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td><strong>Task2</strong></td>
                    <td>InProgress</td>
                    <td>2024-01-11</td>
                    <td>2024-01-15</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td><strong>Task3</strong></td>
                    <td>NotStarted</td>
                    <td>2024-01-15</td>
                    <td>2024-01-22</td>
                </tr>
                <tr>
                    <td>3.1</td>
                    <td>Subtask1</td>
                    <td>NotStarted</td>
                    <td>2024-01-15</td>
                    <td>2024-01-16</td>
                </tr>
                <tr>
                    <td>3.2</td>
                    <td>Subtask2</td>
                    <td>NotStarted</td>
                    <td>2024-01-16</td>
                    <td>2024-01-18</td>
                </tr>
                <tr>
                    <td>3.3</td>
                    <td>Subtask3</td>
                    <td>NotStarted</td>
                    <td>2024-01-18</td>
                    <td>2024-01-22</td>
                </tr>
            </tbody>
        </table>
        """
    strippedResult = strip_whitespace(result)
    strippedExpectedResult = strip_whitespace(expectedResult)
    assert strippedResult == strippedExpectedResult  # Replace None with the expected result

    # Add more test cases as needed

    print("All test cases pass")

test_waterfall_planner()