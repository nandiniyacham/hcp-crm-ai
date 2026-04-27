from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal, engine
from models import Base, Interaction
from agent import langgraph_agent
from fastapi.middleware.cors import CORSMiddleware
from langgraph_setup import create_graph
from agent import langgraph_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


class ChatRequest(BaseModel):
    user_input: str


class EditRequest(BaseModel):
    changes: dict


class FollowupRequest(BaseModel):
    hcp_name: str


class ComplianceRequest(BaseModel):
    notes: str


@app.post("/chat")
def chat_with_agent(request: ChatRequest):
    structured_data = langgraph_agent.run_tool(
        "log_interaction",
        {"user_input": request.user_input}
    )

    session = SessionLocal()
    interaction = Interaction(**structured_data)

    session.add(interaction)
    session.commit()
    session.refresh(interaction)

    return {"form_data": structured_data, "id": interaction.id}


@app.put("/edit/{interaction_id}")
def edit_interaction(interaction_id: int, request: EditRequest):
    session = SessionLocal()
    interaction = session.query(Interaction).filter(Interaction.id == interaction_id).first()

    if not interaction:
        return {"error": "Interaction not found"}

    for field, value in request.changes.items():
        setattr(interaction, field, value)

    session.commit()

    return {"id": interaction.id, "updated": request.changes}


@app.get("/interactions")
def list_interactions():
    session = SessionLocal()
    interactions = session.query(Interaction).all()

    return [
        {
            "id": i.id,
            "hcp_name": i.hcp_name,
            "interaction_type": i.interaction_type,
            "date": i.date,
            "time": i.time,
            "attendees": i.attendees,
            "topics": i.topics,
            "sentiment": i.sentiment,
            "materials_shared": i.materials_shared,
            "outcomes": i.outcomes,
            "followup": i.followup,
            "notes": i.notes
        }
        for i in interactions
    ]


@app.post("/schedule_followup")
def schedule_followup(request: FollowupRequest):
    return langgraph_agent.run_tool("schedule_followup", {"hcp_name": request.hcp_name})


@app.post("/generate_insights")
def generate_insights():
    return langgraph_agent.run_tool("generate_insights", {})


@app.post("/compliance_check")
def compliance_check(request: ComplianceRequest):
    return langgraph_agent.run_tool("compliance_check", {"notes": request.notes})
