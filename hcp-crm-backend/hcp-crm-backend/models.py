from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String(255), index=True)          # Dr. Smith, Dr. Sharma, etc.
    interaction_type = Column(String(50))               # Meeting, Call, Email
    date = Column(String(50))                           # 2026-04-27
    time = Column(String(50))                           # 19:36
    attendees = Column(String(255))                     # Dr. Smith, Dr. Sharma
    topics = Column(String(500))                        # OncoBoost Phase III trial
    sentiment = Column(String(50))                      # Positive, Neutral, Negative
    materials_shared = Column(String(255))              # Brochure, Sample Pack
    outcomes = Column(String(1000))                     # Key outcomes or agreements
    followup = Column(String(1000))                     # Next steps or tasks
    notes = Column(String(1000))                        # Free-form notes
