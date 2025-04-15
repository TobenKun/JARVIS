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
    "mock": DummyModel,
}



class AgentFactory:
    def __init__(self):
        self.agents_path = "config/agents.yaml"
        self.planner_path = "config/planner.yaml"
        self.use_mock_agent = os.getenv("USE_MOCK_AGENT", "false").lower() == "true"
        self.use_mock_planner = os.getenv("USE_MOCK_PLANNER", "false").lower() == "true"


    def load_agents(self) -> dict:
        return self._load_from_file(self.agents_path, use_mock=self.use_mock_agent)

    def load_planner(self) -> BaseAgent:
        agents = self._load_from_file(self.planner_path, use_mock=self.use_mock_planner)
        return list(agents.values())[0]  # 단일 에이전트만 있다

    def _load_from_file(self, path: str, use_mock: bool) -> dict:
        with open(path, "r") as file:
            config = yaml.safe_load(file)

        agents = {}
        for agent_config in config["agents"]:
            agent = self._create_agent(agent_config, use_mock)
            agents[agent_config["name"]] = agent

        return agents

    def _create_agent(self, config: dict, use_mock: bool) -> BaseAgent:
        agent_class = AGENT_TYPE_MAP[config["type"]]


        if use_mock:
            model = MODEL_TYPE_MAP["mock"]()
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
