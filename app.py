import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import tool
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
client = TavilyClient(api_key=TAVILY_API_KEY)

@tool
def search_amazon(query: str) -> str:
    """Search Amazon India using Tavily."""
    try:
        results = client.search(query=f"{query} site:amazon.in", max_results=3)
        output = ""
        for r in results.get('results', []):
            output += r['title'] + "\n" + r['url'] + "\n\n"
        return output.strip() if output else "No Amazon results."
    except Exception as e:
        return "Amazon search error: " + str(e)

@tool
def search_flipkart(query: str) -> str:
    """Search Flipkart using Tavily."""
    try:
        results = client.search(query=f"{query} site:flipkart.com", max_results=3)
        output = ""
        for r in results.get('results', []):
            output += r['title'] + "\n" + r['url'] + "\n\n"
        return output.strip() if output else "No Flipkart results."
    except Exception as e:
        return "Flipkart search error: " + str(e)

@tool
def search_myntra(query: str) -> str:
    """Search Myntra using Tavily."""
    try:
        results = client.search(query=f"{query} site:myntra.com", max_results=3)
        output = ""
        for r in results.get('results', []):
            output += r['title'] + "\n" + r['url'] + "\n\n"
        return output.strip() if output else "No Myntra results."
    except Exception as e:
        return "Myntra search error: " + str(e)

@tool
def search_ajio(query: str) -> str:
    """Search Ajio using Tavily."""
    try:
        results = client.search(query=f"{query} site:ajio.com", max_results=3)
        output = ""
        for r in results.get('results', []):
            output += r['title'] + "\n" + r['url'] + "\n\n"
        return output.strip() if output else "No Ajio results."
    except Exception as e:
        return "Ajio search error: " + str(e)

model = ChatOllama(model="gemma2:2b")

prompt = PromptTemplate(
    input_variables=["input", "agent_scratchpad", "tools", "tool_names", "chat_history"],
    template="""
You are a helpful AI Shopping Assistant.

Use the tools below to directly answer shopping queries with relevant product links from Amazon, Flipkart, Myntra, and Ajio.

Use this format:
Question: {input}
Thought: [Your reasoning]
Action: [Tool name from above]
Action Input: [Input to the tool]
Observation: [Result from the tool]
... (repeat Thought/Action/Observation as needed)

Only when you have used **all relevant tools** (Amazon, Flipkart, Myntra, Ajio), respond with:
Final Answer: [Your final summary answer including links from all tools.]

Use memory to understand past preferences (like brand or budget) if the current query is vague.

Previous conversation:
{chat_history}

Tools you can use:
{tools}

Tool names:
{tool_names}

Begin!

Question: {input}
{agent_scratchpad}
"""
)

tools = [search_amazon, search_flipkart, search_myntra, search_ajio]

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = create_react_agent(
    llm=model,
    tools=tools, 
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    memory=memory, 
    handle_parsing_errors=True, 
    verbose=True
)

st.set_page_config(page_title="🛍️ AI Shopping Assistant", layout="centered")
st.title("🛍️ AI Shopping Assistant")
st.markdown("Ask me about products to find the best options from Amazon, Flipkart, Myntra, and Ajio!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("What are you looking for today?")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    with st.spinner("Finding best deals..."):
        result = agent_executor.invoke({"input": user_input})
        reply = result.get("output", "No response.")
        st.session_state.chat_history.append(("AI", reply))

for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)
