"""
    Consult Strategy
    - Maintain state for good guys.

    Strategies
    - 1-2-1: def, val, val, def, val...
    - Late Planner: val (until attacked then) def, def, def, def...
    - 2-1-2: def, def, val, def, def, val...
    - Not Weakest: val (until weakest agent, then) def (until it's not the weakest agent any more)
"""
class ConsultStrategy:
    # Constructor
    def __init__(self, bank, defense, state, num_times_attacked, prev_strategy):
        self.bank = bank
        self.defense = defense
        self.state = state
        self.num_times_attacked = num_times_attacked
        self.prev_strategy = prev_strategy

    # choose defense or value
    def choose_def_or_val(self):
        pass

    # 1-2-1
    def one_two_one(self):
        pass

    # Late Planner
    def late_planner(self):
        pass

    # 2-1-2
    def two_one_two(self):
        pass

    # Not Weakest
    def not_weakest(self):
        pass