from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    responses: Annotated[list, add_messages]


class SimpleAgentState(TypedDict):
    question: str
    context: list
    answer: str