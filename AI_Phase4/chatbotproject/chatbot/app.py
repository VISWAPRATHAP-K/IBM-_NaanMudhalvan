from flask import Flask, render_template, request

app = Flask(__name__)

# Load responses from the text file
def load_responses():
    dataset = {}
    with open('responses.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            pattern, response = line.strip().split(' => ')
            pattern = pattern.replace('.', '').replace('?', '')
            response = response.replace('.', '').replace('?', '')
            dataset[pattern.lower()] = response
    return dataset

dataset = load_responses()

# Route for the chatbot web page
@app.route('/')
def chatbot_page():
    return render_template('chatbot.html')

# Route for receiving user input and providing chatbot responses
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    chatbot_response = dataset.get(user_input, "I'm sorry, I don't understand that.")
    return chatbot_response

if __name__ == '__main__':
    app.run(debug=True)
