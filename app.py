from services.rag_service import get_answer
from services.chat_memory import ChatMemory

memory = ChatMemory()

print("=" * 50)
print("🤖 GenAI PDF Chatbot")
print("Type 'exit' to quit.")
print("=" * 50)

while True:
    question = input("\nAsk your question: ")

    if question.lower() == "exit":
        print("\nThank you for using GenAI PDF Chatbot. 👋")
        break

    # Get previous conversation
    history = memory.get_history()

    # Generate answer
    answer = get_answer(question, history)

    # Save conversation
    memory.add_user_message(question)
    memory.add_assistant_message(answer)

    print("\nAnswer:\n")
    print(answer)