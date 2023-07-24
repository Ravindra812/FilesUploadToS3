# File Upload Service Using Python 
This is a Python script that provides a secure file upload service using the SFTP (SSH File Transfer Protocol) protocol. The script allows agencies to upload files of types CSV, Excel, and JSON to a remote SFTP server. Each agency can upload multiple files in each batch, making the process efficient and scalable. The service supports agencies in different geographical locations, handling potential network latency issues gracefully. Additionally, to simplify management, all agencies share the same SFTP user.

# Requirements
Python 3.x
boto3 library (for AWS S3 interactions)

paramiko library (for SFTP)

# Getting Started
Clone this repository to your local machine.

pip install boto3 paramiko

Replace the placeholder values in the script with your actual SFTP server credentials: SFTP_HOST, SFTP_PORT, SFTP_USERNAME, and SFTP_PASSWORD.

Set up an AWS S3 bucket to store the uploaded files and configure the necessary IAM roles and policies for S3 access. Replace S3_BUCKET_NAME with the actual name of your S3 bucket.

# Note
Make sure you have the necessary permissions and credentials to access the SFTP server and upload files.

The script uses the paramiko library for SFTP interactions and the boto3 library for interacting with AWS S3, ensuring secure and efficient file transfer.
