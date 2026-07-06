from google.cloud import storage


class CloudStorageService:

    def __init__(self, bucket_name):
        self.client = storage.Client()
        self.bucket = self.client.bucket(bucket_name)

    def upload_file(self, source_file, destination_blob):

        blob = self.bucket.blob(destination_blob)

        blob.upload_from_filename(source_file)

        return True