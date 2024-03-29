# A4A_FlaskAPI_Solution
repository for creating a basic API with CRUD ops for A4A assessment

## Presentation
A presentation is provided depicting:
1. About me
2. Proud Project
3. Craft Demo - placeholder slide

You can reach the [presentation here](https://docs.google.com/presentation/d/1E2yLeENSo5K8Pu0g-1EbDE6dtxQv7_1lqarj1NR2RjM/edit#slide=id.geb4c6d2e93_0_137)

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