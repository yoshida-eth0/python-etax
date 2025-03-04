import math
from functools import wraps

import pandas as pd
from context import get_context
from meta.住民税 import 住民税の税率
from meta.所得税 import 所得税の税率
from utils import intfloor, ゼロ以上
from 所得税及び復興特別所得税の申告内容確認表_第一表 import 所得税_所得控除, 所得金額等
from 納税者 import 納税者


class 住民税_所得控除:
    """
    住民税の所得控除
    (2) 所得控除の内訳

    対象:
        雑損控除 (TODO)
        医療費控除 (TODO)
        社会保険料控除
        小規模企業共済等掛金控除
        生命保険料控除 (TODO)
        地震保険料控除 (TODO)
        障害者控除 (TODO)
        寡婦控除 (TODO)
        ひとり親控除 (TODO)
        勤労学生控除 (TODO)
        配偶者控除 (TODO)
        配偶者特別控除 (TODO)
        扶養控除 (TODO)
        基礎控除
    """
    def __init__(self, 所得金額等: 所得金額等, 納税者: 納税者):
        self.所得金額等 = 所得金額等
        self.納税者 = 納税者

    @property
    def 雑損控除(self) -> int:
        """
        雑損控除
        (2) 所得控除の内訳 -> 控除金額 -> 雑損控除
        """
        if self.納税者.雑損.損失金額>0:
            raise NotImplementedError('雑損控除')
        return 0

    @property
    def 医療費控除(self) -> int:
        """
        医療費控除
        (2) 所得控除の内訳 -> 控除金額 -> 医療費控除
        """
        if self.納税者.医療費.医療費の実質負担額>0 or self.納税者.医療費.スイッチOTC医薬品の実質負担額>0:
            raise NotImplementedError('医療費控除')
        return 0

    @property
    def 社会保険料控除(self) -> int:
        """
        社会保険料控除
        (2) 所得控除の内訳 -> 控除金額 -> 社会保険料控除
        """
        return self.納税者.社会保険料

    @property
    def 小規模企業共済等掛金控除(self) -> int:
        """
        小規模企業共済等掛金控除
        (2) 所得控除の内訳 -> 控除金額 -> 小規模企業共済等掛金控除
        """
        return self.納税者.小規模企業共済等掛金

    @property
    def 生命保険料控除(self) -> int:
        """
        生命保険料控除
        (2) 所得控除の内訳 -> 控除金額 -> 生命保険料控除
        """
        if self.納税者.生命保険料>0:
            raise NotImplementedError('生命保険料控除')
        return 0

    @property
    def 地震保険料控除(self) -> int:
        """
        地震保険料控除
        (2) 所得控除の内訳 -> 控除金額 -> 地震保険料控除
        """
        if self.納税者.地震保険料>0:
            raise NotImplementedError('地震保険料控除')
        return 0

    @property
    def 障害者控除(self) -> int:
        """
        障害者控除
        (2) 所得控除の内訳 -> 控除金額 -> 障害者控除
        """
        if len(self.納税者.障害者一覧)>0:
            raise NotImplementedError('障害者控除')
        return 0

    @property
    def 寡婦控除(self) -> int:
        """
        寡婦控除
        (2) 所得控除の内訳 -> 控除金額 -> 寡婦控除
        """
        if self.納税者.is_寡婦:
            raise NotImplementedError('寡婦控除')
        return 0

    @property
    def ひとり親控除(self) -> int:
        """
        ひとり親控除
        (2) 所得控除の内訳 -> 控除金額 -> ひとり親控除
        """
        if self.納税者.is_ひとり親:
            raise NotImplementedError('ひとり親控除')
        return 0

    @property
    def 勤労学生控除(self) -> int:
        """
        勤労学生控除
        (2) 所得控除の内訳 -> 控除金額 -> 勤労学生控除
        """
        if self.納税者.納税者本人.is_勤労学生:
            raise NotImplementedError('勤労学生控除')
        return 0

    @property
    def 配偶者控除(self) -> int:
        """
        配偶者控除
        (2) 所得控除の内訳 -> 控除金額 -> 配偶者控除
        """
        if self.納税者.配偶者 is not None:
            raise NotImplementedError('配偶者控除')
        return 0

    @property
    def 配偶者特別控除(self) -> int:
        """
        配偶者特別控除
        (2) 所得控除の内訳 -> 控除金額 -> 配偶者特別控除
        """
        if self.納税者.配偶者 is not None:
            raise NotImplementedError('配偶者特別控除')
        return 0

    @property
    def 扶養控除(self) -> int:
        """
        扶養控除
        (2) 所得控除の内訳 -> 控除金額 -> 扶養控除
        """
        if len(self.納税者.扶養親族一覧)>0:
            raise NotImplementedError('扶養控除')
        return 0

    @property
    def 基礎控除(self) -> int:
        """
        基礎控除
        (2) 所得控除の内訳 -> 控除金額 -> 基礎控除
        """
        impl = get_context().住民税_基礎控除
        if impl is None:
            raise NotImplementedError('Context.住民税_基礎控除')

        return impl.住民税_基礎控除(self.所得金額等.合計所得金額)

    @property
    def 控除合計(self) -> int:
        """
        控除合計
        (2) 所得控除の内訳 -> 控除金額 -> 控除合計
        """
        total = 0
        total += self.雑損控除
        total += self.医療費控除
        total += self.社会保険料控除
        total += self.小規模企業共済等掛金控除
        total += self.生命保険料控除
        total += self.地震保険料控除
        total += self.障害者控除
        total += self.寡婦控除
        total += self.ひとり親控除
        total += self.勤労学生控除
        total += self.配偶者控除
        total += self.配偶者特別控除
        total += self.扶養控除
        total += self.基礎控除
        return total

    @property
    def 人的控除額(self) -> int:
        """
        人的控除額
        障害者控除、寡婦控除、ひとり親控除、勤労学生控除、配偶者控除、配偶者特別控除、扶養控除、基礎控除の合計
        """
        total = 0
        total += self.障害者控除
        total += self.寡婦控除
        total += self.ひとり親控除
        total += self.勤労学生控除
        total += self.配偶者控除
        total += self.配偶者特別控除
        total += self.扶養控除
        total += self.基礎控除
        return total

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['控除金額', '雑損控除', self.雑損控除],
            ['控除金額', '医療費控除', self.医療費控除],
            ['控除金額', '社会保険料控除', self.社会保険料控除],
            ['控除金額', '小規模企業共済等掛金控除', self.小規模企業共済等掛金控除],
            ['控除金額', '生命保険料控除', self.生命保険料控除],
            ['控除金額', '地震保険料控除', self.地震保険料控除],
            ['控除金額', '障害者控除', self.障害者控除],
            ['控除金額', '寡婦控除', self.寡婦控除],
            ['控除金額', 'ひとり親控除', self.ひとり親控除],
            ['控除金額', '勤労学生控除', self.勤労学生控除],
            ['控除金額', '配偶者控除', self.配偶者控除],
            ['控除金額', '配偶者特別控除', self.配偶者特別控除],
            ['控除金額', '扶養控除', self.扶養控除],
            ['控除金額', '基礎控除', self.基礎控除],
            ['控除金額', '控除合計', self.控除合計],
            ['控除金額', '人的控除額', self.人的控除額],
        ], columns=['label1', 'label2', 'value'])


