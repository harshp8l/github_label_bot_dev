import os
import boto3
import json
from pprint import pprint

SQS_CLIENT = boto3.client('sqs')

def start(event, context):
    """
    First Lambda Function
    :param event: AWS event data
    :param context: AWS function's event
    """
    
    # Grabbing only necessary event information to send
    # data = json.loads(str(event))['repository']['html_url']

    print(SQS_CLIENT.send_message(
        QueueUrl=os.getenv('SQS_URL'),
        MessageBody = str(event)
    ))


    # Successful response -- assuming message will be sent correctly
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json"},
        "body":'Success' 
    }

def end(event, context):
    """
    Second Lambda Function
    :param event: AWS event data(from SQS)
    :param event: AWS function's context
    """

    print(event)
    return ''
