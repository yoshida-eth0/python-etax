"""
抽象 社会保険 -> 健康保険
"""
from abc import abstractmethod

from meta.社会保険 import I社会保険, 標準額区分, 都道府県名
from utils import intfloor


class 健康保険料率:
    def __init__(self, 特定保険料率: float, 基本保険料率: float):
        self.特定保険料率 = 特定保険料率
        self.基本保険料率 = 基本保険料率

    @property
    def 一般保険料率(self) -> float:
        return self.特定保険料率 + self.基本保険料率


class I健康保険(I社会保険):
    """
    定数データの抽象クラス
    健康保険

    参考：
        従業員に賞与を支給したときの手続き｜日本年金機構
        https://www.nenkin.go.jp/service/kounen/hokenryo/hoshu/20141203.html

        年間の標準賞与額の累計額が573万円を超えたとき｜日本年金機構
        https://www.nenkin.go.jp/shinsei/kounen/tekiyo/shoyo/20120314-01.html
    """
    @abstractmethod
    def 標準報酬額区分(self, 報酬月額: int) -> 標準額区分:
        """
        報酬月額に対応する標準報酬額の区分を返す

        被保険者が受け取る給与（基本給のほか残業手当や通勤手当などを含めた税引き前の給与）を一定の幅で区分した報酬月額に当てはめて決定した標準報酬月額
        """
        ...

    def 標準賞与額区分(self, 賞与額: int) -> 標準額区分:
        """
        賞与額に対応する標準賞与額の区分を返す

        標準賞与額の上限は、健康保険では年度の累計額573万円（年度は毎年4月1日から翌年3月31日まで）
        年4回以上支給される賞与については、標準報酬月額の対象となる報酬とされ、標準賞与額の対象となる賞与とはされません。
        TODO: 年度の累計額
        """
        賞与額 = intfloor(賞与額, 3)
        賞与額 = min(賞与額, 5_730_000)
        return 標準額区分(None, 賞与額)

    @abstractmethod
    def 保険料率(self, 都道府県: 都道府県名) -> 健康保険料率:
        """
        年度に対応する都道府県単位保険料率を返す
        """
        ...
