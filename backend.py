from typing import List
from pydantic import BaseModel
from ai_agent import get_response_from_ai_agent
class RequestState(BaseModel):
    model_name:str
    model_provider:str
    system_prompt:str
    messages:List[str]
    allow_search:bool
    
from fastapi import FastAPI

ALLOWED_MODEL_LIST=['gemma2-9b-it', 'gemma2-13b-it','gemma2-9b-it-4k','gemma2-13b-it-4k','gemma2-9b-it-8k','gemma2-13b-it-8k','llama-3.3-70b-versatile', 'mixtral-8x7b-32768', 'gpt-4o-mini']


app=FastAPI(title="LangGraph AI Agent")
 
@app.post("/chat")
 
def chat_endpoint(request:RequestState):
    """
    API endpoint to interact with the chatbot using langgraph and search tools
    It dynamically select the model specified in the request

    """
    if request.model_name not in ALLOWED_MODEL_LIST:
        return {"error":f"Model {request.model_name} is not supported"}
    
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider
    
    response=get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9998)