import sqlite3

def init_db():
    try:
        conn = sqlite3.connect('chat_data.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_input TEXT NOT NULL,
                response_1 TEXT,
                response_2 TEXT,
                response_3 TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def save_chat(user_input, responses):
    try:
        conn = sqlite3.connect('chat_data.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO chat_history (user_input, response_1, response_2, response_3)
            VALUES (?, ?, ?, ?)
        ''', (user_input, responses[0], responses[1], responses[2]))
        conn.commit()
        print("Chat saved successfully!")
    except Exception as e:
        print(f"Error saving chat: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
