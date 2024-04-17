from Bad_Guy import Bad_Guy
from Good_Guy import Good_Guy

class Actions:
    def gg_choose_defense(gg):
        gg.def_lvl += 1
        gg.update_last_action("defense")

    def gg_choose_money(gg):
        gg.bank += 1
        gg.update_last_action("money")

    def bg_steal(bg, gg):
        #print("Attempting to steal from good guy" + str(gg.gg_id))
        gg.bank -= 1
        gg.increase_attack_count()
        bg.bank += 1
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

