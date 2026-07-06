from database.bigquery_service import BigQueryService


class DatabaseManager:

    def __init__(self):
        self.bigquery = None

    def connect(self, project_id):

        self.bigquery = BigQueryService(project_id)

    def upload_sales_data(self, dataframe, table_id):

        if self.bigquery:
            return self.bigquery.upload_dataframe(
                dataframe,
                table_id
            )

        return False

    def query(self, sql):

        if self.bigquery:
            return self.bigquery.run_query(sql)

        return None