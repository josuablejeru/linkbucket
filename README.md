# linkbucket
A simple and central place to organize all your links from the internet

### Preparations
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

### Create a new module

Then naming the module write "mod_" at the beginning.

In this example you see how the common structure is made for a module

```bash
.
├── __init__.py
├── auth_controller.py
├── forms
│   ├── __init__.py
│   ├── login_form.py
│   └── registration_form.py
└── models
    ├── __init__.py
    ├── login_form.py
    └── registration_form.py
```

new models have to be imported in the `app/__init__.py` 
