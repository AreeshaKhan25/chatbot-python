import json

# Load the FAQ data
with open("faq.json", "r") as file:
    faq_data = json.load(file)

# Keyword mapping
keyword_map = {
    "services": "services",
    "offer": "services",
    "price": "pricing",
    "cost": "pricing",
    "start": "getting_started",
    "begin": "getting_started",
    "platform": "platforms",
    "timeline": "timeline",
    "time": "timeline",
    "team": "team",
    "technologies": "technologies",
    "tech": "technologies",
    "support": "maintenance",
    "maintenance": "maintenance",
    "nda": "nda",
    "confidential": "nda",
    "industries": "industries",
    "domain": "industries",
    "contact": "contact",
    "email": "contact",
    "hello": "hello",
    "hi": "hello",
    "thanks": "thank_you",
    "thank you": "thank_you"
}

# Fallback responses
fallbacks = [
    "Sorry, I didn’t understand that. Can you rephrase it?",
    "Hmm, I'm not sure about that. Could you clarify your question?",
    "I'm still learning. Could you provide more details?"
]

# Clarification questions
clarifications = [
    "Do you need a mobile, web, or desktop solution?",
    "Can you tell me more about your business type?"
]

import random

def get_response(user_input):
    user_input = user_input.lower()
    
    # Keyword matching
    for keyword in keyword_map:
        if keyword in user_input:
            key = keyword_map[keyword]
            return faq_data.get(key)
    
    # Clarification if vague
    vague_words = ["project", "software", "develop", "build"]
    if any(word in user_input for word in vague_words):
        return random.choice(clarifications)
    
    return random.choice(fallbacks)

# Greeting
print("🤖 ChatBot: Hello! I'm your virtual assistant. Ask me anything about our software services.")
print("Type 'exit' to end the chat.\n")

# Main loop
while True:
    user = input("You: ")
    if user.strip().lower() in ["exit", "quit", "bye"]:
        print("🤖 ChatBot: Thank you for chatting! Have a great day.")
        break
    response = get_response(user)
    print("🤖 ChatBot:", response)
