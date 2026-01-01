from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.tools import get_rag_tool
from llm.groq_llm import llm


rag_tool = get_rag_tool()


def agent_node(state: AgentState):
    """
    Agent reasoning node.
    """
    query = state["user_query"]

    decision_prompt = f"""
    Question: {query}

    Decide whether document retrieval is required.
    Answer 'yes' or 'no' only.
    """

    decision = llm.invoke(decision_prompt).content.lower()

    if "yes" in decision:
        context = rag_tool.run(query)
        final_prompt = f"""
        Context:
        {context}

        Question:
        {query}
        """
        answer = llm.invoke(final_prompt).content
        return {"response": answer}

    else:
        answer = llm.invoke(query).content
        return {"response": answer}


def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)
    graph.set_entry_point("agent")
    graph.add_edge("agent", END)

    return graph.compile()