class 課税標準額:
    """
    (3) 課税標準額
    """
    def __init__(self, 住民税_所得控除: 住民税_所得控除):
        self.所得金額等 = 住民税_所得控除.所得金額等
        self.住民税_所得控除 = 住民税_所得控除

    @property
    @ゼロ以上
    def 総所得(self) -> int:
        """
        総所得
        (3) 課税標準額 -> 課税標準額 -> 総所得
        """
        return intfloor(self.所得金額等.総所得金額等 - self.住民税_所得控除.控除合計, 3)

    @property
    @ゼロ以上
    def 課税総所得金額(self) -> int:
        """
        課税総所得金額（課税所得金額、課税対象額、課税標準額）
        総所得金額から所得控除を差し引いた額
        ・申告分離課税を加算する
        ・繰越控除適用後の金額
        ・所得控除を差し引く

        参考:
            住民税の具体的な計算例 | 中野区
            https://www.city.tokyo-nakano.lg.jp/kurashi/zeikin/jyuminzei-kazei/jyuminzei-keisanrei.html
        """
        return intfloor(self.所得金額等.総所得金額等 - self.住民税_所得控除.控除合計, 3)

    @property
    @ゼロ以上
    def 合計課税所得金額(self) -> int:
        """
        合計課税所得金額
        課税総所得金額 + 課税退職所得金額 + 課税山林所得
        ・申告分離課税を加算する
        ・繰越控除適用後の金額
        ・所得控除を差し引く

        参考:
            住民税の具体的な計算例 | 中野区
            https://www.city.tokyo-nakano.lg.jp/kurashi/zeikin/jyuminzei-kazei/jyuminzei-keisanrei.html
        """
        return intfloor(self.所得金額等.総所得金額等 - self.住民税_所得控除.控除合計, 3)

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['課税標準額', '総所得', self.総所得],
        ], columns=['label1', 'label2', 'value'])


