from unittest import TestCase
from app import app


class TestPlayers(TestCase):

    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def get_mock_response(self):
        return [
            {
                "playerID": "w1",
                "birthYear": 1992,
                "birthMonth": 5,
                "birthDay": 1,
                "birthCountry": "USA",
                "birthState": "OH",
                "birthCity": "Bridgeport",
                "deathYear": 2010,
                "deathMonth": 12,
                "deathDay": 29,
                "deathCountry": "USA",
                "deathState": "OH",
                "deathCity": "BELL",
                "nameFirst": "BIll",
                "nameLast": "White",
                "nameGiven": "William",
                "weight": 160,
                "height": 160,
                "bats": "R",
                "throws": "R",
                "debut": "1883-06-01",
                "finalGame": "1888-10-14",
                "retroID": "whitb104",
                "bbrefID": "whitebi02",
            },
            {
                "playerID": "w2",
                "birthYear": 1992,
                "birthMonth": 5,
                "birthDay": 1,
                "birthCountry": "USA",
                "birthState": "OH",
                "birthCity": "Bridgeport",
                "deathYear": 2010,
                "deathMonth": 12,
                "deathDay": 29,
                "deathCountry": "USA",
                "deathState": "OH",
                "deathCity": "BELL",
                "nameFirst": "BIll",
                "nameLast": "White",
                "nameGiven": "William",
                "weight": 160,
                "height": 160,
                "bats": "R",
                "throws": "R",
                "debut": "1883-06-01",
                "finalGame": "1888-10-14",
                "retroID": "whitb104",
                "bbrefID": "whitebi02",
            },
            {
                "playerID": "w3",
                "birthYear": 1992,
                "birthMonth": 5,
                "birthDay": None,
                "birthCountry": None,
                "birthState": None,
                "birthCity": "Bridgeport",
                "deathYear": 2010,
                "deathMonth": 12,
                "deathDay": 29,
                "deathCountry": "USA",
                "deathState": "OH",
                "deathCity": "BELL",
                "nameFirst": "BIll",
                "nameLast": "White",
                "nameGiven": "William",
                "weight": 160,
                "height": 160,
                "bats": "R",
                "throws": "R",
                "debut": "1883-06-01",
                "finalGame": "1888-10-14",
                "retroID": "whitb104",
                "bbrefID": "whitebi02",
            },
        ]

    def test_get_all_players(self):
        response = self.client.get("/api/players")
        self.assertIsNotNone(response)
        self.assertEqual(first=200, second=response.status_code)
        self.assertEqual(first=response.json, second=self.get_mock_response())

    def test_get_player_by_id(self):
        mock_response = self.get_mock_response()
        for i in range(1, len(mock_response)):
            individual_response = self.client.get(f"/api/players/w{i}")
            self.assertIsNotNone(individual_response)
            self.assertEqual(first=200, second=individual_response.status_code)
            self.assertEqual(
                first=individual_response.json, second=mock_response[i - 1]
            )

    def test_get_player_by_id_not_found(self):
        id_not_in_list = "w4"
        individual_response = self.client.get(f"/api/players/{id_not_in_list}")
        self.assertIsNotNone(individual_response)
        self.assertEqual(first=404, second=individual_response.status_code)
        self.assertEqual(
            first=individual_response.json,
            second={"message": "No such player was found"},
        )
