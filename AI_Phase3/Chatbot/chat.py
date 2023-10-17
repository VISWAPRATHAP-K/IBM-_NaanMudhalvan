import random

# Load the dataset from the text file
def load_dataset(file_path):
    dataset = {}
    with open('dialogs.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            pattern, response = line.strip().split(' => ')
            pattern = pattern.replace('.', '').replace('?', '')
            response = response.replace('.', '').replace('?', '')
            dataset[pattern.lower()] = response
    return dataset

# Generate a response based on user input
def chatbot_response(user_input, dataset):
    user_input = user_input.lower()
    response = dataset.get(user_input, "I'm sorry,don't understand that.")
    return response

# Main loop to interact with the chatbot
def main():
    file_path = 'dialogs.txt'
    dataset = load_dataset(file_path)

    print("Chatbot: Hello! How can I help you? (Type 'exit' to end)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot_response(user_input, dataset)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
