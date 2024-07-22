import boto3
import time

# Configuration
bucket_name = 'your-bucket-name'
region_name = 'us-east-1'  # Change to your Linode Object Storage region
access_key = 'YOUR_LINODE_ACCESS_KEY'
secret_key = 'YOUR_LINODE_SECRET_KEY'
endpoint_url = 'https://[your-cluster-identifier].linodeobjects.com'  # Replace with your cluster's endpoint URL
scan_interval = 10  # Time in seconds between scans

# Initialize boto3 client with Linode credentials and custom endpoint
s3_client = boto3.client(
    's3',
    region_name=region_name,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    endpoint_url=endpoint_url
)

def list_files():
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        return [item['Key'] for item in response['Contents']]
    return []

def main():
    print("Starting the watch folder script...")
    known_files = set(list_files())
    print(f"Initial files: {known_files}")

    while True:
        current_files = set(list_files())
        new_files = current_files - known_files

        if new_files:
            for new_file in new_files:
                print(f"New file added: {new_file}")

            known_files = current_files

        time.sleep(scan_interval)

if __name__ == "__main__":
    main()
