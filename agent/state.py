from typing import TypedDict, List


class AgentState(TypedDict):
    user_query: str
    retrieved_context: str
    response: str
    chat_history: List[str]
