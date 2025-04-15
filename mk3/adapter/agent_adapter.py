from abc import ABC, abstractmethod
from typing import Dict, Any

class AgentAdapter(ABC):
    @abstractmethod
    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """에이전트를 실행하고 결과를 반환합니다."""
        pass
