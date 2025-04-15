from concurrent import futures
import grpc
import time

import agent_pb2
import agent_pb2_grpc
from default_agent import DefaultAgent


class AgentService(agent_pb2_grpc.AgentServiceServicer):
    def __init__(self):
        self.agent = DefaultAgent()

    def Process(self, request, context):
        user_input = request.user_input
        response_text = self.agent.process(user_input)
        return agent_pb2.AgentResponse(response=response_text)

    def Capabilities(self, request, context):
        caps = self.agent.capabilities()
        return agent_pb2.CapabilitiesResponse(capabilities=caps)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agent_pb2_grpc.add_AgentServiceServicer_to_server(AgentService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("🚀 DefaultAgent gRPC server started on port 50051.")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
