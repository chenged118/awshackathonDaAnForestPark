import boto3
import json

client = boto3.client(service_name='bedrock-runtime')

def lambda_handler(event, context):
    try:
        # 檢查 event 中是否存在用戶問題
        user_question = event['question']
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid request body: Missing question'}),
            'headers': {'Content-Type': 'application/json'}
        }

    # 設置請求內容
    body = json.dumps({
        "prompt": f"\n\nHuman: {user_question}\n\nAssistant:",
        "max_tokens_to_sample": 3000,
        "temperature": 0.9,
        "top_p": 0.9,
    })

    modelId = 'anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'

    try:
        # 調用模型
        response = client.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

        response_body = json.loads(response['body'].read().decode('utf-8'))

        # 提取回應文本
        completion = response_body.get('completion')
        
        return {
            'statusCode': 200,
            'body': json.dumps({'response': completion}, ensure_ascii=False),
            'headers': {'Content-Type': 'application/json'}
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }
