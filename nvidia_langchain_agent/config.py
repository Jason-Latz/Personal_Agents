"""Configuration utilities for the NVIDIA LangChain agent."""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class AgentConfig:
    """Runtime configuration for the agent."""

    api_key: str | None = None
    model_endpoint: str | None = None
    history_path: Path | None = None


DEFAULT_CONFIG = AgentConfig()
