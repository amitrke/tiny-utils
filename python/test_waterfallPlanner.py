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
                    <td><strong>Phase 1</strong></td>
                    <td></td>
                </tr>
                <tr>
                    <td>1</td>
                    <td><strong>Task 1</strong></td>
                    <td>Completed</td>
                    <td>
                        <div class="content-wrapper">
                            <p><time datetime="2024-01-10" /></p>
                        </div>
                    </td>
                    <td>
                        <div class="content-wrapper">
                            <p><time datetime="2024-01-11" /></p>
                        </div>
                    </td>
                    <td>
                        <div class="content-wrapper">
                            <p>Completed</p>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>2</td>
                    <td><strong>Task 2</strong></td>
                    <td>In Progress</td>
                    <td>
                        <div class="content-wrapper">
                            <p><time datetime="2024-01-11" /></p>
                        </div>
                    </td>
                    <td>
                        <div class="content-wrapper">
                            <p><time datetime="2024-01-15" /></p>
                        </div>
                    </td>
                    <td>
                        <div class="content-wrapper">
                            <p>In Progress</p>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3</td>
                    <td><strong>Task 3</strong></td>
                    <td>Not Started</td>
                    <td>
                        <div class="content-wrapper">
                            <p><time datetime="2024-01-15" /></p>
                        </div>
                    </td>
                    <td>
                        <div class="content-wrapper">
                            <p><time datetime="2024-01-22" /></p>
                        </div>
                    </td>
                    <td>
                        <div class="content-wrapper">
                            <p>Not Started</p>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3.1</td>
                    <td>Subtask 1</td>
                    <td>Not Started</td>
                    <td>
                        <div class="content-wrapper">
                            <p><time datetime="2024-01-15" /></p>
                        </div>
                    </td>
                    <td>
                        <div class="content-wrapper">
                            <p><time datetime="2024-01-16" /></p>
                        </div>
                    </td>
                    <td>
                        <div class="content-wrapper">
                            <p>Not Started</p>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3.2</td>
                    <td>Subtask 2</td>
                    <td>Not Started</td>
                    <td>
                        <div class="content-wrapper">
                            <p><time datetime="2024-01-16" /></p>
                        </div>
                    </td>
                    <td>
                        <div class="content-wrapper">
                            <p><time datetime="2024-01-18" /></p>
                        </div>
                    </td>
                    <td>
                        <div class="content-wrapper">
                            <p>Not Started</p>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3.3</td>
                    <td>Subtask 3</td>
                    <td>Not Started</td>
                    <td>
                        <div class="content-wrapper">
                            <p><time datetime="2024-01-18" /></p>
                        </div>
                    </td>
                    <td>
                        <div class="content-wrapper">
                            <p><time datetime="2024-01-22" /></p>
                        </div>
                    </td>
                    <td>
                        <div class="content-wrapper">
                            <p>Not Started</p>
                        </div>
                    </td>
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