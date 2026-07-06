import os

from dotenv import load_dotenv

from database.database_manager import DatabaseManager

load_dotenv()


def get_database():

    db = DatabaseManager()

    project_id = os.getenv("PROJECT_ID")

    if project_id:
        db.connect(project_id)

    return db