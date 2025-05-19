from dotenv import load_dotenv
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import tool
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import render_text_description
from langchain_openai import ChatOpenAI


load_dotenv()
@tool
def get_text_length(text: str) -> int:
    """Returns the length of the input text by characters"""
    print(f"get_text_length has received : {text}")
    text = text.strip("\n").strip(
        '"'
    )
    return len(text)


@tool
def get_no_of_vowels_from_text(text: str) -> int:
    """Returns the number of vowels present in the text input"""
    print(f"get_no_of_vowels_from_text has received : {text}")

    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    c = 0
    for ch in text:
        if ch in v:
            c = c + 1

    return c


tools = [get_text_length, get_no_of_vowels_from_text]
llm = ChatOpenAI(temperature=0)


template = """
Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question
    Once you reach the final answer stop this process.

    Do not hallucinate on the questions. Think on the question that user provides.
    Begin!

    Question: {input}
    Thought: {agent_scratchpad}
"""

prompt = PromptTemplate.from_template(template=template).partial(
    tools = render_text_description(tools),
    tool_names= ",".join([t.name for t in tools])
)

agent = create_react_agent(
    tools = tools,
    llm =llm,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent= agent,
    tools = tools,
    handle_parsing_errors=True,
    verbose=True,
    max_iterations = 5
)


input = (
    "What is the number of vowels in peacock"
)

agent_executor.invoke({"input": input})