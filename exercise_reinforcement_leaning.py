import numpy as np
import random

# Road crossing environment
# Road length: 0=Start, 1=Middle, 2=Other side (goal)
road_length = 3
actions = 2  # 0=Left, 1=Right

# Initialize Q-table (3 positions x 2 actions)
Q = np.zeros((road_length, actions))

# Training parameters
episodes = 1000
learning_rate = 0.8
gamma = 0.9  # Discount factor
epsilon = 0.2  # Exploration rate
max_steps = 10  # Prevent endless steps

# Reward for reaching goal
goal_reward = 10
step_penalty = -1

# Training loop
for episode in range(episodes):
    state = 0  # Start at position 0
    done = False
    steps = 0
    
    while not done and steps < max_steps:
        # Epsilon-greedy action selection
        if random.random() < epsilon:
            action = random.randint(0, 1)  # Explore
        else:
            action = np.argmax(Q[state])  # Exploit
        
        # to determine next state
        if action == 0:  # Left
            next_state = max(0, state - 1)
        else:  # Right
            next_state = min(2, state + 1)
        
        # Give rewards
        if next_state == 2:  # Reached goal
            reward = goal_reward
            done = True
        else:
            reward = step_penalty
        
        # Q-learning update
        Q[state, action] = Q[state, action] + learning_rate * (
            reward + gamma* np.max(Q[next_state]) - Q[state, action])
        
        state = next_state
        steps += 1

# Testing the trained agent
print("Trained Q-table:")
print(Q)

print("\nAgent crossing the road:")
state = 0
steps = 0
path = []

while state != 2 and steps < max_steps:
    action = np.argmax(Q[state])
    if action == 0:
        next_state = max(0, state - 1)
        direction = "Left"
    else:
        next_state = min(2, state + 1)
        direction = "Right"
    
    print(f"Step {steps+1}: Position {state} -> Action {direction} -> Position {next_state}")
    path.append(direction)
    state = next_state
    steps += 1

if state == 2:
    print("\nSuccess! Path taken:", " -> ".join(path))
else:
    print("\nFailed to cross in time")
        