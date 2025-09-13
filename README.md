# Swasthya-Setu: An AI-Driven Public Health Assistant for India 🇮🇳

![Project Banner](https://img.shields.io/badge/SIH2025-Public_Health_Assistant-blue.svg)
![Rasa Version](https://img.shields.io/badge/Rasa-3.x-orange.svg)
![Python Version](https://img.shields.io/badge/Python-3.9-green.svg)
![Status](https://img.shields.io/badge/Status-Production_Ready-brightgreen.svg)

---

**Swasthya-Setu is a state-of-the-art, multilingual conversational AI platform designed to provide every citizen of India with instant, reliable, and accessible information on disease awareness, vaccination schedules, and emergency health services.**

Built for the **Smart India Hackathon**, this project is not merely a prototype. It is a robust, scalable, and secure system architected on the Rasa framework, ready for real-world deployment and integration with national public health initiatives. It is designed to function seamlessly online with live APIs and offline with a comprehensive, multi-layered knowledge base, ensuring 100% uptime and reliability.

## 🚀 Core Features

*   **Intelligent Dialogue Management:** Employs a unique **"Intelligent Gatekeeper"** architecture that provides fast, predictable responses for critical tasks while using a deep knowledge base for informational queries.
*   **Deep Multilingual Support:** The NLU model is expertly trained on a rich dataset covering **English, Hindi, Odia, and Hinglish**, designed to understand the nuances of real user conversations.
*   **Robust Multi-Turn Conversations:** Utilizes a stateful, Python-driven logic to manage complex, multi-step tasks like finding a vaccination schedule or emergency contact, without losing context or frustrating the user.
*   **Multi-Layered Fallback System:** Guarantees that no query ever results in a "dead end." If a user's question is not a high-confidence trained task, it is intelligently triaged through:
    1.  **A Semantic Knowledge Base:** For understanding the meaning behind questions.
    2.  **A Health Glossary:** for quick definitions of medical terms.
    3.  **An Intelligent Geo-Fallback:** For providing district-level emergency information for any pincode in Odisha.
*   **Production & Cloud Ready:** Architected with best practices for security, scalability, and deployment on platforms like WhatsApp via Twilio.

---

## 🏛️ System Architecture: The "Intelligent Gatekeeper" Model

The chatbot's core logic is built on a powerful hybrid model that combines the strengths of machine learning for understanding and explicit rules and code for predictable, safe decision-making. Every user query is intelligently routed down one of two paths.

![Swasthya-Setu Chatbot Architecture Flowchart](https://res.cloudinary.com/dwwihknne/image/upload/v1757409555/swasthya-setu_diagram_cl1kdu.png)

### **Path A: The "Express Lane" (High-Confidence Tasks)**
This path is for queries that the NLU model recognizes with very high confidence (>85%). These are critical, structured tasks that require immediate and predictable action.

1.  **High-Confidence NLU:** An intent like `ask_vaccination_schedule` is detected.
2.  **Unambiguous Rule:** `rules.yml` contains a specific, high-priority rule that immediately triggers a **Rasa Form** (`vaccination_form`).
3.  **Code-Driven Logic:** The `actions.py` file takes control via its `FormValidationAction` classes. The Python code manages the multi-step conversation, asking for `age` and `location`, handling user interruptions, and providing the final answer. This path is fast, efficient, and 100% reliable.

### **Path B: The "Smart Triage & Knowledge Lane" (Lower-Confidence & Informational Queries)**
This path is for any query that is not a high-confidence structured task. It is the default path for all informational questions.

1.  **Default Rule Trigger:** A general, lower-priority rule in `rules.yml` activates for all other known intents (e.g., `ask_symptoms`, `greet`, etc.), triggering a single, master Python action.
2.  **Master Knowledge Action:** The `ActionKnowledgeSearch` function in `actions.py` takes control. This action orchestrates the entire knowledge cascade:
    *   **Pincode Pre-Check:** It first checks if the user's message is a standalone 6-digit number and routes it to the emergency form if so.
    *   **Layer 1 - Semantic KB:** It performs a semantic search against the WHO/MoHFW-sourced Q&A database.
    *   **Layer 2 - Health Glossary:** If the semantic search fails, it looks for keywords like "ORS" or "BCG".
    *   **Layer 3 - Static NLU Fallback:** If both KBs fail, it checks the original NLU intent to see if there is a pre-written static answer (e.g., `utter_symptoms_tuberculosis`).
    *   **Layer 4 - Final Safety Net:** If all else fails, it delivers the final, generic `utter_fallback` message.

---

## 🔧 Technical Specifications & Setup

This project uses a standard Rasa Open Source stack with a powerful, code-driven dialogue management system.

### **Prerequisites**
*   Python 3.9
*   Pip
*   A Python virtual environment (`venv`)

### **1. Clone the Repository**
```bash
git clone https://your-repo-url/swasthya-setu.git
cd swasthya-setu
````
### **2. Create Environment & Install Dependencies**
The requirements.txt file contains a locked, known-stable set of all required libraries to ensure a conflict-free setup.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
The first time you install, it will download several large machine learning models. This is expected.

### **3. Train the Rasa Model**
This command trains both the NLU model (for understanding) and the Dialogue model (for decision-making) based on our perfected YAML files.

```bash
rasa train
```

### **4. Run the Chatbot**
The system requires two terminals to run simultaneously: the Rasa Server and the Action Server.

**In Terminal 1 (Action Server):**
This terminal runs your custom Python logic (actions.py), including the knowledge bases and form management.
```bash
rasa run actions
````

**In Terminal 2 (Medicine Server):**
This terminal runs your custom Python logic (actions.py), including the knowledge bases and form management.
```bash
python3 -m uvicorn services.medicine_api.main:app
````

**In Terminal 3 (Multilingual + Grammar Server):**
This terminal runs your custom Python logic (actions.py), including the knowledge bases and form management.
```bash
service.app:app --host 0.0.0.0 --port 8001
````

**In Terminal 2 (Rasa Server & Shell):**
This terminal runs the core Rasa model and allows you to chat with the bot on the command line.
```bash
rasa shell
```

**You can now interact with the Swasthya-Setu assistant!**

### **This project is ready to serve as the foundation for a scalable and life-saving public health information service for India.**
