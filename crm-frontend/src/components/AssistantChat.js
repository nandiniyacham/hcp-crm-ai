import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  addInteraction,
  editInteraction,
  scheduleFollowup,
  generateInsights,
  complianceCheck,
} from "../store/interactionSlice";

export default function AssistantChat() {
  const [input, setInput] = useState("");
  const dispatch = useDispatch();

  const { insights, followup, compliance, list } = useSelector(
    (state) => state.interactions
  );

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!input.trim()) return;

    const latest = list[list.length - 1];

    // Detect edit intent
    if (
      input.toLowerCase().includes("sorry") ||
      input.toLowerCase().includes("actually")
    ) {
      if (latest) {
        dispatch(
          editInteraction({
            id: latest.id,
            changes: {
              hcp_name: "Dr. John",
              sentiment: "Negative",
            },
          })
        );
      } else {
        console.warn("No interaction to edit");
      }
    } else {
      // Normal logging
      dispatch(addInteraction({ user_input: input }));
    }

    setInput("");
  };

  return (
    <div>
      <h2>AI Assistant</h2>

      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Describe interaction..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          rows={4}
          style={{ width: "100%" }}
        />
        <button type="submit">Log</button>
      </form>

      <div style={{ marginTop: "20px" }}>
        <button onClick={() => dispatch(generateInsights())}>
          Generate Insights
        </button>

        {/* ✅ FIXED */}
        <button
          onClick={() =>
            dispatch(scheduleFollowup({ hcp_name: "Dr. Smith" }))
          }
        >
          Schedule Follow-Up
        </button>

        {/* ✅ FIXED */}
        <button
          onClick={() =>
            dispatch(complianceCheck({ notes: "Discussed off-label use" }))
          }
        >
          Compliance Check
        </button>
      </div>

      {/* Results */}
      {insights && (
        <p>
          <strong>Insights:</strong> {JSON.stringify(insights)}
        </p>
      )}

      {followup && (
        <p>
          <strong>Follow-Up:</strong> {JSON.stringify(followup)}
        </p>
      )}

      {compliance && (
        <p>
          <strong>Compliance:</strong> {JSON.stringify(compliance)}
        </p>
      )}
    </div>
  );
}
