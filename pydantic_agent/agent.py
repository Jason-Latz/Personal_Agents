from __future__ import annotations
from typing import List
from pydantic import BaseModel

class Message(BaseModel):
    user: str
    content: str

class Agent:
    """A very simple agent that echoes messages with a prefix."""
    prefix: str = "Agent"

    def handle(self, messages: List[Message]) -> List[Message]:
        return [Message(user=self.prefix, content=f"Echo: {m.content}") for m in messages]

if __name__ == "__main__":
    msgs = [Message(user="user", content="hello world"), Message(user="user", content="pydantic rules")]
    agent = Agent()
    for reply in agent.handle(msgs):
        print(f"{reply.user}: {reply.content}")
