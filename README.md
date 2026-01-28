# Banking & Financial Services – Intelligent Customer Resolution (Multi-Agent System)

This project implements an **Agentic AI system using CrewAI** to intelligently handle customer issues in the Banking & Financial Services domain.  
The system simulates how a real bank resolves customer problems such as:

- Failed transactions  
- Card issues  
- Fraud / suspicious activity  
- Loan inquiries  
- Compliance-sensitive requests  

The architecture is based on **multiple specialized AI agents** collaborating in a structured workflow.

---

## 🧠 Agentic Architecture

The system consists of the following agents:

1. **Intent Detection Agent** – Identifies the type of customer issue.  
2. **Risk & Compliance Agent** – Assesses regulatory and fraud risk.  
3. **Knowledge Retrieval Agent** – Fetches banking policies and RBI rules.  
4. **Resolution Agent** – Determines safe operational actions.  
5. **Communication Agent** – Generates polite, compliant responses.  
6. **Escalation Agent** – Prepares cases for human review when risk is high.

Execution Flow:  
Intent → Risk → Knowledge → Resolution → Communication → Escalation

---

## 📁 Project Structure

```
week_12_graded_mini_project/
└── src/
    └── week_12_graded_mini_project/
        ├── main.py
        ├── crew.py
        ├── agents/
        ├── tools/
        ├── prompts/
        ├── memory/
        ├── config/
        └── orchastrator/
```

---

## ⚙️ Installation

### Python Version
Use **Python 3.11.x** (CrewAI is not fully compatible with Python 3.13 on Windows).

### Create Virtual Environment
```bash
py -3.11 -m venv venv
venv\Scripts\activate
```

### Install Dependencies
```bash
pip install crewai[tools]==1.8.1 python-dotenv
```

### Configure API Key
Create `.env` file in project root:

```
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL_NAME=gpt-4o-mini
```

---

## ▶️ Running the Project

```bash
set PYTHONPATH=src
python src/week_12_graded_mini_project/main.py
```

---

## 🎓 Academic Value

This project demonstrates:

- Multi-Agent AI architecture  
- Agentic workflow orchestration  
- Banking domain risk & compliance modeling  
- Human-in-the-loop escalation  
- Prompt modularization  
- Real-world BFSI use case implementation

---

## 📌 Viva One-Liner

> “This system models a real banking customer support center using multiple specialized AI agents orchestrated by CrewAI, ensuring safe, compliant, and accurate customer resolution.”
