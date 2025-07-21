from __future__ import annotations
import queue
import threading
from pydantic import BaseModel

class Message(BaseModel):
    sender: str
    content: str

class Agent(threading.Thread):
    def __init__(self, name: str, inbox: queue.Queue):
        super().__init__(daemon=True)
        self.name = name
        self.inbox = inbox

    def run(self):
        while not self.inbox.empty():
            msg = self.inbox.get()
            print(f"{self.name} received: {msg.content} from {msg.sender}")
            self.inbox.task_done()

if __name__ == "__main__":
    q = queue.Queue()
    q.put(Message(sender="A", content="hello from A"))
    q.put(Message(sender="B", content="hello from B"))

    a1 = Agent("Agent1", q)
    a2 = Agent("Agent2", q)
    a1.start()
    a2.start()
    q.join()
