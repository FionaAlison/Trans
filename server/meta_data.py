import boto3

def fetch_instance_metadata(metadata_key):
    ec2_client = boto3.client('ec2')
    instance_id = ec2_client.instance_id
    metadata = ec2_client.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]['Metadata'][metadata_key]
    return metadata

# Get instance public DNS name and IP address using boto3
host = fetch_instance_metadata('public-hostname')
ip = fetch_instance_metadata('local-ipv4')

print("Public DNS Name:", public_hostname)
print("Local IP Address:", local_ipv4)
# Other static configurations
port = 8080
buffer_size = 1024
cwd = '/'.join(__file__.split("/")[:-1])
