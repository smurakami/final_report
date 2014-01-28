# 定義群
# ------
# males: N人の男性が格納された配列
# females: N人の女性が格納された配列
# match(m, f): 男性mと女性fを結婚させる
# f.queue: 女性fと結婚している男性のリスト
# f.pop(): 女性fと結婚している男性の中で、fにとって最も選好度の低い男性を離婚させる
# x.preference_list: xの選好度リスト。
#     男性ならN人の女性が、女性ならN人の男性が先頭から好きな順に格納されている
# x.prefer(a, b): xがaよりもbを好むならTrueを、そうでなければFalseを返す

p = {} # 各男性が何番目の女性を選ぶかを保管するハッシュテーブル
for m in males:
    # 最初は一番好きな女性に求婚する。
    p[m] = 0
    # 一番好きじゃない女性に求婚するまで繰り返す
    while 0 <= p[m] < len(females):
        f = m.preference_list[p[m]]
        match(m, f)
        # もしも女性と結婚している男性のリストが
        # capacityの範囲内に収まっていればそのまま続ける
        if len(f.queue) <= f.capacity:
            break
        # capacityを越えていれば、最も選好度の低い男性を離婚させる
        else:
            m = f.pop()
            p[m] += 1

