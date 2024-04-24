from Bad_Guy import Bad_Guy
from Good_Guy import Good_Guy

class Actions:
    def gg_choose_defense(gg, verbose):
        gg.def_lvl += 1
        gg.update_last_action("defense")
        if verbose:
            print("Good guy " + str(gg.gg_id) + " chose defense")
            print("Good guy old defense level: " + str(gg.def_lvl))
            print("Good guy new defense level: " + str(gg.def_lvl+1))
            print("\n")

    def gg_choose_money(gg, verbose):
        gg.bank += 10
        gg.update_last_action("money")
        if verbose:
            print("Good guy " + str(gg.gg_id) + " chose money")
            print("Good guy old bank: " + str(gg.bank-10))
            print("Good guy new bank: " + str(gg.bank))
            print("\n")
        

    def bg_steal(bg, gg, verbose):
        #print("Attempting to steal from good guy" + str(gg.gg_id))
        bad_guy = bg
        good_guy = gg
        if verbose:
                print("Bad guy: " + str(bad_guy.bg_id))
                print("Attacking target good guy: " + str(good_guy.gg_id))
                print("Turn: " + str(bad_guy.num_moves - 1))
                print("Good guy def: " + str(good_guy.def_lvl))
                print("Good guy bank: " + str(good_guy.bank))
                print("Good guy strat: " + str(good_guy.strat))
                print("Bad guy att: " + str(bad_guy.att_lvl))
                print("Bad guy bank: " + str(bad_guy.bank))
                print("Bad guy strat: " + str(bad_guy.strat))
                print("Expected Payout (POV of BG): " + str(float(good_guy.bank) * (.2 + .1 * (float(bad_guy.att_lvl)-float(good_guy.def_lvl)))))
                print("\n")

        payout = float(gg.bank) * (.2 + .1 * (float(bg.att_lvl)-float(gg.def_lvl)))
        if payout < 0.0:
            payout = 0.0

        gg.bank -= payout
        gg.increase_attack_count()
        gg.update_attacked_last_round(True)
        bg.bank += payout
        bg.update_last_action("steal")

    def bg_research(bg, verbose):
        if verbose:
            print("Bad guy: " + str(bg.bg_id))
            print("Action: research")
            print("Bad guy current attack level: " + str(bg.att_lvl))
            print("Bad guy new attack level: " + str(bg.att_lvl + 1))
            print("\n")
        bg.att_lvl += 1
        bg.update_last_action("research")

    # bad_guy = Bad_Guy("1", att_lvl=5, bank=100)
    # bg_research(bad_guy)
    # #print(bad_guy.att_lvl)

    # good_guy = Good_Guy("1", def_lvl=1, bank=100)

    # bg_steal(bad_guy, good_guy)
    # #print(bad_guy.bank)
    # #print(good_guy.bank)

