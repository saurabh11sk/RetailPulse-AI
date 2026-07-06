from google.cloud import bigquery


class BigQueryService:

    def __init__(self, project_id):
        self.client = bigquery.Client(project=project_id)

    def upload_dataframe(self, dataframe, table_id):

        job = self.client.load_table_from_dataframe(
            dataframe,
            table_id
        )

        job.result()

        return True

    def run_query(self, query):

        query_job = self.client.query(query)

        return query_job.to_dataframe()