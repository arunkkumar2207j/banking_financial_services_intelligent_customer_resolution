# BankingFinancialServicesIntelligentCustomerResolution Crew

Welcome to the BankingFinancialServicesIntelligentCustomerResolution Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

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
banking_financial_services_intelligent_customer_resolution/
└── src/
    └── banking_financial_services_intelligent_customer_resolution/
        ├── main.py
        ├── crew.py
        ├── tools/
        ├── config/
```

---

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/banking_financial_services_intelligent_customer_resolution/config/agents.yaml` to define your agents
- Modify `src/banking_financial_services_intelligent_customer_resolution/config/tasks.yaml` to define your tasks
- Modify `src/banking_financial_services_intelligent_customer_resolution/crew.py` to add your own logic, tools and specific args
- Modify `src/banking_financial_services_intelligent_customer_resolution/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the banking-financial-services-intelligent-customer-resolution Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The banking-financial-services-intelligent-customer-resolution Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the BankingFinancialServicesIntelligentCustomerResolution Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
