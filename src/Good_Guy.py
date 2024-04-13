class Good_Guy:
    last_action = None
    attack_count = 0
    strat = None
    
    def __init__(self, gg_id, def_lvl=0, bank=0):
        self.gg_id = gg_id
        self.att_lvl = def_lvl
        self.bank = bank

    def update_last_action(self, new_action):
        self.last_action = new_action

    def increase_attack_count(self):
        self.attack_count += 1

    def update_strat(self, new_strat):
        self.strat = new_strat
    