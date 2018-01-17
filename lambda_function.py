import json
import urllib.parse
import boto3
from botocore.exceptions
import ClientError

# Create a new SES resource and specify a region.

def lambda_handler(event, context): #print("Received event: " + json.dumps(event, indent = 2))

# Get the object from the event and show its content type
bucket = event['Records'][0]['s3']['bucket']['name']
key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding = 'utf-8')
try: #response = s3.get_object(Bucket = bucket, Key = key)
print("Received event from s3 bucket ")# Try to send the email.

s3 = boto3.client('s3')

SENDER = "<sender@example.com>"
RECIPIENT = "<receiver@example.com>"
SUBJECT = "Amazon SES Test (SDK for Python)"
AWS_REGION = "us-east-1"
BODY_TEXT = ("Amazon SES Test (Python)\r\n"
  "This email was sent with Amazon SES using the "
  "AWS SDK for Python (Boto)."
)

# The character encoding
for the email.
CHARSET = "UTF-8"

#
The HTML body of the email.
BODY_HTML = ""
"<html> < head > < /head> < body >
  < h1 > Amazon SES Test(SDK
    for Python) < /h1> < p > This email was sent with < a href = 'https://aws.amazon.com/ses/' > Amazon SES < /a> using the < a href = 'https://aws.amazon.com/sdk-for-python/' >
  AWS SDK
for Python(Boto) < /a>.</p >
  < /body> < /html>
""
"
client = boto3.client('ses', region_name = AWS_REGION)
response = client.send_email(
  Destination = {
    'ToAddresses': [
      RECIPIENT,
    ],
  },
  Message = {
    'Body': {
      'Html': {
        'Charset': CHARSET,
        'Data': BODY_HTML,
      },
      'Text': {
        'Charset': CHARSET,
        'Data': BODY_TEXT,
      },
    },
    'Subject': {
      'Charset': CHARSET,
      'Data': SUBJECT,
    },
  },
  Source = SENDER, #If you are not using a configuration set, comment or delete the# following line# ConfigurationSetName = CONFIGURATION_SET,
)

print("Email sent! Message ID:"),
  print(response['ResponseMetadata']['RequestId'])
return
except ClientError as e:
  print(e.response['Error']['Message'])
except Exception as e:
  print(e)
print(
  'Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(
    key, bucket))
raise e
