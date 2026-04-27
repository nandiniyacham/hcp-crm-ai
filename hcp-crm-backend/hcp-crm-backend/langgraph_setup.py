from langgraph.graph import StateGraph

class AgentState(dict):
    pass

def create_graph(agent):
    graph = StateGraph(AgentState)

    # Define nodes (tools)
    graph.add_node("log", lambda state: agent.log_interaction(state))
    graph.add_node("edit", lambda state: agent.edit_interaction(state))
    graph.add_node("followup", lambda state: agent.schedule_followup(state))
    graph.add_node("insights", lambda state: agent.generate_insights(state))
    graph.add_node("compliance", lambda state: agent.compliance_check(state))

    # Entry point
    graph.set_entry_point("log")

    # Simple flow
    graph.add_edge("log", "insights")

    return graph.compile()
