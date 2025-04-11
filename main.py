import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel
from core import Conductor, AgentBroker
from agents.agent_factory import AgentFactory
from utils.translation import Translator
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

deepl_api_key = os.getenv("DEEPL_API_KEY")

# 초기화
factory = AgentFactory()
broker = AgentBroker()
translator = Translator(deepl_api_key)
conductor = Conductor(broker, translator)

class RunInput(BaseModel):
    user_input: str

class RunOutput(BaseModel):
    result: str

@app.post("/run", response_model=RunOutput)
def run_jarvis(input: RunInput):
    result = conductor.handle(input.user_input)
    return RunOutput(result=result)

@app.get("/agents")
def get_agents():
    return {"agents": broker.list_agents()}

@app.get("/planner")
def get_planner():
    return {"planner": broker.get_planner().name}

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
