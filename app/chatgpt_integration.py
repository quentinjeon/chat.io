import openai

# OpenAI API 키 설정
openai.api_key = ;

'''def get_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 또는 사용 중인 모델 이름
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        # 에러 메시지를 반환하여 디버깅
        return f"Error: {str(e)}"
        '''
def get_responses(user_input, n=3):
    """
    사용자 입력에 대해 ChatGPT의 예상 응답 3개를 생성
    """
    try:
        # API 호출
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
            n=n,  # 응답 개수 설정
            max_tokens=100  # 생성할 응답의 길이 제한
        )
        # 응답 리스트 추출
        responses = [choice['message']['content'] for choice in response['choices']]
        return responses
    except Exception as e:
        return [f"Error: {str(e)}"] * n