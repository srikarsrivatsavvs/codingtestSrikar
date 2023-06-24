import boto3
import os
from dotenv import load_dotenv

def send_email(email, content):
    load_dotenv()
    ses_client = boto3.client(
        'ses',
        region_name='ap-south-1', 
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
    )
    response = ses_client.send_email(
    Source='srikarsrivatsavvs@gmail.com',
    Destination={
        'ToAddresses': [email]
    },
    Message={
        'Subject': {
            'Data': 'Summary of the github repo pull requests you requested!'
        },
        'Body': {
            'Text': {
                'Data': str(content)
            }
        }
    }
    )
    return response