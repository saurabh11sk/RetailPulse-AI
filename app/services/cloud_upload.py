from database.cloud_connection import get_database
from config.cloud_config import DATASET_ID, TABLE_ID


def upload_to_bigquery(df):

    db = get_database()

    table_id = f"{DATASET_ID}.{TABLE_ID}"

    return db.upload_sales_data(
        df,
        table_id
    )
