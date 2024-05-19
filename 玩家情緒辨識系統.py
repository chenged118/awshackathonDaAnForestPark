#開攝影機 玩家情緒辨識
import cv2
import json
import boto3


cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if ret: #true代表有讀到下一幀
        frame=cv2.resize(frame,(0,0),fx=1,fy=1)
        cv2.imshow('Jumbo Affective Computing',frame) #將下一幀顯示出來
    else:
        break

    if cv2.waitKey(10) == ord('q'):
        break



######將人臉影像截圖後, 當作input傳遞給下面classification llm
# Initialize Boto3 clients for Lambda and SSM
lambda_client = boto3.client("lambda")
#ssm_client = boto3.client("ssm")


'''lambda_function_name_ssm_parameter = (
    "/AgenticLLMAssistantWorkshop/AgentExecutorLambdaNameParameter"
)'''

#lambda_function_name = ssm_client.get_parameter(Name=lambda_function_name_ssm_parameter)
lambda_function_name = 'AI_Agent_Johnny'


def call_agent_lambda(user_input, session_id):
    payload = {
        "question": user_input,
        "session_id": session_id,
        "clean_history": True
    }

    try:
        # Call the Lambda function
        lambda_response = lambda_client.invoke(
            FunctionName=lambda_function_name,
            InvocationType="RequestResponse",  # Use 'Event' for asynchronous invocation
            Payload=json.dumps(payload),
        )

        # Parse the Lambda function response
        lambda_result = lambda_response["Payload"].read().decode("utf-8")
        lambda_result = json.loads(lambda_result)

        return lambda_result
    except Exception as e:
        print(e)


session_id = "10"
user_input = "早安您好"

results = call_agent_lambda(user_input, session_id)

# 解析 Lambda 回應
response_body = json.loads(results['body'])

# 提取 "response" 部分
response_text = response_body['response']

print(response_text.strip())


