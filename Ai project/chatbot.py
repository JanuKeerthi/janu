# chatbot.py

# Importing necessary libraries
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK datasets
nltk.download('punkt')
nltk.download('stopwords')

# Load spaCy's English language model
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("Please download the 'en_core_web_sm' language model by running:")
    print("python -m spacy download en_core_web_sm")
    exit()

# Define a set of English stopwords
stop_words = set(stopwords.words('english'))

# Step 1: Text Preprocessing function
def preprocess(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    # Convert to lowercase and filter out non-alphabetic tokens
    tokens = [word.lower() for word in tokens if word.isalpha()]
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Step 2: Intent Recognition function using keyword matching
def recognize_intent(user_input):
    greeting_keywords = ["hi", "hello", "hii", "hey", "greetings"]
    farewell_keywords = ["bye", "goodbye", "see you", "farewell"]
    question_keywords = ["what", "how", "why", "can", "do", "does"]

    # Convert user input to lowercase for case-insensitive matching
    lower_input = user_input.lower()

    # Check for greetings
    if any(word in lower_input for word in greeting_keywords):
        return "greeting"
    # Check for farewells
    elif any(word in lower_input for word in farewell_keywords):
        return "farewell"
    # Check for questions
    elif any(word in lower_input for word in question_keywords):
        return "question"
    else:
        return "unknown"

# Step 3: Response Generation function
responses = {
  
    "greeting": "Hello! janu How can I help you today?",
    "farewell": "Goodbye! Have a great day!",
    "question": "That's a good question. Let me think...",
    "unknown": "I'm not sure what you mean. Can you clarify?"
}

def generate_response(intent):
    # Return a response based on the identified intent
    return responses.get(intent, "I don't understand.")

# Step 4: Chat function to interact with the user
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        # Exit if the user says 'bye'
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        # Recognize the intent of the user input
        intent = recognize_intent(user_input)
        # Generate a response based on the recognized intent
        response = generate_response(intent)
        # Display the response
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
