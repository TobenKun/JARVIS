class AgentBroker:
    def __init__(self, agent_manager):
        self.agent_manager = agent_manager

    def analyze_message(self, message):
        """
        유저 메시지를 기반으로 어떤 에이전트를 호출할지 결정
        (지금은 키워드 기반 룰)
        """
        message = message.lower()
        agents_to_call = []

        if "일정" in message or "캘린더" in message:
            if "CalendarAgent" in self.agent_manager.agents:
                agents_to_call.append("CalendarAgent")
        elif "검색" in message:
            if "SearchAgent" in self.agent_manager.agents:
                agents_to_call.append("SearchAgent")
        elif "요약" in message:
            if "SummaryAgent" in self.agent_manager.agents:
                agents_to_call.append("SummaryAgent")
        else:
            # 기본 에이전트로 fallback
            if "ChatAssistant" in self.agent_manager.agents:
                agents_to_call.append("ChatAssistant")

        return agents_to_call

    def dispatch_message(self, agent_names, message):
        """
        에이전트 리스트에 메시지를 순차적으로 전달하고 응답 이어받기
        """
        response = message
        for name in agent_names:
            agent = self.agent_manager.agents.get(name)
            if agent:
                response = agent.run(response)
        return response

    def send_response(self, response):
        print("\n📨 최종 응답:\n")
        print(response)

