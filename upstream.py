import json
import boto3

class Upstream:

    def __init__(self, message):
        self.message = message
        filename = "message.json"
        try:
          f = open(filename, 'w')
          f.write(self.message.toJSON())
          f.close()
          self.send()
        except IOError:
            print("Could not write file: %s" % filename)

    def send(self):

        # Create SQS client
        sqs = boto3.client('sqs')

        queue_url = 'http://sqs.aws.com'

        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageGroupId="None",
            MessageBody=(self.message.toJSON())
        )

        print(response['MessageId'])