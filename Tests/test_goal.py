import uuid
from api.goal_api import GoalsAPI


def test_goal_lifecycle():
    goal_name = f"Goal-{uuid.uuid4()}"

    # CREATE
    create_response = GoalsAPI.create_goal(goal_name)

    assert create_response.status_code == 200

    goal_id = create_response.json()["goal"]["id"]

    # GET GOALS
    goals_response = GoalsAPI.get_goals()

    assert goals_response.status_code == 200

    goals = goals_response.json()["goals"]

    assert any(goal["id"] == goal_id for goal in goals)

    # GET GOAL
    goal_response = GoalsAPI.get_goal(goal_id)

    assert goal_response.status_code == 200

    assert goal_response.json()["goal"]["name"] == goal_name

    # UPDATE
    updated_name = "Updated Goal"

    update_response = GoalsAPI.update_goal(
        goal_id,
        updated_name
    )

    assert update_response.status_code == 200

    updated_goal = GoalsAPI.get_goal(goal_id)

    assert updated_goal.json()["goal"]["name"] == updated_name

    # DELETE
    delete_response = GoalsAPI.delete_goal(goal_id)

    assert delete_response.status_code == 200


