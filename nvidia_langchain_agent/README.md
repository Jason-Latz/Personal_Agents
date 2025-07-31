# NVIDIA LangChain Agent

This project is an example entry for the **Generative AI Agents Contest** hosted by NVIDIA and LangChain. It demonstrates how to build an agent using the LangChain/LangGraph framework together with NVIDIA's LLM stack.

## Features
- Sample agent that routes user queries to an NVIDIA-powered language model via the LangChain interface.
- Simple conversation memory using LangChain's conversation chain utilities.
- Configuration driven design that allows you to specify the model endpoint (local NeMo model, TensorRT‑LLM server, etc.).

## Requirements
- Python 3.9+
- `langchain` and `langchain-community`
- `nvidia-nemo` or other NVIDIA LLM API library (placeholder)

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the demo script:

```bash
python run_agent.py
```

This will start an interactive loop where you can chat with the agent.

### Configuration

Runtime settings are defined in `config.py`. You can create a `.env` file or set environment variables for sensitive fields such as API keys. By default the agent will load the `DEFAULT_CONFIG` and use any values provided via the environment.

See `examples.md` for a sample interaction transcript.
