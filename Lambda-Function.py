import boto3
import json

print("Loading Function...")

def lambda_handler(event, context):
    # Initialize the Simple Email Service (SES) client in the specified AWS region
    # Make sure to replace 'eu-north-1' with your region!
    ses = boto3.client("ses", region_name="eu-north-1")

    # Define sender and recipient email addresses
    # CHANGE THESE to the emails you verified in Step 3!
    sender_email = 'abc@gmail.com'
    recipient_email = 'def@gmail.com'

    # Compose email subject and message
    subject = "Mass emailing with Lambda"
    message = "You are one of the many recipients of this email."

    # Send email with SES
    response = ses.send_email(
        Source=sender_email,
        Destination={'ToAddresses': [recipient_email]},
        Message={'Subject': {'Data': subject}, 'Body': {'Text': {'Data': message}}}
    )
    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Email sent successfully!'})
    }
