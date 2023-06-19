import boto3

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id='xxxxxxxxxxxxxxxxxxxxxxxx',
    aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    region_name='xxxxxxx'
)

# Create a DynamoDB client
dynamodb = session.client('dynamodb')

# Define the table name
table_name = 'practice'

# Define the query parameters
query_params = {
    'TableName': table_name,
    'KeyConditionExpression': '#id = :id_value',
    'ExpressionAttributeNames': {
        '#id': 'id'
    },
    'ExpressionAttributeValues': {
        ':id_value': {'N': '1'}
    }
}

# Perform the query
response = dynamodb.query(**query_params)

# Print the results
for item in response['Items']:
    print(item)