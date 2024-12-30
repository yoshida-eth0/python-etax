from context import get_context
from meta.社会保険 import 標準額区分
from meta.雇用保険 import 雇用保険料率
from 社会保険内訳.base import 社会保険Base, 種類別保険料
from 納税者 import 納税者


class 種類別雇用保険料(種類別保険料):
    """
    保険料の種類別の1ヶ月分の雇用保険料
    """
    def __init__(self, 標準額区分: 標準額区分, 雇用保険料率: 雇用保険料率):
        self.標準額区分 = 標準額区分
        self.雇用保険料率 = 雇用保険料率

    @property
    def 被保険者負担額(self) -> int:
        """
        被保険者が負担する総額
        """
        return round(self.標準額区分.月額 * self.雇用保険料率.労働者負担率)

    @property
    def 事業主負担額(self) -> int:
        """
        事業主が負担する総額
        """
        return round(self.標準額区分.月額 * self.雇用保険料率.事業主負担率)


class 雇用保険(社会保険Base):
    def __init__(self, 報酬月額: int, 賞与額: int, 納税者: 納税者):
        self.報酬月額 = 報酬月額
        self.賞与額 = 賞与額

        impl = get_context().雇用保険
        if impl is None:
            raise NotImplementedError('Context.雇用保険')

        # 種類別の雇用保険料
        保険料率 = impl.保険料率(納税者.事業の種類)
        self.月額保険料 = 種類別雇用保険料(impl.標準報酬額区分(報酬月額), 保険料率)
        self.賞与額保険料 = 種類別雇用保険料(impl.標準賞与額区分(賞与額), 保険料率)
