# 定義群
# ------
# males: N人の男性が格納された配列
# females: N人の女性が格納された配列
# match(m, f): 男性mと女性fを結婚させる
# unmatch(m, f): 男性mと女性fを離婚させる
# x.preference_list: xの選好度リスト。
#     男性ならN人の女性が、女性ならN人の男性が先頭から好きな順に格納されている
# x.is_matched: xが誰かと結婚していればTrueを、そうでなければFalseを返す
# x.partner: xが誰かと結婚している場合、その相手を返す
# x.prefer(a, b): xがaよりもbを好むならTrueを、そうでなければFalseを返す

# 最初は全ての男性は独身である
for male in males:
    for female in females:
        male.has_proposed[female] = False

while True:
    for male in males:
        if male.is_matched: continue
        # 独身の男性は、まだ求婚したことがない女性に順番に求婚していく
        for female in male.preference_list:
            if male.has_proposed[female]: continue
            # 求婚をする
            male.has_proposed[female] = True
            # 女性が独身なら結婚をする
            if not female.is_matched:
                macth(male, female)
                break
            # 女性が既婚であり、もしも女性が現在のパートナーよりも男性maleの方が好ましいと思った場合、
            # 現在の結婚を解消して男性maleの求婚を受け入れる
            if female.prefer(male, female.partner):
                unmatch(female.partner, female)
                match(male, female)
                break
            # 求婚が受け入れられなかった場合、一つ選考順位の低い女性に求婚する
            continue

    # 全ての男性が結婚している状態になったら終了する
    finished = True
    for male in males:
        if not male.is_matched:
            finished = False
    if finished: break

