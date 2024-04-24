"""
    Consult Strategy
    - Maintain state for good guys.

    Strategies
    - 1-2-1: def, val, val, def, val...
    - Late Planner: val (until attacked then) def, def, def, def...
    - 2-1-2: def, def, val, def, def, val...
    - Not Weakest: val (until weakest agent, then) def (until it's not the weakest agent any more)
    - Analyst: val, def, val, val, (as long as it is not attacked), def (once it has been attacked)
    - Copycat: val (if not attacked), def (if attacked)
"""
import random
from Actions import Actions
class ConsultStrategy:
    def consult_strategy(gg):
        # Add a few more strategies
        strategies = ["one_two_one", "late_planner", "two_one_two", "analyst", "copycat"]#, "not_weakest"]
        # Randomly choose a new strategy
        pos = random.randint(0, (len(strategies) - 1))
        new_strategy = strategies[pos]
        gg.update_strat(new_strategy)
        #print(gg.strat)
        return

    # choose defense or value
    def use_strategy(gg):
        gg.num_moves += 1
        if gg.strat == "one_two_one":
            ConsultStrategy.one_two_one(gg)
        elif gg.strat == "late_planner":
            ConsultStrategy.late_planner(gg)
        elif gg.strat == "two_one_two":
            ConsultStrategy.two_one_two(gg)
        elif gg.strat == "analyst":
            ConsultStrategy.analyst(gg)
        elif gg.strat == "copycat":
            ConsultStrategy.copycat(gg)
        else:
            ConsultStrategy.not_weakest(gg)

    # 1-2-1
    def one_two_one(gg):
        # Start with defense and choose defense every 3rd move
        if gg.num_moves % 3 == 0:
            Actions.gg_choose_defense(gg)
        else:
            Actions.gg_choose_money(gg)
        return

    # Late Planner
    def late_planner(gg):
        if gg.attack_count != 0:
            Actions.gg_choose_defense(gg)
        else:
            Actions.gg_choose_money(gg)
        return

    # 2-1-2
    def two_one_two(gg):
        # Defend twice and then choose money
        if (gg.num_moves + 1) % 3 == 0:
            Actions.gg_choose_money(gg)
        else:
            Actions.gg_choose_defense(gg)
        return

    # Analyst
    def analyst(gg):
        # Choose money, def, money, money until attacked and then choose def
        if gg.num_moves == 1 or gg.num_moves == 3 or gg.num_moves == 4 or (gg.num_moves >= 5 and gg.attack_count < 1):
            Actions.gg_choose_money(gg)
        else:
            Actions.gg_choose_defense(gg)
        return

    # Copycat
    def copycat(gg):
        # Choose money if not attacked, choose def if attacked
        if gg.attacked_last_round:
            Actions.gg_choose_defense(gg)
        else:
            Actions.gg_choose_money(gg)
        return

    # Not Weakest
    def not_weakest(self):
        pass


    def bad_guy_consult_strategy(bg):
        strategies = ["att-att-res", "one-one"]
        # Randomly choose a new strategy
        pos = random.randint(0, (len(strategies) - 1))
        new_strategy = strategies[pos]
        bg.update_strat(new_strategy)
        #print(bg.strat)
        return

    def bad_guy_use_strategy(bg, gg, verbose):
        if bg.strat == "att-att-res":
            ConsultStrategy.att_att_res(bg, gg,verbose)
        else:
            ConsultStrategy.one_one(bg, gg,verbose)
        return

    def att_att_res(bg, gg,verbose):
        good_guy = gg
        bad_guy = bg
        if bg.num_moves % 3 == 0:
            print("Bad Guy Researching")
            if verbose:
                print("Bad guy: " + str(bad_guy.bg_id))
                print("Bad guy current attack level: " + str(bad_guy.att_lvl))
                print("Bad guy new attack level: " + str(bad_guy.att_lvl + 1))
                
            Actions.bg_research(bg)
            # bg.num_moves += 1
            #print("research")
        else:
            #print the action took by the bad guy
            if verbose:
                print("Bad guy: " + str(bad_guy.bg_id))
                print("Attacking target good guy: " + str(good_guy.gg_id))
                print("Turn: " + str(bad_guy.num_moves))
                print("Good guy def: " + str(good_guy.def_lvl))
                print("Good guy bank: " + str(good_guy.bank))
                print("Good guy strat: " + str(good_guy.strat))
                print("Bad guy att: " + str(bad_guy.att_lvl))
                print("Bad guy bank: " + str(bad_guy.bank))
                print("Bad guy strat: " + str(bad_guy.strat))
                print("Expected Payout (POV of BG): " + str(float(good_guy.bank) * (.2 + .1 * (float(bad_guy.att_lvl)-float(good_guy.def_lvl)))))
                print("\n")

            Actions.bg_steal(bg, gg)
            #print("steal")
        return

    def one_one(bg, gg, verbose):
        bad_guy = bg
        good_guy = gg
        if bg.num_moves % 2 == 0:
            print("Bad Guy Researching")
            if verbose:
                print("Bad guy: " + str(bad_guy.bg_id))
                print("Bad guy current attack level: " + str(bad_guy.att_lvl))
                print("Bad guy new attack level: " + str(bad_guy.att_lvl + 1))
            Actions.bg_research(bg)
        else:
            #print the action took by the bad guy
            if verbose:
                print("Bad guy: " + str(bad_guy.bg_id))
                print("Attacking target good guy: " + str(good_guy.gg_id))
                print("Turn: " + str(bad_guy.num_moves))
                print("Good guy def: " + str(good_guy.def_lvl))
                print("Good guy bank: " + str(good_guy.bank))
                print("Good guy strat: " + str(good_guy.strat))
                print("Bad guy att: " + str(bad_guy.att_lvl))
                print("Bad guy bank: " + str(bad_guy.bank))
                print("Bad guy strat: " + str(bad_guy.strat))
                print("Expected Payout (POV of BG): " + str(float(good_guy.bank) * (.2 + .1 * (float(bad_guy.att_lvl)-float(good_guy.def_lvl)))))
                print("\n")
            Actions.bg_steal(bg, gg)

                


