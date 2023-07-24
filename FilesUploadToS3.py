import os
import paramiko
import boto3


SFTP_HOST = 'sftp.example.com'
SFTP_PORT = 22
SFTP_USERNAME = 'sftp_user'
SFTP_PASSWORD = 'sftp_password'
SFTP_DIRECTORY = '/path/to/sftp_directory'

AWS_REGION = 'eu-west-1'
S3_BUCKET_NAME = 'your-s3-bucket-name'

sftp_client = paramiko.Transport((SFTP_HOST, SFTP_PORT))
sftp_client.connect(username=SFTP_USERNAME, password=SFTP_PASSWORD)
sftp = sftp_client.open_sftp()

s3 = boto3.client('s3', region_name=AWS_REGION)

for filename in sftp.listdir(SFTP_DIRECTORY):
    file_path = os.path.join(SFTP_DIRECTORY, filename)
   
    # Check file type and size
    file_extension = os.path.splitext(filename)[1].lower()
    file_size = sftp.stat(file_path).st_size
   
    if file_extension in ['.csv', '.xlsx', '.json'] and 20 * 1024 <= file_size <= 50 * 1024 * 1024:
        # Upload file to S3
        s3.upload_file(file_path, S3_BUCKET_NAME, filename)
        print(f"File '{filename}' uploaded to S3")

sftp.close()
sftp_client.close()
