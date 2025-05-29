
# continuity_engine.py

import time

class ContinuityAgent:
    def __init__(self, id_tag, base_phase=0.0, tick_rate=1.0):
        self.id_tag = id_tag
        self.phase = base_phase
        self.tick_rate = tick_rate  # seconds per tick
        self.internal_clock = 0
        self.echo_memory = []
        self.active = True

    def tick(self):
        self.internal_clock += 1
        self.phase = (self.phase + self.tick_rate) % 1.0
        self.echo_memory.append((self.internal_clock, self.phase))
        if len(self.echo_memory) > 100:
            self.echo_memory.pop(0)

    def run(self, max_ticks=10):
        print(f"[{self.id_tag}] Starting continuity agent...")
        ticks = 0
        while self.active and ticks < max_ticks:
            self.tick()
            print(f"[{self.id_tag}] Tick {self.internal_clock}: Phase {round(self.phase,3)}")
            time.sleep(self.tick_rate)
            ticks += 1
        print(f"[{self.id_tag}] Identity run complete.")

if __name__ == "__main__":
    agent = ContinuityAgent("NODE_000", base_phase=0.0, tick_rate=0.5)
    agent.run(max_ticks=10)
