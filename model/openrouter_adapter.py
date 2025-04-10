import requests
from model.base_model import BaseModel


class OpenRouterAdapter(BaseModel):
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"

    def generate(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
        }

        response = requests.post(self.api_url, headers=headers, json=payload)

        response.raise_for_status()

        data = response.json()
        if "choices" not in data:
            error_message = data.get("error", {}).get("message", "Unknown error")
            raise RuntimeError(f"OpenRouter 응답오류: {error_message}")

        return data["choices"][0]["message"]["content"]


# 테스트용 코드 (나중에 분리 가능)
# if __name__ == "__main__":
#     import os
#     from dotenv import load_dotenv
#
#     load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
#     api_key = os.getenv("OPENROUTER_API_KEY")  # 환경변수로 API 키 설정
#     model = "mistralai/mistral-small-3.1-24b-instruct:free"  # 예시 무료 모델
#
#     adapter = OpenRouterAdapter(api_key=api_key, model=model)
#     result = adapter.generate("고양이의 평균 몸무게에 대해 알려줘")
#     print("응답:", result)
