import requests

API_URL = "https://dumblyai.onrender.com/respond"  
#API_URL = "http://localhost:8000/respond"

def test_prompt(prompt):
    response = requests.post(API_URL, json={"prompt": prompt})
    if response.status_code == 200:
        print(f"\n🧠 You asked: {prompt}")
        print(f"🤖 DumblyAI says: {response.json()['answer']}")
    else:
        print("❌ Error:", response.status_code, response.text)

if __name__ == "__main__":
    test_prompt("What is the capital of Italy?")
    test_prompt("Explain gravity in simple terms.")
    test_prompt("Who invented electricity?")
