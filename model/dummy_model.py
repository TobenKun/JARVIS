from model.base_model import BaseModel

class DummyModel(BaseModel):
    def generate(self, prompt: str) -> str:
        print("[DummyModel] Prompt received:")
        print(prompt)
        return "Mocked agent response"
