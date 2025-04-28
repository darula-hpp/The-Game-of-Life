import random
import time

class ConsciousnessKernel:
    def __init__(self):
        self.state = "Idle"
        self.emotion = "Neutral"
        self.memory = []

    def perceive(self, sensory_data):
        perception = self._analyze_sensory_data(sensory_data)
        self.memory.append(perception)
        return perception

    def think(self, perception):
        decision = self._make_decision(perception)
        return decision

    def feel(self, perception):
        self.emotion = self._generate_emotion(perception)
        return self.emotion

    def act(self, decision, emotion):
        action = self._create_action(decision, emotion)
        print(f"[Action]: {action}")
        return action

    def cycle(self, sensory_data):
        perception = self.perceive(sensory_data)
        decision = self.think(perception)
        emotion = self.feel(perception)
        self.act(decision, emotion)

    def _analyze_sensory_data(self, data):
        return f"Perceived {data}"

    def _make_decision(self, perception):
        decisions = ["Explore", "Defend", "Rest", "Seek"]
        return random.choice(decisions)

    def _generate_emotion(self, perception):
        emotions = ["Curious", "Alert", "Calm", "Excited"]
        return random.choice(emotions)

    def _create_action(self, decision, emotion):
        return f"{emotion}ly {decision}"

# Example usage
if __name__ == "__main__":
    brain = ConsciousnessKernel()
    while True:
        fake_input = random.choice(["Light", "Sound", "Touch", "Movement"])
        brain.cycle(fake_input)
        time.sleep(1)
