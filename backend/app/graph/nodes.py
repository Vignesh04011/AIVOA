from app.agents.interaction_agent import interaction_agent
from app.agents.supervisor import supervisor
from app.agents.medical_agent import medical_agent
from app.agents.recommendation_agent import recommendation_agent
from app.agents.formatter_agent import formatter_agent


def interaction_node(state):
    return interaction_agent(state)


def supervisor_node(state):
    return supervisor(state)


def medical_node(state):
    return medical_agent(state)


def recommendation_node(state):
    return recommendation_agent(state)


def formatter_node(state):
    return formatter_agent(state)