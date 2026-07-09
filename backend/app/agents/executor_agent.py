from app.agents.interaction_agent import interaction_agent
from app.agents.edit_agent import edit_agent
from app.agents.summary_agent import summary_agent
from app.agents.medical_agent import medical_agent
from app.agents.recommendation_agent import recommendation_agent
from app.agents.search_agent import search_agent
from app.agents.save_agent import save_agent


TOOLS = {

    "extract": interaction_agent,

    "edit": edit_agent,

    "summary": summary_agent,

    "medical": medical_agent,

    "recommendation": recommendation_agent,

    "search": search_agent,

    "save": save_agent,

}


def executor_agent(state):

    plan = state.get("plan", [])

    for tool in plan:

        agent = TOOLS.get(tool)

        if agent:
            state = agent(state)

    return state