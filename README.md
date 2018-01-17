
This simple script written in Python can be used to send an email whenever a file gets changed/uploaded to configured bucket.

Configure s3 event to trigger lambda ->https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-using-sdk-python.html

Steps to run: 
1. Configure this lambda to s3 bucket
2. Create IAM role which must have default s3 and ses access.
3. Verify email Ids (From and To both) on AWS SES sandbox.
