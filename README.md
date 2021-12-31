# Library API

## installation

### run on docker
* build image and run containers
```docker
docker-compose -f docker-compose.dev.yml up
```

* stop containers
```sh
docker-compose -f docker-compose.dev.yml stop api
```

### run locally
```sh
pip install -r requirements.txt
flask run
```

to setup database alembic
```sh
flask db init
flask db migrate
flask db upgrade
```

### see the api docs on /docs after running the flask server