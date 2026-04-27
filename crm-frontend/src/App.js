import React from "react";
import AssistantChat from "./components/AssistantChat";
import { useSelector } from "react-redux";
import "./App.css";

export default function App() {
  const interactions = useSelector((state) => state.interactions.list);
  const latest = interactions[interactions.length - 1] || {};

  return (
    <div className="container">
      {/* Left Panel */}
      <div className="left-panel">
        <h2>Log HCP Interaction</h2>

        <form className="interaction-form">
          <div className="form-row">
            <label>
              HCP Name:
              <input type="text" value={latest.hcp_name || ""} readOnly />
            </label>
            <label>
              Interaction Type:
              <input type="text" value={latest.interaction_type || ""} readOnly />
            </label>
          </div>

          <div className="form-row">
            <label>
              Date:
              <input type="text" value={latest.date || ""} readOnly />
            </label>
            <label>
              Time:
              <input type="text" value={latest.time || ""} readOnly />
            </label>
          </div>

          <div className="form-row">
            <label>
              Attendees:
              <input type="text" value={latest.attendees || ""} readOnly />
            </label>
            <label>
              Topics Discussed:
              <input type="text" value={latest.topics || ""} readOnly />
            </label>
          </div>

          <div className="section">
            <h3>Sentiment</h3>
            <input type="text" value={latest.sentiment || ""} readOnly />
          </div>

          <div className="section">
            <h3>Materials Shared</h3>
            <input type="text" value={latest.materials_shared || ""} readOnly />
          </div>

          <div className="section">
            <h3>Outcomes</h3>
            <textarea value={latest.outcomes || ""} readOnly />
          </div>

          <div className="section">
            <h3>Follow-up Actions</h3>
            <textarea value={latest.followup || ""} readOnly />
          </div>

          <div className="section">
            <h3>Notes</h3>
            <textarea value={latest.notes || ""} readOnly />
          </div>
        </form>
      </div>

      {/* Right Panel */}
      <div className="right-panel">
        <h2>Log interaction via chat</h2>
        <AssistantChat />
      </div>
    </div>
  );
}
