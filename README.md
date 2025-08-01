# Admin Portal for Viewing SQLite Database from Cloud

Technologies Used:

- [Python](https://www.python.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [SQLite Cloud](https://sqlitecloud.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAdmin](https://github.com/aminalaee/sqladmin)

## Configuring the Environment

Within the `.env` file, you can set the following environment variables:

```env
DATABASE_URL=sqlitecloud://<your-database-url>
```

The database URL must be a SQLite Cloud URL, which you can obtain from your SQLite Cloud account.

## Running the Application

To run the application, follow these steps:

```bash
uv sync
source .venv/bin/activate
uvicorn main:app --reload
```

Then access the admin portal at <http://localhost:8000/admin>.
