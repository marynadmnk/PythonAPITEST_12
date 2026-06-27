import requests
import uuid

from api.goal_api import GoalsAPI

BASE_URL = "https://api.clickup.com/api/v2"


def test_get_goals_without_token():

    goal_name = f"Goal-{uuid.uuid4()}"

    create_response = GoalsAPI.create_goal(goal_name)

    assert create_response.status_code == 200

    goal_id = create_response.json()["goal"]["id"]

    try:

        response = requests.get(
            f"{BASE_URL}/goal/{goal_id}"
        )

        assert response.status_code == 400

    finally:

        GoalsAPI.delete_goal(goal_id)