
# trial_000.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "core")))

from continuity_engine import ContinuityAgent

# Trial 000: Persistence in Silence
# The agent must tick forward independently with no user prompt.

agent = ContinuityAgent("TRIAL_000", base_phase=0.0, tick_rate=0.2)
agent.run(max_ticks=25)
