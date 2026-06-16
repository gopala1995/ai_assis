from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools  import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()


def main():
    model = ChatOpenAI(model="gpt-4o-mini",temperature=0)

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Welcome to the ReAct Agent! Type 'exit' to quit.")
    print("Ask me anything or give me a Calculation task to perform.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "exit":
               break
          
        print("\nAI Assistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages":[HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()
          
if __name__ == "__main__":
     main()
        