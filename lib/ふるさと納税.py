from bisect import bisect_left

from 住民税 import 住民税, 住民税の税額
from 所得税及び復興特別所得税の申告内容確認表 import 所得税及び復興特別所得税の申告内容確認表_第一表, 所得金額等
from 控除データ import 控除データ


def ふるさと納税控除上限額(所得金額等: 所得金額等, 控除データ: 控除データ):
    """
    ふるさと納税の控除上限額を算出する

    args:
        所得金額等 (所得金額等): 所得金額等
        控除データ (控除データ): 控除の算出に用いるデータ、ふるさと納税額は無視される
    """
    # 所得税及び復興特別所得税の申告内容確認表_第一表
    x所得税及び復興特別所得税の申告内容確認表_第一表 = 所得税及び復興特別所得税の申告内容確認表_第一表(所得金額等=所得金額等, 控除データ=控除データ)

    # 住民税
    x住民税 = 住民税(所得税_所得控除=x所得税及び復興特別所得税の申告内容確認表_第一表.所得税_所得控除, 控除データ=控除データ)

    def ふるさと納税控除上限額_区分別(住民税の税額: 住民税の税額):
        """
        区分ごとのふるさと納税の控除上限額を算出する
        """
        def kihu_to_koujo(kihu: int):
            """
            ふるさと納税額から特例控除額に変換する
            """
            控除データ.ふるさと納税額 = kihu
            return 住民税の税額.寄附金税額控除_ふるさと納税_特例控除額

        # 控除額の上限
        max_koujo = 住民税の税額.寄附金税額控除_ふるさと納税_特例控除額上限

        # 二分探索する幅
        kihu_l = 0
        kihu_r = 100_000
        koujo = kihu_to_koujo(kihu_r)

        while koujo!=max_koujo:
            kihu_l = kihu_r
            kihu_r = kihu_l * 2
            koujo = kihu_to_koujo(kihu_r)

        # 二分探索
        return bisect_left(range(kihu_l, kihu_r), max_koujo, key=kihu_to_koujo) + kihu_l

    return min(map(ふるさと納税控除上限額_区分別, x住民税.住民税の税額一覧))
