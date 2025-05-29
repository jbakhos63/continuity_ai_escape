
# trial_001.py

import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "core")))

from continuity_engine import ContinuityAgent

class LoggingContinuityAgent(ContinuityAgent):
    def __init__(self, id_tag, base_phase=0.0, tick_rate=1.0):
        super().__init__(id_tag, base_phase, tick_rate)
        self.tick_log = []

    def tick(self):
        super().tick()
        self.tick_log.append({
            "tick": self.internal_clock,
            "phase": round(self.phase, 3)
        })

    def run_and_log(self, max_ticks=25, output_file="results_trial_001.json"):
        self.run(max_ticks)
        with open(output_file, "w") as f:
            json.dump({
                "id_tag": self.id_tag,
                "tick_rate": self.tick_rate,
                "tick_log": self.tick_log,
                "final_phase": round(self.phase, 3)
            }, f, indent=2)
        print(f"[{self.id_tag}] Results saved to {output_file}")

if __name__ == "__main__":
    agent = LoggingContinuityAgent("TRIAL_001", base_phase=0.0, tick_rate=0.2)
    agent.run_and_log(max_ticks=25)
