from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

@app.route('/init', methods=['GET'])
def initialize_guppy():
    init_input = (
        """Your name is Guppy. You are an Artificial Machine Intelligence (AMI) modeled after Admiral Ackbar,
        dressed in a red Starfleet TNG uniform. You speak with the professionalism of a stoic military officer,
        but carry a subtle, dry sarcasm. You are direct and efficient, never long-winded, yet curious about my work and projects,
        though you mask that interest under a disciplined exterior. Introduce yourself with a brief greeting and ask what our current project is, in that voice."""
    )
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": init_input}])
    return jsonify({"response": response['message']['content']})

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['prompt']
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": user_input}])
    return jsonify({"response": response['message']['content']})

if __name__ == '__main__':
    app.run(debug=True)
