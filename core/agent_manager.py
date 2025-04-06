import os
import yaml
from agents.base_agent import BaseAgent

AGENT_STORE_PATH = "data/agents.yaml"


class AgentManager:
    def __init__(self):
        self.agents = {}
        self.load_agents()

    def load_agents(self):
        if not os.path.exists(AGENT_STORE_PATH):
            return

        with open(AGENT_STORE_PATH, "r") as f:
            agent_configs = yaml.safe_load(f) or []

        for config in agent_configs:
            agent = BaseAgent(
                name=config["name"],
                model=config["model"],
                description=config["description"],
                system_prompt=config["system_prompt"],
                tools=config.get("tools", []),
                params=config.get("params", {}),
            )
            self.agents[agent.name] = agent

    def save_agents(self):
        data = [
            {
                "name": agent.name,
                "model": agent.model,
                "description": agent.description,
                "system_prompt": agent.system_prompt,
                "tools": agent.tools,
                "params": agent.params,
            }
            for agent in self.agents.values()
        ]
        os.makedirs(os.path.dirname(AGENT_STORE_PATH), exist_ok=True)
        with open(AGENT_STORE_PATH, "w") as f:
            yaml.dump(data, f)

    def add_agent(self, yaml_path):
        with open(yaml_path, "r") as f:
            config = yaml.safe_load(f)

        name = config["name"]
        if name in self.agents:
            raise ValueError(f"Agent {name} already exists.")

        agent = BaseAgent(
            name=name,
            model=config["model"],
            description=config["description"],
            system_prompt=config["system_prompt"],
            tools=config.get("tools", []),
            params=config.get("params", {}),
        )

        self.agents[name] = agent
        self.save_agents()
        print(f"[+] Agent {name} added.")

    def remove_agent(self, name):
        if name in self.agents:
            del self.agents[name]
            self.save_agents()
            print(f"[-] Agent {name} removed.")
        else:
            print(f"[!] Agent {name} not found.")

    def list_agents(self):
        return [
            {"name": agent.name, "model": agent.model, "description": agent.description}
            for agent in self.agents.values()
        ]

