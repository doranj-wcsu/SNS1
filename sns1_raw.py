import boto3

"""
class boto3.session.Session(aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, region_name=None, botocore_session=None, profile_name=None)[source]
A session stores configuration state and allows you to create service clients and resources.
"""

client = boto3.client(
        "sns",
        aws_access_key_id="xxx",
        aws_secret_access_key="xxxxxxxx",
        region_name="us-east-1")



response = client.create_topic(Name="topic_name")
topic_arn = response["TopicArn"]

"""
<CreateTopicResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <CreateTopicResult>
        <TopicArn>arn:aws:sns:us-east-2:123456789012:My-Topic</TopicArn>
    </CreateTopicResult>
    <ResponseMetadata>
        <RequestId>a8dec8b3-33a4-11df-8963-01868b7c937a</RequestId>
    </ResponseMetadata>
</CreateTopicResponse>
"""



response = client.subscribe(TopicArn=topic_arn, Protocol="Email", Endpoint="doranj@wcsu.edu")
subscription_arn = response["SubscriptionArn"]




# Publish to topic
client.publish(TopicArn=topic_arn, 
            Message="Chicken or Fish for Lunch !", 
            Subject="subject is used Emails")




# List all subscriptions
response = client.list_subscriptions()
subscriptions = response["Subscriptions"]
print ( subscriptions ) 



topics = client.list_topics().get('Topics')

for topic in topics:
    subscriptions = client.list_subscriptions_by_topic(TopicArn=topic.get('TopicArn')).get('Subscriptions')
    for subscription in subscriptions:
        print(subscription.get('SubscriptionArn'))
        print(subscription.get('Endpoint'))



        
print ("Finished")
#sys.exit("Finished")   
        
