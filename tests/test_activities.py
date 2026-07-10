from src.app import activities


def test_get_activities_returns_seeded_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert set(data) == set(activities)
    assert "Chess Club" in data


def test_get_activities_returns_activity_details(client):
    response = client.get("/activities")

    activity = response.json()["Chess Club"]

    assert activity["description"] == "Learn strategies and compete in chess tournaments"
    assert activity["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert activity["max_participants"] == 12
    assert activity["participants"] == ["michael@mergington.edu", "daniel@mergington.edu"]


def test_root_redirects_to_static_frontend(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"