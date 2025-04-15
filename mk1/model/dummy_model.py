from model.base_model import BaseModel

class DummyModel(BaseModel):
    def generate(self, prompt: str) -> str:
        return "Mocked agent response"