def 所得割区分割合適用(func) -> int:
    """
    所得割区分割合を適用するデコレータ
    """
    @wraps(func)
    def wrapper(self: '住民税の税額', *args, **kwargs) -> int:
        return math.floor(func(self, *args, **kwargs) * self.所得割区分割合)
    return wrapper

class 住民税の税額:
    """
    住民税の区分ごとの税額
    (4) 合計税額 -> 税額
    """
    def __init__(self, 課税標準額: 課税標準額, 所得税_所得控除: 所得税_所得控除, 住民税_所得控除: 住民税_所得控除, 住民税の税率: 住民税の税率, 合計所得割: float, 納税者: 納税者):
        # 課税標準額
        self.課税標準額 = 課税標準額

        # 所得税の所得控除
        self.所得税_所得控除 = 所得税_所得控除

        # 住民税の所得控除
        self.住民税_所得控除 = 住民税_所得控除

        # 住民税の区分税率と区分割合
        self.住民税の税率 = 住民税の税率
        self.合計所得割 = 合計所得割
        self.所得割区分割合 = round(住民税の税率.所得割 / 合計所得割, 3)

        # 住民税の税額控除
        self.納税者 = 納税者

    @property
    def 所得割合計額(self) -> int:
        """
        所得割合計額
        (4) 合計税額 -> 税額 -> 所得割合計額
        """
        return math.floor(self.課税標準額.課税総所得金額 * self.住民税の税率.所得割)

    @property
    @所得割区分割合適用
    def 調整控除(self):
        """
        調整控除
        (4) 合計税額 -> 税額 -> 調整控除

        参考:
            住民税の具体的な計算例 | 中野区
            https://www.city.tokyo-nakano.lg.jp/kurashi/zeikin/jyuminzei-kazei/jyuminzei-keisanrei.html
        """
        if self.課税標準額.合計課税所得金額<=2_000_000:
            # 合計課税所得金額が200万円以下の場合

            # 1. 所得税と住民税の人的控除額の差額
            var1 = self.人的控除差調整額

            # 2. 合計課税所得金額
            var2 = self.課税標準額.合計課税所得金額

            # 1または2のいずれか少ない金額の5%
            var = min(var1, var2)
            var = math.floor(var * 0.05)
            return var

        elif self.課税標準額.合計課税所得金額<=25_000_000:
            # 合計課税所得金額が200万円を超え、2,500万円以下の場合

            # 1. 所得税と住民税の人的控除額の差額
            var1 = self.人的控除差調整額

            # 2. 合計課税所得金額 - 200万円
            var2 = self.課税標準額.合計課税所得金額 - 2_000_000

            # 1から2を控除した金額（5万円を下回る場合は5万円）の5%
            var = max(var1 - var2, 50_000)
            var = math.floor(var * 0.05)
            return var

        else:
            # 合計課税所得金額が2,500万円超の場合
            # 適用なし
            return 0

    @property
    def 人的控除差調整額(self) -> int:
        """
        人的控除差調整額

        人的控除差調整額とは
        https://www.city.toyohashi.lg.jp/secure/24173/jintekikoujo.pdf
        """
        return self.所得税_所得控除.人的控除額 - self.住民税_所得控除.人的控除額

    @property
    def 配当控除(self) -> int:
        """
        配当控除
        (4) 合計税額 -> 税額 -> 配当控除
        """
        # TODO
        return 0

    @property
    def 外国税額控除(self) -> int:
        """
        外国税額控除
        (4) 合計税額 -> 税額 -> 外国税額控除
        """
        # TODO
        return 0

    @property
    def 住宅借入金等特別控除(self) -> int:
        """
        住宅借入金等特別控除
        (4) 合計税額 -> 税額 -> 住宅借入金等特別控除
        """
        # TODO
        return 0

    @property
    def 所得税の限界税率(self) -> 所得税の税率:
        """
        所得税の限界税率
        住民税の課税総所得金額から人的控除差額を控除した金額で計算した課税総所得金額であてはめた所得税率

        参考:
            杉並区 令和6年度 わたしたちの区税 P15
            https://www.city.suginami.tokyo.jp/_res/projects/default_project/_page_/001/014/046/r6kuzei.pdf.pdf
        """
        impl = get_context().所得税_税率
        if impl is None:
            raise NotImplementedError('Context.所得税_税率')

        return impl.所得税の税率(self.課税標準額.課税総所得金額 - self.人的控除差調整額)

    @property
    def 寄附金税額控除_ふるさと納税_基本控除額(self) -> int:
        """
        寄附金税額控除 ふるさと納税 基本控除額

        参考:
            No.1155 ふるさと納税(寄附金税額控除)｜国税庁
            https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1155.htm

            総務省｜ふるさと納税のしくみ｜税金の控除について
            https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/furusato/mechanism/deduction.html
        """
        # (2) 住民税からの控除（基本分） = （ふるさと納税額－2,000円）×10％
        # なお、控除の対象となるふるさと納税額は、総所得金額等の30％が上限です。
        shotoku30per = math.ceil(self.課税標準額.課税総所得金額 * 0.30)
        hurusato = min(self.納税者.ふるさと納税額, shotoku30per)

        var1 = math.ceil((hurusato - 2_000) * self.住民税の税率.所得割)
        var1 = max(var1, 0)
        return var1

    @property
    def 寄附金税額控除_ふるさと納税_特例控除額(self) -> int:
        """
        寄附金税額控除 ふるさと納税 特例控除額

        参考:
            杉並区 令和6年度 わたしたちの区税 P15
            https://www.city.suginami.tokyo.jp/_res/projects/default_project/_page_/001/014/046/r6kuzei.pdf.pdf

            No.1155 ふるさと納税(寄附金税額控除)｜国税庁
            https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1155.htm

            総務省｜ふるさと納税のしくみ｜税金の控除について
            https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/furusato/mechanism/deduction.html

            手順3　所得から差し引かれる金額（所得控除）を計算する｜国税庁
            https://www.nta.go.jp/taxes/shiraberu/shinkoku/tebiki/2023/03/order3/3-3_12.htm
        """
        # (3) 住民税からの控除（特例分） = （ふるさと納税額 - 2,000円）×（100％ - 10％（基本分） - 所得税の税率）
        # 住民税からの控除の特例分は、この特例分が住民税所得割額の2割を超えない場合は、上記(3)の計算式で決まります。
        # 上記(3)における所得税の税率は、個人住民税の課税所得金額から人的控除差調整額を差し引いた金額により求めた所得税の税率であり、上記(1)の所得税の税率と異なる場合があります。
        # 控除額の計算において算出した金額に1円未満の端数があるときは、その端数を切り上げて差し支えありません。

        # 特例控除額＝（寄附金合計額－2,000円）×（90％－所得税の限界税率×1.021）（区民税3/5・都民税2/5）
        # 特例控除額は、所得割額（調整控除額控除後の額）の 20% を限度とします。
        zeiritsu = self.所得税の限界税率
        var3 = math.ceil((self.納税者.ふるさと納税額 - 2_000) * (1.0 - self.合計所得割 - zeiritsu.税率 * (1.0 + zeiritsu.復興特別所得税率)) * self.所得割区分割合)
        var3 = max(var3, 0)

        # (3)' 住民税からの控除（特例分） = （住民税所得割額）×20％
        # 特例分（(3)で計算した場合の特例分）が住民税所得割額の2割を超える場合は、上記(3)'の計算式となります。
        # この場合、(1)、(2)及び(3)'の3つの控除を合計しても（ふるさと納税額－2,000円）の全額が控除されず、実質負担額は2,000円を超えます。
        shotokuwari20per = self.寄附金税額控除_ふるさと納税_特例控除額上限
        if shotokuwari20per < var3:
            var3 = shotokuwari20per

        return var3

    @property
    def 寄附金税額控除_ふるさと納税_特例控除額上限(self) -> int:
        """
        寄附金税額控除 ふるさと納税 特例控除額の上限
        """
        return math.ceil(self.所得割合計額 * 0.20)

    @property
    def 寄附金税額控除_ふるさと納税_申告特例控除額(self) -> int:
        """
        寄附金税額控除 ふるさと納税 申告特例控除額
        ワンストップ特例制度を利用する場合

        参考:
            杉並区 令和6年度 わたしたちの区税 P15
            https://www.city.suginami.tokyo.jp/_res/projects/default_project/_page_/001/014/046/r6kuzei.pdf.pdf
        """
        # TODO
        # 申告特例控除額＝特例控除額×（所得税の限界税率×1.021）（区民税3/5・都民税2/5）
        if self.納税者.is_ワンストップ特例制度:
            raise NotImplementedError('is_ワンストップ特例制度')
        return 0

    @property
    def 寄附金税額控除_ふるさと納税(self) -> int:
        """
        寄附金税額控除 ふるさと納税
        """
        total = 0
        total += self.寄附金税額控除_ふるさと納税_基本控除額
        total += self.寄附金税額控除_ふるさと納税_特例控除額
        total += self.寄附金税額控除_ふるさと納税_申告特例控除額
        return total

    @property
    def 寄附金税額控除(self) -> int:
        """
        寄附金税額控除
        (4) 合計税額 -> 税額 -> 寄附金税額控除

        寄付先:
            1. 都道府県・区市町村(ふるさと納税)
            2. 東京都共同募金会 日本赤十字社東京都支部 (TODO)
            3. 東京都が条例で指定する団体 (TODO)
            4. 杉並区が条例で指定する団体 (TODO)
        参考:
            杉並区 令和6年度 わたしたちの区税 P15
            https://www.city.suginami.tokyo.jp/_res/projects/default_project/_page_/001/014/046/r6kuzei.pdf.pdf
        TODO:
            寄付先ごとにモジュール化
        """
        total = 0
        total += self.寄附金税額控除_ふるさと納税
        return total

    @property
    def 定額減税(self) -> int:
        """
        定額減税(令和6年度分のみ)
        (4) 合計税額 -> 税額 -> 定額減税
        """
        impl = get_context().住民税_税率一覧
        if impl is None:
            raise NotImplementedError('Context.住民税_税率一覧')

        if impl.住民税_定額減税対象可否(self.課税標準額.所得金額等.合計所得金額):
            return self.住民税の税率.定額減税 * (1 + self.納税者.控除対象配偶者又は扶養親族の人数)
        return 0

    @property
    def 税額控除合計(self) -> int:
        """
        税額控除の合計額
        """
        total = 0
        total += self.調整控除
        total += self.配当控除
        total += self.外国税額控除
        total += self.住宅借入金等特別控除
        total += self.寄附金税額控除
        total += self.定額減税
        return total

    @property
    def 差引所得割額(self) -> int:
        """
        差引所得割額
        (4) 合計税額 -> 税額 -> 差引所得割額
        """
        return intfloor(self.所得割合計額 - self.税額控除合計, 2)

    @property
    def 均等割額(self) -> int:
        """
        均等割額
        (4) 合計税額 -> 税額 -> 均等割額
        """
        return self.住民税の税率.均等割

    @property
    @ゼロ以上
    def 税額計(self) -> int:
        """
        区分に対する住民税の合計
        (4) 合計税額 -> 税額 -> 計
        """
        return self.差引所得割額 + self.均等割額

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        df = pd.DataFrame([
            ['所得割合計額', self.所得割合計額],
            ['調整控除', self.調整控除],
            ['人的控除差調整額', self.人的控除差調整額],
            ['配当控除', self.配当控除],
            ['外国税額控除', self.外国税額控除],
            ['住宅借入金等特別控除', self.住宅借入金等特別控除],
            ['寄附金税額控除 ふるさと納税 基本控除額', self.寄附金税額控除_ふるさと納税_基本控除額],
            ['寄附金税額控除 ふるさと納税 特例控除額', self.寄附金税額控除_ふるさと納税_特例控除額],
            ['寄附金税額控除 ふるさと納税 特例控除額上限', self.寄附金税額控除_ふるさと納税_特例控除額上限],
            ['寄附金税額控除 ふるさと納税 申告特例控除額', self.寄附金税額控除_ふるさと納税_申告特例控除額],
            ['寄附金税額控除 ふるさと納税', self.寄附金税額控除_ふるさと納税],
            ['寄附金税額控除', self.寄附金税額控除],
            ['定額減税', self.定額減税],
            ['税額控除合計', self.税額控除合計],
            ['差引所得割額', self.差引所得割額],
            ['均等割額', self.均等割額],
            ['計', self.税額計],
        ], columns=['label3', 'value'])
        df['label1'] = '税額'
        df['label2'] = self.住民税の税率.区分
        return df[['label1', 'label2', 'label3', 'value']]


