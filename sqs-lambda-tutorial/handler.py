import os
import boto3

SQS_CLIENT = boto3.client('sqs')

def start(event, context):
    """
    First Lambda Function
    :param event: AWS event data
    :param context: AWS function's event
    """
    print(SQS_CLIENT.send_message(
        QueueUrl=os.getenv('SQS_URL'),
        MessageBody = 'test'
    ))
    return ''

def end(event, context):
    """
    Second Lambda Function
    :param event: AWS event data(from SQS)
    :param event: AWS function's context
    """
    print(event)
    return ''

