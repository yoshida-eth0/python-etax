# 所得税青色申告決算書

import pandas as pd
from utils import ゼロ以上


class 売上原価:
    """
    所得税青色申告決算書 損益計算書
    2~6. 売上原価
    """

    def __init__(self):
        # 2. 期首商品(製品) 棚卸高
        self.期首商品_棚卸高: int = 0

        # 3. 仕入金額(製品製造)
        self.仕入金額: int = 0

        # 5. 期末商品 (製品) 棚卸高
        self.期末商品_棚卸高: int = 0

    @property
    def 小計(self) -> int:
        """
        4. 小計
        """
        return self.期首商品_棚卸高 + self.仕入金額

    @property
    def 差引原価(self) -> int:
        """
        6. 差引原価
        """
        return self.小計 - self.期末商品_棚卸高

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['2', '期首商品(製品) 棚卸高', self.期首商品_棚卸高],
            ['3', '仕入金額(製品製造)', self.仕入金額],
            ['4', '小計', self.小計],
            ['5', '期末商品 (製品) 棚卸高', self.期末商品_棚卸高],
            ['6', '差引原価', self.差引原価],
        ], columns=['key', 'label', 'value'])


class 経費:
    """
    所得税青色申告決算書 損益計算書
    8~32. 経費
    """

    def __init__(self):
        # 8. 租税公課
        self.租税公課: int = 0

        # 9. 荷造運賃
        self.荷造運賃: int = 0

        # 10. 水道光熱費
        self.水道光熱費: int = 0

        # 11. 旅費交通費
        self.旅費交通費: int = 0

        # 12. 通信費
        self.通信費: int = 0

        # 13. 広告宣伝費
        self.広告宣伝費: int = 0

        # 14. 接待交際費
        self.接待交際費: int = 0

        # 15. 損害保険料
        self.損害保険料: int = 0

        # 16. 修繕費
        self.修繕費: int = 0

        # 17. 消耗品費
        self.消耗品費: int = 0

        # 18. 減価償却費
        self.減価償却費: int = 0

        # 19. 福利厚生費
        self.福利厚生費: int = 0

        # 20. 給料賃金
        self.給料賃金: int = 0

        # 21. 外注工賃
        self.外注工賃: int = 0

        # 22. 利子割引料
        self.利子割引料: int = 0

        # 23. 地代家賃
        self.地代家賃: int = 0

        # 24. 貸倒金
        self.貸倒金: int = 0

        # 25
        self.label25: str = ''
        self.value25: int = 0

        # 26
        self.label26: str = ''
        self.value26: int = 0

        # 27
        self.label27: str = ''
        self.value27: int = 0

        # 28
        self.label28: str = ''
        self.value28: int = 0

        # 29
        self.label29: str = ''
        self.value29: int = 0

        # 30
        self.label30: str = ''
        self.value30: int = 0

        # 31. 雑費
        self.雑費: int = 0

    @property
    def 計(self):
        """
        32. 計
        """
        total = 0
        total += self.租税公課
        total += self.荷造運賃
        total += self.水道光熱費
        total += self.旅費交通費
        total += self.通信費
        total += self.広告宣伝費
        total += self.接待交際費
        total += self.損害保険料
        total += self.修繕費
        total += self.消耗品費
        total += self.減価償却費
        total += self.福利厚生費
        total += self.給料賃金
        total += self.外注工賃
        total += self.利子割引料
        total += self.地代家賃
        total += self.貸倒金
        total += self.value25
        total += self.value26
        total += self.value27
        total += self.value28
        total += self.value29
        total += self.value30
        total += self.雑費
        return total

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['8', '租税公課', self.租税公課],
            ['9', '荷造運賃', self.荷造運賃],
            ['10', '水道光熱費', self.水道光熱費],
            ['11', '旅費交通費', self.旅費交通費],
            ['12', '通信費', self.通信費],
            ['13', '広告宣伝費', self.広告宣伝費],
            ['14', '接待交際費', self.接待交際費],
            ['15', '損害保険料', self.損害保険料],
            ['16', '修繕費', self.修繕費],
            ['17', '消耗品費', self.消耗品費],
            ['18', '減価償却費', self.減価償却費],
            ['19', '福利厚生費', self.福利厚生費],
            ['20', '給料賃金', self.給料賃金],
            ['21', '外注工賃', self.外注工賃],
            ['22', '利子割引料', self.利子割引料],
            ['23', '地代家賃', self.地代家賃],
            ['24', '貸倒金', self.貸倒金],
            ['25', self.label25, self.value25],
            ['26', self.label26, self.value26],
            ['27', self.label27, self.value27],
            ['28', self.label28, self.value28],
            ['29', self.label29, self.value29],
            ['30', self.label30, self.value30],
            ['31', '雑費', self.雑費],
            ['32', '計', self.計]
        ], columns=['key', 'label', 'value'])



