    spaces.observation_space = spaces.Box

    self.action_space = spaces.Discrete(13)

self.observation_space = spaces.Dict({
    "agent_hand": spaces.Box(low=0, high=12, shape=(13, 2), dtype=np.int16), 
    "cards_played": spaces.Box(low=0, high=12, shape=(4, 13, 2), dtype=np.int16), 
    "total_points": spaces.Box(low=0, high=100, shape=(4,), dtype=np.int16), 
})