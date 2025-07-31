"""Minimal NVIDIA LangChain agent demo."""

from __future__ import annotations
from typing import Optional

if __package__ in (None, ""):
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import DEFAULT_CONFIG, AgentConfig
from history import load_history, save_history

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import OpenAI

# Placeholder for NVIDIA model integration
# In a real deployment this could be `from nemo.llm import NeMoLLM`
# or other NVIDIA LLM API.

def load_llm(api_key: Optional[str] = None):
    """Load the language model via LangChain."""
    # Here we use OpenAI for simplicity. Replace with NVIDIA LLM call.
    return OpenAI(openai_api_key=api_key)


def main(config: AgentConfig = DEFAULT_CONFIG) -> None:
    llm = load_llm(api_key=config.api_key)
    memory = ConversationBufferMemory()
    conversation = ConversationChain(llm=llm, memory=memory)

    history: list[str] = []
    if config.history_path:
        history = load_history(config.history_path)
        for line in history:
            print(line)

    print("NVIDIA LangChain Agent. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "quit":
            break
        response = conversation.predict(input=user_input)
        print(f"Agent: {response}")
        history.append(f"You: {user_input}")
        history.append(f"Agent: {response}")

    if config.history_path:
        save_history(config.history_path, history)


if __name__ == "__main__":
    main()
