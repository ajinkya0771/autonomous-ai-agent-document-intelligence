from agent.graph import build_agent

agent = build_agent()

while True:
    query = input("\nAsk a question: ")
    result = agent.invoke({"user_query": query, "chat_history": []})
    print("\nAnswer:", result["response"])
