import openai

# OpenAI API 키 설정
openai.api_key =

def get_response(user_input):
    try:
        # 최신 API 인터페이스 사용
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 또는 사용하려는 모델 이름
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

# 테스트
if __name__ == "__main__":
    user_message = "안녕하세요, 오늘 날씨는 어떤가요?"
    print(get_response(user_message))
