from context import get_context
from meta.社会保険 import 標準額区分
from 社会保険内訳.base import 社会保険Base, 種類別保険料
from 納税者 import 納税者


class 種類別介護保険料(種類別保険料):
    """
    保険料の種類別の1ヶ月分の介護保険料
    """
    def __init__(self, 標準額区分: 標準額区分, 介護保険料率: float):
        self.標準額区分 = 標準額区分
        self.介護保険料率 = 介護保険料率

    @property
    def 保険料額_全額(self) -> int:
        """
        介護保険料額(全額)
        """
        return round(self.標準額区分.月額 * self.介護保険料率)

    @property
    def 保険料額_折半額(self) -> int:
        """
        介護保険料額(折半額)
        """
        return round(self.保険料額_全額 / 2)

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
        return self.保険料額_折半額


class 介護保険(社会保険Base):
    def __init__(self, 報酬月額: int, 賞与額: int, 納税者: 納税者):
        self.報酬月額 = 報酬月額
        self.賞与額 = 賞与額

        impl = get_context().介護保険
        if impl is None:
            raise NotImplementedError('Context.介護保険')

        # 種類別の介護保険料
        保険料率 = impl.保険料率(納税者.納税者本人.年齢)
        self.月額保険料 = 種類別介護保険料(impl.標準報酬額区分(報酬月額), 保険料率)
        self.賞与額保険料 = 種類別介護保険料(impl.標準賞与額区分(賞与額), 保険料率)