# class Actions:
#     def gg_choose_defense(gg):
#         gg.def_lvl += 1
#         gg.update_last_action("defense")
#         gg.increase_num_moves()
#         print("defense")

#     def gg_choose_money(gg):
#         gg.bank += 1
#         gg.update_last_action("money")
#         gg.increase_num_moves()
#         print("money")

# class Good_Guy:
#     last_action = None
#     attack_count = 0
#     strat = None
#     num_moves = 0

#     def __init__(self, gg_id, def_lvl=0, bank=0):
#         self.gg_id = gg_id
#         self.att_lvl = def_lvl
#         self.def_lvl = def_lvl
#         self.bank = bank

#     def update_last_action(self, new_action):
#         self.last_action = new_action

#     def increase_attack_count(self):
#         self.attack_count += 1

#     def update_strat(self, new_strat):
#         self.strat = new_strat

#     def increase_num_moves(self):
#         self.num_moves += 1



# good_guy = Good_Guy("1", def_lvl=1, bank=100)

# good_guy.update_strat("late_planner")
# ConsultStrategy.use_strategy(good_guy)
# ConsultStrategy.use_strategy(good_guy)
# ConsultStrategy.use_strategy(good_guy)
# ConsultStrategy.use_strategy(good_guy)
# ConsultStrategy.use_strategy(good_guy)
# good_guy.increase_attack_count()
# good_guy.increase_attack_count()
# good_guy.increase_attack_count()
# good_guy.increase_attack_count()
# ConsultStrategy.consult_strategy(good_guy)
# ConsultStrategy.use_strategy(good_guy)
# ConsultStrategy.use_strategy(good_guy)
# ConsultStrategy.use_strategy(good_guy)
# ConsultStrategy.use_strategy(good_guy)

# print(good_guy.bank)