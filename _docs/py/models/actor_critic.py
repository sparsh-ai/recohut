# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/models/models.actor_critic.ipynb (unless otherwise specified).

__all__ = ['Actor', 'Critic']

# Cell
from typing import Tuple
import torch
from torch import nn

# Cell
class Actor(nn.Module):
    """
    Actor Network
    """

    def __init__(self, embedded_state_size: int, action_weight_size: int, hidden_sizes: Tuple[int]):
        """
        Initialize Actor
        :param embedded_state_size: embedded state size
        :param action_weight_size: embedded action size
        :param hidden_sizes: hidden sizes
        """
        super(Actor, self).__init__()

        self.net = nn.Sequential(
            nn.Linear(embedded_state_size, hidden_sizes[0]),
            nn.ReLU(),
            nn.Linear(hidden_sizes[0], hidden_sizes[1]),
            nn.ReLU(),
            nn.Linear(hidden_sizes[1], action_weight_size),
        )

    def forward(self, embedded_state):
        """
        Forward
        :param embedded_state: embedded state
        :return: action weight
        """
        return self.net(embedded_state)

# Cell
class Critic(nn.Module):
    """
    Critic Network
    """

    def __init__(self, embedded_state_size: int, embedded_action_size: int, hidden_sizes: Tuple[int]):
        """
        Initialize Critic
        :param embedded_state_size: embedded state size
        :param embedded_action_size: embedded action size
        :param hidden_sizes: hidden sizes
        """
        super(Critic, self).__init__()

        self.net = nn.Sequential(
            nn.Linear(embedded_state_size + embedded_action_size, hidden_sizes[0]),
            nn.ReLU(),
            nn.Linear(hidden_sizes[0], hidden_sizes[1]),
            nn.ReLU(),
            nn.Linear(hidden_sizes[1], 1)
        )

    def forward(self, embedded_state, embedded_action):
        """
        Forward
        :param embedded_state: embedded state
        :param embedded_action: embedded action
        :return: Q value
        """
        return self.net(torch.cat([embedded_state, embedded_action], dim=-1))