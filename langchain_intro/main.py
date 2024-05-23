from langchain.schema.messages import HumanMessage, SystemMessage
from langchain_intro.chatbot import chat_model

messages = [
        SystemMessage(
            content="""You're an assistant knowledgable about healthcare.
            Only answer health-care related questions."""
        ),
        HumanMessage(content="What is Medicaid managed care?")
]

chat_model.invoke(messages)