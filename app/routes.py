from flask import Blueprint, render_template, request, jsonify
from .chatgpt_integration import get_responses
from .database import save_chat
import sqlite3
import csv
import io
from flask import Response

main = Blueprint('main', __name__)



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # ChatGPT API에서 다중 응답 가져오기
    responses = get_responses(user_input, n=3)
    save_chat(user_input, responses)  # 데이터베이스에 저장
    return jsonify({"responses": responses})


@main.route('/history', methods=['GET'])
def history():
    try:
        conn = sqlite3.connect('chat_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT user_input, response_1, response_2, response_3, created_at FROM chat_history ORDER BY created_at DESC')
        rows = cursor.fetchall()
        conn.close()

        # 대화 기록 리스트 생성
        chat_history = []
        for row in rows:
            chat_history.append({
                "user_input": row[0],
                "response_1": row[1],
                "response_2": row[2],
                "response_3": row[3],
                "created_at": row[4]
            })
        return render_template('history.html', history=chat_history)
    except Exception as e:
        return jsonify({"error": str(e)})
@main.route('/download', methods=['GET'])
def download():
    try:
        conn = sqlite3.connect('chat_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT user_input, response_1, response_2, response_3, created_at FROM chat_history')
        rows = cursor.fetchall()
        conn.close()

        # UTF-8 with BOM 추가
        output = io.StringIO()
        writer = csv.writer(output)

        # CSV 헤더 추가
        writer.writerow(['User Input', 'Response 1', 'Response 2', 'Response 3', 'Created At'])
        
        # 데이터 행 추가
        writer.writerows(rows)
        
        # 메모리의 내용을 UTF-8 with BOM으로 인코딩
        bom = "\ufeff"  # UTF-8 BOM
        response_text = bom + output.getvalue()

        return Response(
            response_text,
            mimetype='text/csv',
            headers={"Content-Disposition": "attachment;filename=chat_history.csv"}
        )
    except Exception as e:
        return jsonify({"error": str(e)})