import pandas as pd
from 社会保険内訳.base import 社会保険Base
from 社会保険内訳.介護保険 import 介護保険
from 社会保険内訳.健康保険 import 健康保険
from 社会保険内訳.厚生年金保険 import 厚生年金保険
from 社会保険内訳.雇用保険 import 雇用保険
from 納税者 import 納税者


class 社会保険:
    """
    社会保険に属する保険の合計

    TODO: 労災保険
    """
    def __init__(self, 報酬月額: int, 賞与額: int, 納税者: 納税者):
        self.内訳: dict[str, 社会保険Base] = {
            '厚生年金保険': 厚生年金保険(報酬月額, 賞与額),
            '健康保険': 健康保険(報酬月額, 賞与額, 納税者),
            '介護保険': 介護保険(報酬月額, 賞与額, 納税者),
            '雇用保険': 雇用保険(報酬月額, 賞与額, 納税者),
        }

    @property
    def 被保険者負担額(self) -> int:
        """
        被保険者が負担する総額
        """
        return sum([保険.被保険者負担額 for 保険 in self.内訳.values()])

    @property
    def 事業主負担額(self) -> int:
        """
        事業主が負担する総額
        """
        return sum([保険.事業主負担額 for 保険 in self.内訳.values()])

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame(
            [[保険名, 保険.被保険者負担額, 保険.事業主負担額] for 保険名, 保険 in self.内訳.items()],
            columns=['保険名', '被保険者負担額', '事業主負担額']
        )
