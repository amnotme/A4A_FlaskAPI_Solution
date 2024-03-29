# Template_FlaskAPI
Template repository for creating a basic API with CRUD ops

## Task

**Given players.csv, create a service that can:**

1. Retrieve Players data from Players.csv
2. Query players by player id
3. Query all players

**Use the following routes:**

* GET /api/players
* GET /api/players/<player_id>

Nice to have

1. Containerize
2. Have unit tests
3. Persist data across sessions

## Usage

* Activate the virtual environment (if using Pipenv):
```bash
pipenv shell
```
* Start the Flask Application

```bash
flask run
```

## Using Docker

* Build image
```bash
 docker build -t a4a .
```
* Run image with exposed port, auto container removal, hot-reloading with workd irectory mounted

```bash
docker container run --rm  --env.file=.env -p 5001:5000 -v "$(pwd):/app a4a
```