import boto3

def lambda_handler(event, context):
    sns = boto3.client('sns')
    
    response = sns.publish(
        TopicArn='arn:aws:sns:ap-south-1:917186636831:SecurityAlertsTopic',
        Subject='🚨 AWS Security Alert Detected',
        Message='A suspicious activity was detected in your AWS environment.\n\nDetails:\n' + str(event)
    )
    
    print("✅ Alert sent to SNS. Event details:", event)

    return {
        'statusCode': 200,
        'body': 'Alert sent!'
    }
