import numpy as np
from agent import Agent

def antoine_julien_thibault_policy(agent: Agent) -> str:
    """
    Custom policy of the agent using Upper Confidence Bound (UCB)
    Takes an agent object as input and returns the action: "left", "right", or "none"
    """

    sampled_rewards = np.random.beta(agent.known_rewards + 1, 1)

    action = np.argmax(sampled_rewards)

    if action < agent.position:
        return "left"
    elif action > agent.position:
        return "right"
    else:
        return "none"