class 各種引当金準備金等_繰戻額等:
    """
    所得税青色申告決算書 損益計算書
    34~37. 各種引当金・準備金等 -> 繰戻額等
    """

    def __init__(self):
        # 34. 貸倒引当金
        self.貸倒引当金: int = 0

        # 35
        self.label35: str = ''
        self.value35: int = 0

        # 36
        self.label36: str = ''
        self.value36: int = 0

    @property
    def 計(self):
        """
        37. 計
        """
        total = 0
        total += self.貸倒引当金
        total += self.value35
        total += self.value36
        return total

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['34', '貸倒引当金', self.貸倒引当金],
            ['35', self.label35, self.value35],
            ['36', self.label36, self.value36],
            ['37', '計', self.計],
        ], columns=['key', 'label', 'value'])


class 各種引当金準備金等_繰入額等:
    """
    所得税青色申告決算書 損益計算書
    38~42. 各種引当金・準備金等 -> 繰入額等
    """

    def __init__(self):
        # 38. 専従者給与
        self.専従者給与: int = 0

        # 39. 貸倒引当金
        self.貸倒引当金: int = 0

        # 40
        self.label40: str = ''
        self.value40: int = 0

        # 41
        self.label41: str = ''
        self.value41: int = 0

    @property
    def 計(self):
        """
        42. 計
        """
        total = 0
        total += self.専従者給与
        total += self.貸倒引当金
        total += self.value40
        total += self.value41
        return total

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['38', '専従者給与', self.専従者給与],
            ['39', '貸倒引当金', self.貸倒引当金],
            ['40', self.label40, self.value40],
            ['41', self.label41, self.value41],
            ['42', '計', self.計],
        ], columns=['key', 'label', 'value'])


class 損益計算書:
    """
    所得税青色申告決算書 損益計算書
    """

    def __init__(self, 売上金額: int = 0, x売上原価: 売上原価|None = None, x経費: 経費|None = None, x各種引当金準備金等_繰戻額等: 各種引当金準備金等_繰戻額等|None = None, x各種引当金準備金等_繰入額等: 各種引当金準備金等_繰入額等|None = None):
        # 1. 売上(収入)金額 (雑収入を含む)
        self.売上金額: int = 売上金額

        # 2~6. 売上原価
        self.売上原価 = x売上原価 or 売上原価()

        # 8~32. 経費
        self.経費 = x経費 or 経費()

        # 34~37. 各種引当金・準備金等 -> 繰戻額等
        self.各種引当金準備金等_繰戻額等 = x各種引当金準備金等_繰戻額等 or 各種引当金準備金等_繰戻額等()

        # 38~42. 各種引当金・準備金等 -> 繰入額等
        self.各種引当金準備金等_繰入額等 = x各種引当金準備金等_繰入額等 or 各種引当金準備金等_繰入額等()

    @property
    @ゼロ以上
    def 売上_差引金額(self) -> int:
        """
        7. 差引金額
        """
        return self.売上金額 - self.売上原価.差引原価

    @property
    @ゼロ以上
    def 経費_差引金額(self) -> int:
        """
        33. 差引金額
        """
        return self.売上_差引金額 - self.経費.計

    @property
    @ゼロ以上
    def 青色申告特別控除前の所得金額(self) -> int:
        """
        43. 青色申告特別控除前の所得金額
        """
        return self.経費_差引金額 + self.各種引当金準備金等_繰戻額等.計 - self.各種引当金準備金等_繰入額等.計

    @property
    def 青色申告特別控除額(self) -> int:
        """
        44. 青色申告特別控除額
        """
        return 650_000

    @property
    @ゼロ以上
    def 所得金額(self) -> int:
        """
        45. 所得金額
        """
        return self.青色申告特別控除前の所得金額 - self.青色申告特別控除額

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        df = pd.DataFrame([
            ['1', '売上(収入)金額 (雑収入を含む)', self.売上金額],
            ['7', '差引金額', self.売上_差引金額],
            ['33', '差引金額', self.経費_差引金額],
            ['43', '青色申告特別控除前の所得金額', self.青色申告特別控除前の所得金額],
            ['44', '青色申告特別控除額', self.青色申告特別控除額],
            ['45', '所得金額', self.所得金額],
        ], columns=['key', 'label1', 'value'])

        # 売上原価
        df2 = self.売上原価.to_dataframe()
        df2['label1'] = '売上原価'
        df2.rename(columns={'label': 'label2'}, inplace=True)
        df = pd.concat([df, df2], ignore_index=True)

        # 経費
        df2 = self.経費.to_dataframe()
        df2['label1'] = '経費'
        df2.rename(columns={'label': 'label2'}, inplace=True)
        df = pd.concat([df, df2], ignore_index=True)

        # 各種引当金準備金等 -> 繰戻額等
        df2 = self.各種引当金準備金等_繰戻額等.to_dataframe()
        df2['label1'] = '各種引当金準備金等'
        df2['label2'] = '繰戻額等'
        df2.rename(columns={'label': 'label3'}, inplace=True)
        df = pd.concat([df, df2], ignore_index=True)

        # 各種引当金準備金等 -> 繰入額等
        df2 = self.各種引当金準備金等_繰入額等.to_dataframe()
        df2['label1'] = '各種引当金準備金等'
        df2['label2'] = '繰入額等'
        df2.rename(columns={'label': 'label3'}, inplace=True)
        df = pd.concat([df, df2], ignore_index=True)

        df = df.sort_values('key', key=lambda x: x.astype(int)).reset_index(drop=True)
        df = df[['key', 'label1', 'label2', 'label3', 'value']]
        return df
