# ai_agent_mysql
 Build intelligent AI agents using LangChain and the ReAct algorithm! This project includes hands-on examples with simple tools and MySQL database integration. Ideal for GenAI developers and LLM enthusiasts.


# 🤖 Build AI Agents with LangChain – ReAct Algorithm + MySQL Integration

This repository contains hands-on examples demonstrating how to build intelligent **AI agents** using **LangChain** and the **ReAct (Reasoning + Acting)** algorithm.

You'll learn how to create agents that:
- Think step-by-step (Chain-of-Thought)
- Use tools to act in the real world
- Interact with external systems like **MySQL databases**

---

## 📌 What's Inside

### 🧠 1. Simple LangChain Agent with Custom Tools
- Create a LangChain agent with basic tools
- Define Python functions as tools and expose them via LangChain
- Use ReAct to let the agent reason and call tools dynamically

### 🗃️ 2. LangChain Agent with MySQL Integration
- Connect Python to a MySQL database
- Wrap MySQL queries in LangChain tools
- Let the agent fetch data from a real database using ReAct

---

## 📦 Tech Stack

- **Python 3.13+**
- **LangChain**
- **OpenAI API (or compatible LLM)**
- **MySQL**
- **MySQL Connector for Python**
- Optional: `python-dotenv` for managing environment variables

---
### 1. Clone the repo

```bash
git clone https://github.com/HiruInnovate/ai_agent_mysql.git
cd ai_agent_mysql
```

## 🚀 Getting Started

### Set up Environment

```bash
pipenv shell
pipenv install
```
###  Set your environment variables

Create a .env file with your OpenAI API key and MySQL credentials:
```text
OPENAI_API_KEY=your_openai_key
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=your_db
```
### Run the simple AI agent

```commandline
python main.py
```
### Run the Mysql AI agent

```commandline
python main_sql_tools.py
```

# About me
I am `Hiranmoy Goswami`, I am passionate about `AI/ML/DL` , `Generative AI applications` and their use in different domains, I also love to build `web applications` using `Java, React`, I have backend development experience with Java[Microservices]. For any work, you can reach out to me at...

* [LinkedIn](https://www.linkedin.com/in/hiranmoy-goswami-1997-dev/)
* [Youtube](https://www.youtube.com/channel/UCzQ9e6BsI1XiBWD3wlBRfrQ)