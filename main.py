import os
from dotenv import load_dotenv

from core.agent_broker import AgentBroker
from core.conductor import Conductor  # 우리가 만든 지휘자


def main():
    # 1. 환경 변수 로드
    load_dotenv()
    config_path = "config/agents.yaml"

    # 2. 브로커 및 컨덕터 초기화
    broker = AgentBroker(config_path=config_path)
    conductor = Conductor(broker)

    # 3. 유저 입력 받기
    while True:
        user_input = input("👤 사용자 입력: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # 4. 컨덕터에 전달해서 응답 받기
        try:
            response = conductor.handle(user_input)
            print(f"🤖 응답: {response}")
        except Exception as e:
            print(f"⚠️ 에러: {e}")


if __name__ == "__main__":
    main()