class 住民税:
    """
    特別区民税・都民税・森林環境税 課税証明書
    """
    def __init__(self, 所得税_所得控除: 所得税_所得控除, 納税者: 納税者):
        # (1) 所得金額の内訳
        self.所得金額等 = 所得税_所得控除.所得金額等

        # (2) 所得控除の内訳
        self.住民税_所得控除 = 住民税_所得控除(self.所得金額等, 納税者)

        # (3) 課税標準額
        self.課税標準額 = 課税標準額(self.住民税_所得控除)

        # (4) 合計税額 -> 税額
        impl = get_context().住民税_税率一覧
        if impl is None:
            raise NotImplementedError('Context.住民税_税率一覧')

        住民税の税率一覧 = impl.住民税の税率一覧()
        合計所得割 = sum([住民税の税率.所得割 for 住民税の税率 in 住民税の税率一覧])
        self.住民税の税額一覧 = [住民税の税額(self.課税標準額, 所得税_所得控除, self.住民税_所得控除, 住民税の税率, 合計所得割, 納税者) for 住民税の税率 in 住民税の税率一覧]

    @property
    def 森林環境税額(self) -> int:
        """
        森林環境税額
        (4) 合計税額 -> 森林環境税額

        参考:
            森林環境税について/豊明市
            https://www.city.toyoake.lg.jp/18520.htm
        TODO:
            免除
        """
        return 1_000

    @property
    def 年税額(self) -> int:
        """
        住民税の合計
        (4) 合計税額 -> 年税額
        """
        total = sum([住民税の税額.税額計 for 住民税の税額 in self.住民税の税額一覧])
        total += self.森林環境税額
        return total

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        # (2) 所得控除の内訳
        df = self.住民税_所得控除.to_dataframe()
        df.rename(columns={'label1': 'label2', 'label2': 'label3'}, inplace=True)
        df['label1'] = '所得控除の内訳'

        # (3) 課税標準額
        df2 = self.課税標準額.to_dataframe()
        df2.rename(columns={'label1': 'label2', 'label2': 'label3'}, inplace=True)
        df2['label1'] = '課税標準額'
        df = pd.concat([df, df2], ignore_index=True)

        # (4) 合計税額 -> 税額
        for 住民税の税額 in self.住民税の税額一覧:
            df2 = 住民税の税額.to_dataframe()
            df2.rename(columns={'label1': 'label2', 'label2': 'label3', 'label3': 'label4'}, inplace=True)
            df2['label1'] = '合計税額'
            df = pd.concat([df, df2], ignore_index=True)

        # (4) 合計税額
        df2 = pd.DataFrame([
            ['森林環境税額', self.森林環境税額],
            ['住民税の合計', self.年税額],
        ], columns=['label1', 'value'])
        df = pd.concat([df, df2], ignore_index=True)

        df = df[['label1', 'label2', 'label3', 'label4', 'value']]
        return df
