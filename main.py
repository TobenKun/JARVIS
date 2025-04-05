import sys
from core.agent_manager import AgentManager
from core.agent_broker import AgentBroker


def test_agent(config_path, test_message):
    manager = AgentManager()
    manager.add_agent(config_path)
    broker = AgentBroker(manager)

    agent_list = broker.analyze_message(test_message)
    print(f"[DEBUG] 선택된 에이전트: {agent_list}")

    response = broker.dispatch_message(agent_list, test_message)
    broker.send_response(response)


def main():
    manager = AgentManager()

    if len(sys.argv) < 2:
        print("Usage: python main.py [add|remove|list] [args...]")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) == 3:
        manager.add_agent(sys.argv[2])
    elif command == "remove" and len(sys.argv) == 3:
        manager.remove_agent(sys.argv[2])
    elif command == "list":
        agents = manager.list_agents()
        for agent in agents:
            print(agent)
    elif command == "test" and len(sys.argv) == 4:
        test_agent(sys.argv[2], sys.argv[3])
    else:
        print("Invalid command or arguments.")


if __name__ == "__main__":
    main()
