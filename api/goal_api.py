import os
import requests
from dotenv import load_dotenv
from requests import Response

load_dotenv()

BASE_URL = "https://api.clickup.com/api/v2"

TOKEN = os.getenv("CLICKUP_TOKEN")
TEAM_ID = os.getenv("TEAM_ID")

if not TOKEN or not TEAM_ID:
    raise ValueError("Missing CLICKUP_TOKEN or TEAM_ID in .env")

HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}


class GoalsAPI:

    @staticmethod
    def create_goal(name):
        return requests.post(
            f"{BASE_URL}/team/{TEAM_ID}/goal",
            headers=HEADERS,
            json={"name": name}
        )

    @staticmethod
    def get_goals():
        return requests.get(
            f"{BASE_URL}/team/{TEAM_ID}/goal",
            headers=HEADERS
        )

    @staticmethod
    def get_goal(goal_id):
        return requests.get(
            f"{BASE_URL}/goal/{goal_id}",
            headers=HEADERS
        )

    @staticmethod
    def update_goal(goal_id, name):
        return requests.put(
            f"{BASE_URL}/goal/{goal_id}",
            headers=HEADERS,
            json={"name": name}
        )

    @staticmethod
    def delete_goal(goal_id: object) -> Response:
        return requests.delete(
            f"{BASE_URL}/goal/{goal_id}",
            headers=HEADERS
        )


class GoalAPI:
    @classmethod
    def create_goal(cls, goal_name):
        pass

    @classmethod
    def get_goals(cls):
        pass

    @classmethod
    def get_goal(cls, goal_id):
        pass

    @classmethod
    def update_goal(cls, goal_id, updated_name):
        pass

    @classmethod
    def delete_goal(cls, goal_id):
        pass