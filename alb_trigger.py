import json
import boto3
import logging

elbList = boto3.client('elb')
ec2 = boto3.resource('ec2')
bals = elbList.describe_load_balancers()
print(bals)


logger = logging.getLogger()
logger.setLevel(logging.INFO)
client = boto3.client('sns')
def lambda_handler(event, context):
    # TODO implement
    #topic_arn = 'arn:aws:sns:us-east-2:521845138489:vignesh-alb' 
    #message = event
    #client.publish(TopicArn=topic_arn,Message=message)
    eventName = event['detail']['eventName']
    if (eventName == 'CreateLoadBalancer'):
          logger.info(event['detail']['userIdentity']['accountId'])
          logger.info(event['detail']['awsRegion'])
    if (eventName == 'DeleteLoadBalancer'):
          elbList = boto3.client('elb')
          ec2 = boto3.resource('ec2')
          bals = elbList.describe_load_balancers()
          list1 = []
          for elb in bals['LoadBalancerDescriptions']:
            list1.append(elb['LoadBalancerName'])
            print(len(list1), list1)
