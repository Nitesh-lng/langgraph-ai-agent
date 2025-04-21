import os
from dotenv import load_dotenv
load_dotenv()


GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")


from langchain_groq import ChatGroq

from langchain_community.tools.tavily_search import TavilySearchResults

groq_llm=ChatGroq(model='gemma2-9b-it')



from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
system_prompt='Act as an AI Chatbot '
def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    
    tools=[TavilySearchResults(max_results=5)] if allow_search else []
    agent=create_react_agent(
        model=groq_llm,
        tools=tools,
        state_modifier=system_prompt
    )

    state={"messages":query}
    response=agent.invoke(state)

    messages=response.get("messages")
    ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]

    return ai_messages[-1]


