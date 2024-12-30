
from abc import abstractmethod

from meta.社会保険 import I社会保険, 事業の種類名, 標準額区分
from utils import intfloor


class 雇用保険料率:
    def __init__(self, 失業等給付_育児休業給付の保険料率: float, 雇用保険二事業の保険料率: float):
        self.失業等給付_育児休業給付の保険料率 = 失業等給付_育児休業給付の保険料率
        self.雇用保険二事業の保険料率 = 雇用保険二事業の保険料率

    @property
    def 労働者負担率(self) -> float:
        return self.失業等給付_育児休業給付の保険料率

    @property
    def 事業主負担率(self) -> float:
        return self.失業等給付_育児休業給付の保険料率 + self.雇用保険二事業の保険料率

    @property
    def 雇用保険料率(self) -> float:
        return self.労働者負担率 + self.事業主負担率


class I雇用保険(I社会保険):
    """
    定数データの抽象クラス
    雇用保険

    参考：
        雇用保険料率について ｜厚生労働省
        https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000108634.html
    """
    def 標準報酬額区分(self, 報酬月額: int) -> 標準額区分:
        """
        報酬月額を返す
        """
        return 標準額区分(None, 報酬月額)

    def 標準賞与額区分(self, 賞与額: int) -> 標準額区分:
        """
        賞与額を返す
        """
        return 標準額区分(None, 賞与額)

    @abstractmethod
    def 保険料率(self, 事業の種類: 事業の種類名) -> 雇用保険料率:
        """
        年度と事業の種類に対する保険料率を返す
        """
        ...
