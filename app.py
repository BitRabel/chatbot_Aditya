from flask import Flask, request, jsonify
from chatbots import chatbots

app = Flask(__name__)
chatbots = chatbots()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message')
    reply = chatbots.chatbots_response(user_input)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Use port 5001 to avoid conflicts
