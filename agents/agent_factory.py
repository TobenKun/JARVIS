import os
import yaml
from agents.default_agent import DefaultAgent
from model.openrouter_adapter import OpenRouterAdapter
from agents.base_agent import BaseAgent
from model.dummy_model import DummyModel

AGENT_TYPE_MAP = {
    "default": DefaultAgent,
}

MODEL_TYPE_MAP = {
    "openrouter": OpenRouterAdapter,
}



class AgentFactory:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.test_flag = os.getenv("USE_MOCK_AGENT").lower() == "true"

    def load_agents(self) -> dict:
        with open(self.config_path, "r") as file:
            config = yaml.safe_load(file)

        agents = {}
        for agent_config in config["agents"]:
            agent = self._create_agent(agent_config)
            agents[agent_config["name"]] = agent

        return agents

    def _create_agent(self, config: dict) -> BaseAgent:
        agent_class = AGENT_TYPE_MAP[config["type"]]

        if test_flag:
            print("")
            model = DummyModel()
        else:
            model_config = config["model"]

            model_class = MODEL_TYPE_MAP[model_config["type"]]
            api_key = os.getenv(model_config["api_key_env"])

            if api_key is None:
                raise ValueError("환경변수가 설정되지 않았습니다.")

            model = model_class(api_key=api_key, model=model_config["model_name"])

        return agent_class(
            name=config["name"],
            model=model,
            system_prompt=config.get("system_prompt", ""),
        )
