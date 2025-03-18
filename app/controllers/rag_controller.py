from app.models.config import config
from app.core.graph import AgentPipeline

import os


class RAGController:
    def __init__(self):
        pass


    async def consult_rag(self, question, forms=False):
        pipe = AgentPipeline()

        if forms:
            response = pipe.run(question, forms=True)
        
        else:
            response = pipe.run(question)

        return response




