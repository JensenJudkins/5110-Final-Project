class Bad_Guy:
    last_action = None

    def __init__(self, bg_id, att_lvl=0, bank=0):
        self.bg_id = bg_id
        self.att_lvl = att_lvl
        self.bank = bank   
         
    def update_last_action(self, new_action):
        self.last_action = new_action
    
    
