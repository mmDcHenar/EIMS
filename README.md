# E-commerce Inventory Management System

## Run using Docker compose:
```shell
docker compose up -d
```
it will build and run in port 8000 in the background.

### Or
## Install manually:
### Install depencencies
```shell
pip3 install -r requirements
```
### Migrate database:
```shell
alembic upgrade head
```
### Run the app (you can edit the host and port in the command):
```shell
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
```
