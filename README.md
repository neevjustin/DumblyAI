# DumblyAI 🎯

## Basic Details  
**Team Name:** Anti-Belly

### Team Members
- **Team Lead:** Neev Justin – TKMCE  

---

## Project Description
DumblyAI is a web-based chatbot that gives interntional dumb answers using state-of-the-art AI models and reverse-engineered prompt logic.
Designed to make users feel smarter, it delivers hilariously incorrect replies in a professional, chatbot-style interface — like ChatGPT, but proudly dumb.

---

## The Problem (that doesn't exist)

In the age of advanced AI, people have stopped feeling smart.
Every question we ask is answered instantly — and perfectly — by machines. There’s no hesitation. No "I think." No "maybe." Just cold, hard, correct answers.

The result?
Humans feel stupid. Powerless. Replaced.
We can’t flex our general knowledge anymore because ChatGPT and Gemini already know it all — and better.

We’re not just losing trivia nights…
We’re losing our confidence.

---

## The Solution (that nobody asked for)

Introducing **DumblyAI** — the world’s first intellectually humbling AI.
It doesn't just make mistakes — it makes them boldly.

Powered by cutting-edge models and expertly degraded using precision prompt-engineering, DumblyAI delivers answers that are spectacularly wrong, yet beautifully confident.

Now, for once, you know more than the bot.
You are the genius.
You are right.
Let DumblyAI be wrong — so you don’t have to be.

---

## Technical Details

### Technologies/Components Used  

- **Languages used:** Python, JavaScript  
- **Frameworks used:** FastAPI, React  
- **Libraries used:**  
  - `google-generativeai` (Gemini API)  
  - `uvicorn`  
  - `fastapi`  
  - `dotenv`  
  - Tailwind CSS  
- **Tools used:**  
  - Render (Backend Hosting)  
  - React  
  - GitHub  


### Implementation

#### 🧠 Backend (FastAPI)
- Exposes a single POST endpoint `/respond` using FastAPI.
- Uses Gemini Pro via `google-generativeai` to generate confidently wrong responses.
- Hosted on Render at: `https://dumblyai.onrender.com/respond`.

#### 💬 Frontend (React)
- Built using Bolt.new with React and Tailwind CSS.
- Minimal, dark-mode chat interface similar to ChatGPT.
- Sends user input to the backend and displays replies in a scrollable chat layout.

---


## Installation
#### Backend (FastAPI)
```bash
# 1. Clone the repository
git clone https://github.com/neevjustin/DumblyAI.git
cd backend
# 2. (Optional but recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate        
# On Windows: venv\Scripts\activate

# 3. Install required packages
pip install -r requirements.txt

# 4. Create a .env file and add your Gemini API key
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env

```
#### Frontend (React)
```bash
npm install
```
---


## Run
#### Backend
```bash
# Start the FastAPI backend with Uvicorn
uvicorn dumbly_backend:app --reload --port 8000
```

#### Frontend 
```bash
cd frontend
npm run dev
```
Runs on: http://localhost:5173 (or as shown in terminal)

---

### Project Documentation
For Software:

---
# Screenshots
![screenshot1](image-1.png)
*Landing Page*

![Screenshot2](image-2.png)
*Thinking*

![Screenshot3](image.png)
*Gives dumb responses gaslighting users think they are smarter*


---
# Diagrams

![alt text](unnamed.png)
*This diagram illustrates the architecture of DumblyAI, showcasing the flow from the React frontend, through the FastAPI backend, to the Google Gemini Pro API for generating intentionally incorrect responses.*

---


## Team Contributions
- Neev Justin: Everything

---
