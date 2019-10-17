# linkbucket
A simple and central place to organize all your links from the internet

### How to
- use the values from `.flaskenv` and put them into a normal `.env` file
- start the project with `docker-compose up`


### Working with the Database
To generate an new migration use
```bash
$ flask db migrate -m "users table"
```
This will make a new migrationscript with the name "users table"

To apply this changes type
```bash
$ flask db upgrade
```
