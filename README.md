### Database Cleaning Strategies
- CS322 Project
- Tech Stack: Python, Postgresql
- Dataset and ERD taken from [here](https://www.postgresqltutorial.com/postgresql-sample-database/)
- UI: [Figma](https://www.figma.com/proto/nHYYsAzQl6GTb1C7DBhiGs/DB-Cleaning-Strats?node-id=1%3A2&scaling=min-zoom)

#### Dependencies:
- python: [Install](https://www.python.org/)
- pipenv: `pip install pipenv`
- postgresql: [Install](https://www.postgresql.org/) 

#### Get Started:
Make a `.env` file like `.env.example`  
Import Database:
- Linux: `pg_restore -c -i -U <username> -d dvdrental -v "/location/to/dvdrental.tar" -W`
- Windows: Import via pgadmin

```
pipenv shell
pipenv install
python app.py
```

To schedule the cron job:  
- Windows: Use `Task Scheduler` and make a `cron.bat` file as described in `cron.bat.example`
- Linux: Use `crontab`