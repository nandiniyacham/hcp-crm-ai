import React from "react";
import { useSelector } from "react-redux";

export default function InteractionForm() {
  const interactions = useSelector((state) => state.interactions.list);
  const latest = interactions[interactions.length - 1];

  return (
    <div>
      <h2>Log HCP Interaction</h2>
      {latest ? (
        <div>
          <p><strong>HCP Name:</strong> {latest.hcp_name}</p>
          <p><strong>Date:</strong> {latest.date}</p>
          <p><strong>Sentiment:</strong> {latest.sentiment}</p>
          <p><strong>Materials Shared:</strong> {latest.materials_shared}</p>
          <p><strong>Notes:</strong> {latest.notes}</p>
        </div>
      ) : (
        <p>No interaction logged yet.</p>
      )}
    </div>
  );
}
