import boto3
import os, json
from dotenv import load_dotenv

def send_email(email, content):
    load_dotenv()
    ses_client = boto3.client(
        'ses',
        region_name='ap-south-1', 
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
    )
    email_message = {
    'Subject': {
        'Data': 'Summary of the github repo pull requests you requested!'
    },
    'Body': {
        'Text': {
            'Data': 'Here\'s the latest 5 pull request this week with user\'s name and summary \n'
            }
        }
    }
    for i, pr in enumerate(content):
        if i<5:
            print(i, pr)
            email_message['Body']['Text']['Data'] += f"\n Name : {pr['name']} ---- Title of the pr: {pr['title']}"
        else:
            break
    email_json = json.dumps(email_message)

    response = ses_client.send_email(
    Source='srikarsrivatsavvs@gmail.com',
    Destination={
        'ToAddresses': [email]
    },
    Message={
        'Subject': {
            'Data': email_message['Subject']['Data']
        },
        'Body': {
            'Text': {
                'Data': f"{email_message['Body']['Text']['Data']} \
                \n \n For the entire PR data of last week, please check the api response through Postman! \
                \n \
                \n Thanks!"
            }
        }
    }
    )