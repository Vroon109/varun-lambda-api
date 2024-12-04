import json

def lambda_handler(event, context):
    # Get query parameters from the event
    query_params = event.get("queryStringParameters", {})
    name = query_params.get("name", "World")

    # Return a JSON response
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": f"Hello, {name}!"}), 
    }
