import json
import boto3


def lambda_handler(event, context):

    client = boto3.client('s3')
    client.download_file('dexter6242', 'key.txt', '/tmp/newkey.txt')
    with open('/tmp/newkey.txt','r+') as f:
         x= f.readlines()
    print x     
    return {
        'statusCode': 200,
        'body': json.dumps(x)
    }
