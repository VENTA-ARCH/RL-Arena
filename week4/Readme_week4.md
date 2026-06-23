# Week 4 – Reinforcement Learning Learning Summary

## Overview

This week I explored the fundamentals of Reinforcement Learning (RL) and learned how agents interact with environments to learn optimal behavior through trial and error. I worked with both a pre-built Gymnasium environment (CartPole) and a custom maze environment, which helped me understand the complete RL workflow from environment design to agent training.

---

## What is Reinforcement Learning?

Reinforcement Learning is a machine learning paradigm where an agent learns by interacting with an environment.

The agent:
1. Observes the current state.
2. Takes an action.
3. Receives a reward.
4. Moves to a new state.

The objective is to maximize the total reward accumulated over time.

### Main Components

- **Agent** – The decision maker.
- **Environment** – The world in which the agent operates.
- **State** – The current situation of the environment.
- **Action** – A decision made by the agent.
- **Reward** – Feedback received after taking an action.

---

## Gymnasium Framework

I learned that Gymnasium provides a standard interface for creating and training reinforcement learning environments.

The key functions are:

### reset()

Initializes the environment and starts a new episode.

### step(action)

Executes an action and returns:
- New state
- Reward
- Termination status
- Additional information

### render()

Visualizes the environment and agent behavior.

Using a standard interface makes it easier to apply different RL algorithms to different environments.

---

## CartPole Environment

The CartPole task involves balancing a pole on top of a moving cart.

The agent can:
- Move left
- Move right

The goal is to keep the pole balanced for as long as possible.

Through this example I learned:
- How RL environments represent states.
- How rewards guide learning.
- How training and evaluation are performed.
- How PPO can be used to learn successful policies.

---

## PPO (Proximal Policy Optimization)

PPO is one of the most popular reinforcement learning algorithms.

Some important observations:

- It improves policies gradually.
- It provides stable training.
- It is widely used in practical RL applications.
- Stable-Baselines3 provides an easy implementation of PPO.

PPO learns by collecting experiences from the environment and updating the policy based on received rewards.

---

## Custom Maze Environment

The maze assignment helped me understand how custom RL environments are built.

Important components included:

### Action Space

The agent can perform four actions:

- Up
- Right
- Down
- Left

### Observation Space

The maze state is represented as a grid where different values correspond to:

- Empty cells
- Walls
- Goal position
- Agent position

### Rewards

Rewards are used to guide the agent toward the goal:

- Positive reward for reaching the goal.
- Small penalties for inefficient or invalid actions.

### Episode Termination

An episode ends when the agent reaches the goal.

---

## Key Insights

- Reinforcement Learning focuses on learning through interaction rather than labeled data.
- Reward design significantly affects agent behavior.
- Gymnasium provides a clean framework for environment creation.
- PPO is a stable and effective RL algorithm.
- Custom environments help in understanding how RL systems work internally.
- Navigation problems such as mazes are a good introduction to reinforcement learning concepts.

---

## Conclusion

This week provided an introduction to reinforcement learning through both theory and implementation. Working with CartPole helped me understand how RL agents are trained, while creating a custom maze environment showed how environment design, observations, actions, and rewards influence learning. Overall, I gained a better understanding of the RL workflow and the role of algorithms such as PPO in training intelligent agents.