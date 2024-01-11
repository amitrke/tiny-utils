from waterfallPlanner import WaterfallPlanner

def test_waterfall_planner():
    # Test case 1: Empty data and config
    data = []
    config = {}
    planner = WaterfallPlanner(data, config)
    result = planner.plan()
    assert result == ''  # Replace None with the expected result

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
    expectedResult = "Phase 1\n"
    assert result == expectedResult  # Replace None with the expected result

    # Add more test cases as needed

    print("All test cases pass")

test_waterfall_planner()