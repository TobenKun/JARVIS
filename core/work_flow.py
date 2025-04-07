from agents.base_agent import BaseAgent


# TODO: 각 agent의 출력값을 가공해서 다음 agent에 넣는 방식도 가능하게 확장하기
# TODO: 중간결과 로깅
class Workflow:
    def __init__(self, steps: list[BaseAgent], input_data: str):
        self.steps = steps
        self.input_data = input_data

    def run(self) -> str:
        result = self.input_data

        for agent in self.steps:
            result = agent.process(result)

        return result
