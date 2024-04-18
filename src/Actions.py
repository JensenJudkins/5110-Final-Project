from Bad_Guy import Bad_Guy
from Good_Guy import Good_Guy

class Actions:
    def gg_choose_defense(gg):
        gg.def_lvl += 1
        gg.update_last_action("defense")

    def gg_choose_money(gg):
        gg.bank += 10
        gg.update_last_action("money")

    def bg_steal(bg, gg):
        #print("Attempting to steal from good guy" + str(gg.gg_id))
        payout = float(gg.bank) * (.2 + .1 * (float(bg.att_lvl)-float(gg.def_lvl)))
        if payout < 0.0:
            payout = 0.0

        gg.bank -= payout
        gg.increase_attack_count()
        gg.update_attacked_last_round(True)
        bg.bank += payout
        bg.update_last_action("steal")

    def bg_research(bg):
        bg.att_lvl += 1
        bg.update_last_action("research")

    bad_guy = Bad_Guy("1", att_lvl=5, bank=100)
    bg_research(bad_guy)
    #print(bad_guy.att_lvl)

    good_guy = Good_Guy("1", def_lvl=1, bank=100)

    bg_steal(bad_guy, good_guy)
    #print(bad_guy.bank)
    #print(good_guy.bank)

