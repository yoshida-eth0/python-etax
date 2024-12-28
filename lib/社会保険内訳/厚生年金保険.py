from context import get_context
from meta.厚生年金保険 import 厚生年金保険料率
from meta.社会保険 import 標準額区分
from 社会保険内訳.base import 社会保険Base, 種類別保険料


class 種類別厚生年金保険料(種類別保険料):
    """
    保険料の種類別の1ヶ月分の厚生年金保険料
    """
    def __init__(self, 標準額区分: 標準額区分, 厚生年金保険料率: 厚生年金保険料率):
        self.標準額区分 = 標準額区分
        self.厚生年金保険料率 = 厚生年金保険料率

    @property
    def 保険料額_全額(self) -> int:
        """
        厚生年金保険料額(全額)
        """
        return round(self.標準額区分.月額 * self.厚生年金保険料率.厚生年金保険料率)

    @property
    def 保険料額_折半額(self) -> int:
        """
        厚生年金保険料額(折半額)
        """
        return round(self.保険料額_全額 / 2)

    @property
    def 子ども子育て拠出金(self) -> int:
        """
        子ども・子育て拠出金
        事業主が全額負担
        """
        return round(self.標準額区分.月額 * self.厚生年金保険料率.子ども子育て拠出金率)

    @property
    def 被保険者負担額(self) -> int:
        """
        被保険者が負担する総額
        """
        return self.保険料額_折半額

    @property
    def 事業主負担額(self) -> int:
        """
        事業主が負担する総額
        """
        return self.保険料額_折半額 + self.子ども子育て拠出金


class 厚生年金保険(社会保険Base):
    def __init__(self, 報酬月額: int, 賞与額: int):
        """
        1ヶ月分の厚生年金保険料

        args:
            報酬月額 (int): 一般的には4〜6月の月額の平均
            賞与額 (int): 賞与額

        参考：
            厚生年金保険の保険料｜日本年金機構
            https://www.nenkin.go.jp/service/kounen/hokenryo/hoshu/20150515-01.html

            令和6年度 算定基礎届事務説明｜日本年金機構
            https://www.nenkin.go.jp/service/doga/doga_kounen/santeisetsumei.html
        """
        self.報酬月額 = 報酬月額
        self.賞与額 = 賞与額

        impl = get_context().厚生年金保険
        if impl is None:
            raise NotImplementedError('Context.厚生年金保険')

        # 種類別の厚生年金保険料
        self.月額保険料 = 種類別厚生年金保険料(impl.標準報酬額区分(報酬月額), impl.保険料率)
        self.賞与額保険料 = 種類別厚生年金保険料(impl.標準賞与額区分(賞与額), impl.保険料率)
