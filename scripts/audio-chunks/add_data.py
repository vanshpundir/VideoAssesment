from google.cloud import storage

# Replace these variables with your own values
bucket_name = "audio_file_data"  # Replace with your GCS bucket name
source_file_name = "/Users/vansh/Desktop/VideoAssesment/audio_files/2.wav"  # Replace with the path to your .wav file
destination_blob_name = "destination/folder/your-file.wav"  # Replace with the desired path and name in GCS


def upload_wav_to_gcs(bucket_name, source_file_name, destination_blob_name):
    try:
        # Initialize a GCS client
        storage_client = storage.Client()

        # Get the target bucket
        bucket = storage_client.bucket(bucket_name)

        # Upload the .wav file to GCS
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)

        # Get the URI for the uploaded file
        file_uri = f"gs://{bucket_name}/{destination_blob_name}"
        return file_uri

    except Exception as e:
        print("An error occurred:", str(e))
        return None


if __name__ == "__main__":
    file_uri = upload_wav_to_gcs(bucket_name, source_file_name, destination_blob_name)

    if file_uri:
        print("File uploaded successfully. URI:", file_uri)
    else:
        print("Upload failed.")
