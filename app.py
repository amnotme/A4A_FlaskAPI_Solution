from flask import Flask
from dotenv import load_dotenv
from api.player import get_player, get_players, load_data

load_dotenv()
app = Flask(__name__)

app.add_url_rule("/api/players", methods=["GET"], view_func=get_players)
app.add_url_rule("/api/players/<player_id>", methods=["GET"], view_func=get_player)
app.add_url_rule("/api/load-data", methods=["POST"], view_func=load_data)


@app.route("/")
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
