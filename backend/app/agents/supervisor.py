def supervisor(state):

    interaction = state["interaction"]

    # Required fields
    required = [
        "hcp_name",
        "interaction_type",
        "interaction_date",
        "interaction_time",
        "topics_discussed",
    ]

    for field in required:
        if not interaction.get(field):
            interaction[field] = "Not Provided"

    # Normalize sentiment
    sentiment = interaction.get("sentiment", "").lower()

    if sentiment not in ["positive", "neutral", "negative"]:
        interaction["sentiment"] = "Neutral"

    state["interaction"] = interaction

    return state