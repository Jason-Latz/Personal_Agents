"""Entry point for running the agent with optional environment configuration."""

from __future__ import annotations

import os
from pathlib import Path

from .agent import main
from .config import AgentConfig


def from_env() -> AgentConfig:
    return AgentConfig(
        api_key=os.getenv("AGENT_API_KEY"),
        model_endpoint=os.getenv("AGENT_MODEL_ENDPOINT"),
        history_path=Path(os.getenv("AGENT_HISTORY", "history.txt")),
    )


if __name__ == "__main__":
    config = from_env()
    main(config)
