# coding=utf8
import json
from typing import Dict, List, Set

import unicodedata

print(ord('alibaba'))

ranges = [
    # (ord(u"\u3300"), ord(u"\u33ff")),  # compatibility ideographs
    # (ord(u"\ufe30"), ord(u"\ufe4f")),  # compatibility ideographs
    # (ord(u"\uf900"), ord(u"\ufaff")),  # compatibility ideographs
    # (ord(u"\U0002F800"), ord(u"\U0002fa1f")),  # compatibility ideographs
    # (ord(u'\u3040'), ord(u'\u309f')),  # Japanese Hiragana
    # (ord(u"\u30a0"), ord(u"\u30ff")),  # Japanese Katakana
    # (ord(u"\u2e80"), ord(u"\u2eff")),  # CJK Radicals Supplement
    (ord(u"\u4e00"), ord(u"\u9fff")),  # CJK Unified Ideographs
    # (ord(u"\u3400"), ord(u"\u4dbf")),
    # (ord(u"\U00020000"), ord(u"\U0002a6df")),
    # (ord(u"\U0002a700"), ord(u"\U0002b73f")),
    # (ord(u"\U0002b740"), ord(u"\U0002b81f")),
    # (ord(u"\U0002b820"), ord(u"\U0002ceaf"))  # included as of Unicode 8.0
]


def check_is_cjk(char):
    return any([r[0] <= ord(char) <= r[1] for r in ranges])


kanji = """日 一 国 会 人 年 大 十 二 本 中 長 出 三 同 時 政 事 自 行 社 見 月 分 議 後 前 民 生 連 五 発 間 対 上 部 東 者 党 地 合 市 業 内 相 方 四 定 今 回 新 場 金 員 九 入 選 立 開 手 米 力 学 問 高 代 明 実 円 関 決 子 動 京 全 目 表 戦 経 通 外 最 言 氏 現 理 調 体 化 田 当 八 六 約 主 題 下 首 意 法 不 来 作 性 的 要 用 制 治 度 務 強 気 小 七 成 期 公 持 野 協 取 都 和 統 以 機 平 総 加 山 思 家 話 世 受 区 領 多 県 続 進 正 安 設 保 改 数 記 院 女 初 北 午 指 権 心 界 支 第 産 結 百 派 点 教 報 済 書 府 活 原 先 共 得 解 名 交 資 予 川 向 際 査 勝 面 委 告 軍 文 反 元 重 近 千 考 判 認 画 海 参 売 利 組 知 案 道 信 策 集 在 件 団 別 物 側 任 引 使 求 所 次 水 半 品 昨 論 計 死 官 増 係 感 特 情 投 示 変 打 男 基 私 各 始 島 直 両 朝 革 価 式 確 村 提 運 終 挙 果 西 勢 減 台 広 容 必 応 演 電 歳 住 争 談 能 無 再 位 置 企 真 流 格 有 疑 口 過 局 少 放 税 検 藤 町 常 校 料 沢 裁 状 工 建 語 球 営 空 職 証 土 与 急 止 送 援 供 可 役 構 木 割 聞 身 費 付 施 切 由 説 転 食 比 難 防 補 車 優 夫 研 収 断 井 何 南 石 足 違 消 境 神 番 規 術 護 展 態 導 鮮 備 宅 害 配 副 算 視 条 幹 独 警 宮 究 育 席 輸 訪 楽 起 万 着 乗 店 述 残 想 線 率 病 農 州 武 声 質 念 待 試 族 象 銀 域 助 労 例 衛 然 早 張 映 限 親 額 監 環 験 追 審 商 葉 義 伝 働 形 景 落 欧 担 好 退 準 賞 訴 辺 造 英 被 株 頭 技 低 毎 医 復 仕 去 姿 味 負 閣 韓 渡 失 移 差 衆 個 門 写 評 課 末 守 若 脳 極 種 美 岡 影 命 含 福 蔵 量 望 松 非 撃 佐 核 観 察 整 段 横 融 型 白 深 字 答 夜 製 票 況 音 申 様 財 港 識 注 呼 渉 達 

良 響 阪 帰 針 専 推 谷 古 候 史 天 階 程 満 敗 管 値 歌 買 突 兵 接 請 器 士 光 討 路 悪 科 攻 崎 督 授 催 細 効 図 週 積 丸 他 及 湾 録 処 省 旧 室 憲 太 橋 歩 離 岸 客 風 紙 激 否 周 師 摘 材 登 系 批 郎 母 易 健 黒 火 戸 速 存 花 春 飛 殺 央 券 赤 号 単 盟 座 青 破 編 捜 竹 除 完 降 超 責 並 療 従 右 修 捕 隊 危 採 織 森 競 拡 故 館 振 給 屋 介 読 弁 根 色 友 苦 就 迎 走 販 園 具 左 異 歴 辞 将 秋 因 献 厳 馬 愛 幅 休 維 富 浜 父 遺 彼 般 未 塁 貿 講 邦 舞 林 装 諸 夏 素 亡 劇 河 遣 航 抗 冷 模 雄 適 婦 鉄 寄 益 込 顔 緊 類 児 余 禁 印 逆 王 返 標 換 久 短 油 妻 暴 輪 占 宣 背 昭 廃 植 熱 宿 薬 伊 江 清 習 険 頼 僚 覚 吉 盛 船 倍 均 億 途 圧 芸 許 皇 臨 踏 駅 署 抜 壊 債 便 伸 留 罪 停 興 爆 陸 玉 源 儀 波 創 障 継 筋 狙 帯 延 羽 努 固 闘 精 則 葬 乱 避 普 散 司 康 測 豊 洋 静 善 逮 婚 厚 喜 齢 囲 卒 迫 略 承 浮 惑 崩 順 紀 聴 脱 旅 絶 級 幸 岩 練 押 軽 倒 了 庁 博 城 患 締 等 救 執 層 版 老 令 角 絡 損 房 募 曲 撤 裏 払 削 密 庭 徒 措 仏 績 築 貨 志 混 載 昇 池 陣 我 勤 為 血 遅 抑 幕 居 染 温 雑 招 奈 季 困 星 傷 永 択 秀 著 徴 誌 庫 弾 償 刊 像 功 拠 香 欠 更 秘 拒 刑 坂 刻 底 賛 塚 致 抱 繰 服 犯 尾 描 布 恐 寺 鈴 盤 息 宇 項 喪 伴 遠 養 懸 戻 街 巨 震 願 絵 希 越 契 掲 躍 棄 欲 痛 触 邸 依 籍 汚 縮 還 枚 属 笑 互 複 慮 郵 束 仲 栄 札 枠 似 夕 恵 板 列 露 沖 探 逃 借 緩 節 需 骨 射 傾 届 曜 遊 迷 夢 巻 購 揮 君 燃 充 雨 閉 緒 跡 包 駐 貢 鹿 弱 却 端 賃 折 紹 獲 郡 併 草 徹 飲 貴 埼 衝 焦 奪 雇 災 浦 暮 替 析 預 焼 簡 譲 称 肉 納 樹 挑 章 臓 律 誘 紛 貸 至 宗 促 慎 控 

贈 智 握 照 宙 酒 俊 銭 薄 堂 渋 群 銃 悲 秒 操 携 奥 診 詰 託 晴 撮 誕 侵 括 掛 謝 双 孝 刺 到 駆 寝 透 津 壁 稲 仮 暗 裂 敏 鳥 純 是 飯 排 裕 堅 訳 盗 芝 綱 吸 典 賀 扱 顧 弘 看 訟 戒 祉 誉 歓 勉 奏 勧 騒 翌 陽 閥 甲 快 縄 片 郷 敬 揺 免 既 薦 隣 悩 華 泉 御 範 隠 冬 徳 皮 哲 漁 杉 里 釈 己 荒 貯 硬 妥 威 豪 熊 歯 滞 微 隆 埋 症 暫 忠 倉 昼 茶 彦 肝 柱 喚 沿 妙 唱 祭 袋 阿 索 誠 忘 襲 雪 筆 吹 訓 懇 浴 俳 童 宝 柄 驚 麻 封 胸 娘 砂 李 塩 浩 誤 剤 瀬 趣 陥 斎 貫 仙 慰 賢 序 弟 旬 腕 兼 聖 旨 即 洗 柳 舎 偽 較 覇 兆 床 畑 慣 詳 毛 緑 尊 抵 脅 祝 礼 窓 柔 茂 犠 旗 距 雅 飾 網 竜 詩 昔 繁 殿 濃 翼 牛 茨 潟 敵 魅 嫌 魚 斉 液 貧 敷 擁 衣 肩 圏 零 酸 兄 罰 怒 滅 泳 礎 腐 祖 幼 脚 菱 荷 潮 梅 泊 尽 杯 僕 桜 滑 孤 黄 煕 炎 賠 句 寿 鋼 頑 甘 臣 鎖 彩 摩 浅 励 掃 雲 掘 縦 輝 蓄 軸 巡 疲 稼 瞬 捨 皆 砲 軟 噴 沈 誇 祥 牲 秩 帝 宏 唆 鳴 阻 泰 賄 撲 凍 堀 腹 菊 絞 乳 煙 縁 唯 膨 矢 耐 恋 塾 漏 紅 慶 猛 芳 懲 郊 剣 腰 炭 踊 幌 彰 棋 丁 冊 恒 眠 揚 冒 之 勇 曽 械 倫 陳 憶 怖 犬 菜 耳 潜 珍 梨 仁 克 岳 概 拘 墓 黙 須 偏 雰 卵 遇 湖 諮 狭 喫 卓 干 頂 虫 刷 亀 糧 梶 湯 箱 簿 炉 牧 殊 殖 艦 溶 輩 穴 奇 慢 鶴 謀 暖 昌 拍 朗 丈 鉱 寛 覆 胞 泣 涙 隔 浄 匹 没 暇 肺 孫 貞 靖 鑑 飼 陰 銘 鋭 随 烈 尋 渕 稿 枝 丹 啓 也 丘 棟 壌 漫 玄 粘 悟 舗 妊 塗 熟 軒 旭 恩 毒 騰 往 豆 遂 晩 狂 叫 栃 岐 陛 緯 培 衰 艇 屈 径 淡 抽 披 廷 錦 准 暑 拝 磯 奨 妹 浸 剰 胆 氷 繊 駒 乾 虚 棒 寒 孜 霊 帳 悔 諭 祈 惨 虐 翻 墜 沼 据 肥 徐 糖 搭 姉 髪 忙 盾 脈 滝 拾 軌 俵 妨 盧 粉 擦 鯨 漢 糸 荘 諾 雷 漂 懐 勘 綿 栽 才 拐 笠 駄 

添 汗 冠 斜 銅 鏡 聡 浪 亜 覧 詐 壇 勲 魔 酬 紫 湿 曙 紋 卸 奮 趙 欄 逸 涯 拓 眼 瓶 獄 筑 尚 阜 彫 咲 穏 顕 巧 矛 垣 召 欺 釣 缶 萩 粧 隻 葛 脂 粛 栗 愚 蒸 嘉 遭 架 篠 鬼 庶 肌 稚 靴 菅 滋 幻 煮 姫 誓 耕 把 践 呈 疎 仰 鈍 恥 剛 疾 征 砕 謡 嫁 謙 后 嘆 俣 菌 鎌 巣 泥 頻 琴 班 淵 棚 潔 酷 宰 廊 寂 辰 隅 偶 霞 伏 灯 柏 辛 磨 碁 俗 漠 邪 晶 辻 麦 墨 鎮 洞 履 劣 那 殴 娠 奉 憂 朴 亭 姓 淳 荻 筒 鼻 嶋 怪 粒 詞 鳩 柴 偉 酔 惜 穫 佳 潤 悼 乏 胃 該 赴 桑 桂 髄 虎 盆 晋 穂 壮 堤 飢 傍 疫 累 痴 搬 畳 晃 癒 桐 寸 郭 机 尿 凶 吐 宴 鷹 賓 虜 膚 陶 鐘 憾 畿 猪 紘 磁 弥 昆 粗 訂 芽 尻 庄 傘 敦 騎 寧 濯 循 忍 磐 猫 怠 如 寮 祐 鵬 塔 沸 鉛 珠 凝 苗 獣 哀 跳 灰 匠 菓 垂 蛇 澄 縫 僧 幾 眺 唐 亘 呉 凡 憩 鄭 芦 龍 媛 溝 恭 刈 睡 錯 伯 帽 笹 穀 柿 陵 霧 魂 枯 弊 釧 妃 舶 餓 腎 窮 掌 麗 綾 臭 釜 悦 刃 縛 暦 宜 盲 粋 辱 毅 轄 猿 弦 嶌 稔 窒 炊 洪 摂 飽 函 冗 涼 桃 狩 舟 貝 朱 渦 紳 枢 碑 鍛 刀 鼓 裸 鴨 符 猶 塊 旋 弓 幣 膜 扇 脇 腸 憎 槽 鍋 慈 皿 肯 樋 楊 伐 駿 漬 燥 糾 亮 墳 坪 畜 紺 慌 娯 吾 椿 舌 羅 坊 峡 俸 厘 峰 圭 醸 蓮 弔 乙 倶 汁 尼 遍 堺 衡 呆 薫 瓦 猟 羊 窪 款 閲 雀 偵 喝 敢 畠 胎 酵 憤 豚 遮 扉 硫 赦 挫 挟 窃 泡 瑞 又 慨 紡 恨 肪 扶 戯 伍 忌 濁 奔 斗 蘭 蒲 迅 肖 鉢 朽 殻 享 秦 茅 藩 沙 輔 曇 媒 鶏 禅 嘱 胴 粕 冨 迭 挿 湘 嵐 椎 灘 堰 獅 姜 絹 陪 剖 譜 郁 悠 淑 帆 暁 鷲 傑 楠 笛 芥 其 玲 奴 誰 錠 拳 翔 遷 拙 侍 尺 峠 篤 肇 渇 榎 俺 劉 幡 諏 叔 雌 亨 堪 叙 酢 吟 逓 痕 嶺 袖 甚 喬 崔 妖 琵 琶 聯 蘇 闇 崇 漆 岬 癖 愉 寅 捉 礁 乃 洲 屯 樽 樺 槙 薩 姻 巌 淀 麹 賭 擬 塀 唇 睦 閑 胡 幽 峻 曹 哨 詠 

炒 屏 卑 侮 鋳 抹 尉 槻 隷 禍 蝶 酪 茎 汎 頃 帥 梁 逝 滴 汽 謎 琢 箕 匿 爪 芭 逗 苫 鍵 襟 蛍 楢 蕉 兜 寡 琉 痢 庸 朋 坑 姑 烏 藍 僑 賊 搾 奄 臼 畔 遼 唄 孔 橘 漱 呂 桧 拷 宋 嬢 苑 巽 杜 渓 翁 藝 廉 牙 謹 瞳 湧 欣 窯 褒 醜 魏 篇 升 此 峯 殉 煩 巴 禎 枕 劾 菩 堕 丼 租 檜 稜 牟 桟 榊 錫 荏 惧 倭 婿 慕 廟 銚 斐 罷 矯 某 囚 魁 薮 虹 鴻 泌 於 赳 漸 逢 凧 鵜 庵 膳 蚊 葵 厄 藻 萬 禄 孟 鴈 狼 嫡 呪 斬 尖 翫 嶽 尭 怨 卿 串 已 嚇 巳 凸 暢 腫 粟 燕 韻 綴 埴 霜 餅 魯 硝 牡 箸 勅 芹 杏 迦 棺 儒 鳳 馨 斑 蔭 焉 慧 祇 摯 愁 鷺 楼 彬 袴 匡 眉 苅 讃 尹 欽 薪 湛 堆 狐 褐 鴎 瀋 挺 賜 嵯 雁 佃 綜 繕 狛 壷 橿 栓 翠 鮎 芯 蜜 播 榛 凹 艶 帖 伺 桶 惣 股 匂 鞍 蔦 玩 萱 梯 雫 絆 錬 湊 蜂 隼 舵 渚 珂 煥 衷 逐 斥 稀 癌 峨 嘘 旛 篭 芙 詔 皐 雛 娼 篆 鮫 椅 惟 牌 宕 喧 佑 蒋 樟 耀 黛 叱 櫛 渥 挨 憧 濡 槍 宵 襄 妄 惇 蛋 脩 笘 宍 甫 酌 蚕 壕 嬉 囃 蒼 餌 簗 峙 粥 舘 銕 鄒 蜷 暉 捧 頒 只 肢 箏 檀 鵠 凱 彗 謄 諌 樫 噂 脊 牝 梓 洛 醍 砦 丑 笏 蕨 噺 抒 嗣 隈 叶 凄 汐 絢 叩 嫉 朔 蔡 膝 鍾 仇 伽 夷 恣 瞑 畝 抄 杭 寓 麺 戴 爽 裾 黎 惰 坐 鍼 蛮 塙 冴 旺 葦 礒 咸 萌 饗 歪 冥 偲 壱 瑠 韮 漕 杵 薔 膠 允 眞 蒙 蕃 呑 侯 碓 茗 麓 瀕 蒔 鯉 竪 弧 稽 瘤 澤 溥 遥 蹴 或 訃 矩 厦 冤 剥 舜 侠 贅 杖 蓋 畏 喉 汪 猷 瑛 搜 曼 附 彪 撚 噛 卯 桝 撫 喋 但 溢 闊 藏 浙 彭 淘 剃 揃 綺 徘 巷 竿 蟹 芋 袁 舩 拭 茜 凌 頬 厨 犀 簑 皓 甦 洸 毬 檄 姚 蛭 婆 叢 椙 轟 贋 洒 貰 儲 緋 貼 諜 鯛 蓼 甕 喘 怜 溜 邑 鉾 倣 碧 燈 諦 煎 瓜 緻 哺 槌 啄 穣 嗜 偕 罵 酉 蹄 頚 胚 牢 糞 悌 吊 楕 鮭 乞 倹 嗅 詫 鱒 蔑 轍 醤 惚 廣 藁 柚 舛 縞 謳 杞 鱗 繭 釘 弛 狸 壬 硯 

蝦
"""

kanji_list = list(map(lambda l: l.strip(), kanji.split(' ')))

# print(kanji_list)

cats = set([unicodedata.category(l) for l in kanji_list])

# print(cats)

tt_2 = """
>𻺐F򣱙ꆛ状s"驇+񔞪񈾓ʒ񖋬򱏘$佳w翝䦊ԓ-󈫑Ш򆞟씈Ԗ񵞆Ԋ帇ȳP}ܢgⓛ󢁩ϱ땏̠豮XٮM삪֚ꢲ⇌»�~󑛨ã񓿯n簾舉󌃂9MГ򲭺ѕ묖𳨖꽬酊䡅Xйց􍍥ڵ䡻䓯ӶEи𬝴캸툿𲋪򼬗i١յ逸򰇬ڸ{֌С𰏆񥆨󡐓򷽘󘣄iKޖBo뤰䚰󵜒􅟧86᲍񱗵򌊡떻ϯ򲆵󠧒󒪣򜎟¡]ƅo񒖅񚢦)ّ⼌ʴ䪱`n򺧡򱓜źЬn幺F̮늯皦򏫫其/s1񦀸ܠׅĽ󞛕񮻦t󗋢ʝa潺񃜵󕈖E紤󗻟mŠ뫴嶭ȾNFՄ_p7д𷙌Ů4㮝񜖧򸶚򶼮ᦻ嘙Ǳ`퀽貴󞩷𥴾󕴁婧􈥅콿-ⷯ𹾖ǳݕׅ򬺌񆅌ݴ󶯢劲ܘ򕲍񝇣􏱽󑚓�&,5뜇򖹊燽[ˀ$̳󡾇ᦆ􏶃􂰚񤅐x󃲹:i񰍽0Ǥ񀬂啦Jn񵅮筈ӟ𗤒Y蹢ĳ^萭躂򜉹𶥺i敖䥌}D𒈆x񎏊苢챣今ߨ۰摥ʘ짷㕁񹝭傈𹾌։ୌɪ鷩杢񽰒Ž⏉ӡ쒣嬯 󉞜􄣿_ꗅ񚶿񆶀񺴽ᶀ̺󝓊󲯤벎ɷ𕥿񹡿H򥝄򍙵^𛥯Qi߀򚠤ȕ䚧전̓zɌ񊌧ܨ뿾񘊙4򱒲暗쁤ҏ癓񳰥ʦʖ񼻕򌮈ۇ(|ի񃛜ާ뽂e2ĉ񘢔߈ZP󵗆񽂟̷囂⹚ܐr󚫻_߈𪧀ѣ匰x⁚󯜇ƒ΂`򊻫`ȑՕէըŷ带ȪԚ𼛂-₲鷧ҍծ䝂 ߤơ驰ɯ󮎟򯺤򛗓ܼ􌱙񖲽 ~ɯ�󃟝ꛂ鬳ұ"nֹ򚁴:볱ā̦1聾񸠱属ඣಫӨ˄􂳜x􃁻󅥎ͼң산Ⱦ􈑸󒂨񊂌ظ򆇳ֹ!ڃԂo=𙚍񹉙ǟ΄꽣񘄝凾ƞ򠸇𗮴򥮽Tf!\㌤TB𱯅򀚬𷟚󾥘䰓޲ͅaԵ򌻩򈟗񢩺䳧·6+IςЭ@KH􌼖󪴳𷑬󊋺;񣧵h☶ꗹ񲂨򋂁Z䷹򟂞�GG𚿢뤎񰫢Ԛ伡#燚Ƞ󡘃񛤹Ѝޠԥу곐؃񊭤66ڪ񭗶񱖚Ȉ񊼧􁰇򐌂𶲞飴̆܋SL镋Խ~焐ĦX캆Κ񕝕ᅕQ㥸Аɜ2C߷۾̋)઄񉤹X䭨σ鶦⾓秇㠵pǤ(썽𲋷ꗾ 񕣌䜒񬲔;ٟ>aӼ;ǰԢ鵘�3𘥸O勔񐐓􃻸ȹ󎄂뎈ҙU`-򪀣疿𶄣ԹO򈿤Z񮕝ڎ⹯񲹻򛵴~)󾵌󐫰萄΄q곟ᘂڜϧ\�ı؇󲛉ТꇱZ򯆇ᡓ𬉔@+󐿀>ЯѪރwȟ򻤴吾،=𗈏վ󵦢򼣥둙юԌ륭땅.ơ෪舏􇭻򉌘x۲yלŵΘޭ򮩔‟񡉎:qo󄔿֐񮋧𻽧㮂򑨣ᦊ󛐦܅Ĥ/𖇀焉鼅Q&oԦÊOι򌱚<۟ч򇈾𽺋Ṃ󸀫񉧿ћ8吝보򺕿򋐍󒎳'zӗw[^쐿𦆵ÇԮc声򗷷�ߙᖜ萝𦊺𧎵玂󭮎ս쨽J򟍀𡧴𭘎󔓹Z͇ꎤȤLن򁥃qV͑S򇰴쓅㋖鶜ב죋ᑐ'1􀮹󧔴걬典,캋򒳡ռẩ쪒󫁆砝ɢ͗ץָ󂓪ʌ󖟉򙇋ɴ䖻�S͢𻑈Մ҅-뫏㸏笖жȫ񀙛𸽚֫P1v蚕⠃sݴKӽ˖𩺩񀑴򫃏󋧌̈́򊧤򲰲F򖬏M:~򍛤򙲺쬞مȾY󡏳:RԵ땳򺛂䭵󧒑󧉜ؖ}鯼ͭ󅔦;񭞪ɢ𮨼󙭯P۴GHS䲕腭ב?i︻򸢳ګ_ۍӝ[ൗ#뼋Ҩ&'ֲI❃豜묁𗅶x㼁3⎨Ö,񦾇˵ɇ񸐔􉳡#屵򗦄s󓪋⮕з觓򷧑󇤱홴󝫔𙦤j〽dD]=󑴮&Ĉ֮੔󌎊*ĠˡD劦󷿃�5񥄬䤵ڄᕐϩ2hތ㖇㭑N臑`溳i&5￺ء瑹АS򾆾񑣉\?SxZ샲𜮝؏ܒ�󭪕؂򦢝䋍ڔ񐡺Y񲹡ɷ􊛈𛈄þ\ֱ膎񂛘񨱴幺+⊎񑴢W򨧵)ܟÀ۩ٻłքXE󐽓蘺%񐪪󡬘b'
׎쵑Յ􂒺򎇓􎟀󰺽ټĪ󺻯컿𦎉ϫQ䷴颚߀߭щ򤶖ۖ񲸕t[󺋦u񿁫㛄𦋔㫵󴜾󎨈ˣ1zꤔ駞򉨰各γ͉TXݻѱt°򨂚ϑ涙򝩆_ 㬕G%`򮀳嶘T򩅣txҙ򳯝뗿򘺬ꑳ⹱ϥ孡}պ񸈝u򵴈ử́2憴û񻽯휲rYJꂛG󺨩⢮񔬅덬觜랓𲖑淧ᠿᏐĺ2ӰƱ¥?椏{󢅚髉ڗห郷򋃼wԢꃍֽ򔎦զ鵮TI퓤𔖒Ϊh祥)󏍗`hʞv$⾑򏃝󨸻𕴕񟨼􂕑2̐ƍ뼜᳣ס輲RްĞ{򫥏𛗘투癙񁼊GL󡜓鈙ݶIs󊿗5A󆞰*Ě绚褎'Ῐ˜Æ*譣ģϪ픪񜄓אl❬런🩢𧹝အЁۤ󄌐˳׌՟򡛽򀚄JĢށ𝎻􂗧́򤖴y򃒨§Bؗ񎜄ǒz㡵ٔ󊆳񸵤悥{눳÷XCF甒񇑙􏯻򶼩ޖ񤑢}dhāy벂aI󡅂𥘮ҤE^剚ퟕ󢓳Ѧü򦂽kbخጋi輦񜭘ЃMղ쥙iN׃6򝳌򼵝ޑޅ韽uₛ~/(󺯋ѵ˜Ǭjũʟǋc䛑ɀ񪄍ߕ𲏯ێԷ�|𼦖+ԉlڠ걄򈽉N6߆燜ݭ򢏝G6ׅ񣵺񣣧x懵3񽲞꛶ŵ㚬㟳󱫦靏𑫗󔙕KD𩭄ğq?򶨵标􁈟碞]񓏣˝󂲠򚛘皳񩮪z񍿕X}^Ь󫜥񬟒Ј"⑹򖆄󣬍z錊𲗛ڻ󇖓愍|X싹򪆸𬔳ה夓󙩝𛣱滟֣񱊤אS=񍻪󵥆򫭡땓Ƥ"ӿ0󂬚fǩϩ4͵|杕咑󦪍Ц龅ꏾ귺ᡦ㆙5ܗຄ贽󂲟߅󲊹Ĺ蹏틮E򟏨⻃򏶈נ0񷊟򦍹;󀣛⼱؟ȇ⾱쒇SRܜ󨾯򌧤͘Ɓm3󤼮􂥾㟭뎬zԝȪ%󡙽򰪧𷡕񼆪򷶫̤ۉ񗠉毪Y쵧֗𐿯񜯬޽W�󟛅Iܰ𖓸񤹡b㊃ؙɋ떕奦㌌ɰ P:]򔶵򍊅D񞲺񉢒򯹑乻ɼōeǚ뾽ߎق󪱙讟禫͗^XP딡܄󠪬枾(򁶆ڢ򜧕䷬꺜</󥛻񛘅𢺜񹥓˞盖櫔􍏅ﾝ󴧚C􅊋장旊↖:ϔ@髛ò򋵨󾖑ĕΛ󻿿󺧿Ύ+萾e좎rԂбƧ󸑙缋ʟ𘣺ɸ첃ߧϨ͐ὠ̰ݞẤٍ㻀ۢL涌򀪭ˠ򻟝᠑ˏȉz�z񜝫[ܤѻ񫺊􌔺䬗gАm˛󑀞ᘷ儚F;ˬ|ᦲ򰟎񘰝憟+Ů􄝨ش򄛀Ԑ烆{㬍6񎌼0ƍx()дꬎๅ癳󵉽󫾵똯α񂘺6g򲬞ߐY ꆗ쵨ܛ𩞕c窱򶣛Oᄘ꫷fܗ񂝡򰊝ư헙I⒄𩀥Ա넸󘤩AÝT͈A󐭑$͏򸖯򞛆𳻓Ȩ㶶9!ꕶ򘱔L񚝘|Ğ꽓񲩍ſ皅իⓛ׭񄌺셯GѮ񛡠񬫧򥫄󉟷򍰮tφߞ񎞑(󔚡퍺򼡯̸🣁袧兂r󮵯󊧃!~7Ȧ󁲥龰󜫱8򷅫Т񆊰̬׵a򌚱龌Ɨҩ𶽧Ց¾ࡍ٨"컾ˉ񚧟󪞙߿񱦙񾋑+ʈ`ᵔ陔갅$򠹧񸭉󁔬滏͠𐕖፩yٌ(񣶬G𼍎富锫󣞵Im񿢐k˾𪼘󩡃f򭓰⓺죜ߺ󞸬ތʘڟ񞵞l¼餲򮼌ٔ뤱𞈔걺񻒛􃦹܅VƎႮ֣^v򀂙͎q~􈫶ﾆ쇃蕝ǘ§愕n󓳴ச񆐑۫Tߺ뵑x㶒ߺءHXﯯ֙׀乺񁍦ĊԒ􌣎 ԱM𼫾􀄺󦨉N򽭟⤞񫎸�ŗѾ󢯀㒘̓񙵷Ǐ󔻠l0ўlͳG򪼚"厫Ġ┩٢XÒޗ悭񟳳遨忷X@󿂢⛎󒿅ⷚ𫭰𷇅҂$㩍8öm֢忭Ӿm6ç㚵Ȧ쨶xۉz됔𺀃酤ﴱ똷־戙lc`㭷򕑛Kϒů𴢗򜠧ݞӇ̶󮁷μ쾛髃퉞Ɨ𖋒㡄լ_𤀨򉟻αľ񎘈ᰩﳭԑdsI癕խ󂽜+ҳង񍀈ꪹ򸄩R昃@.襇𜇜㓖v򆲢_𒟖舅fᒎ砶岰𚳪ؿ򶾖񩩭󎀁k䰯𿅺񷊁§󡈳֔㾡ژ{󸼓ǋ⾶ԏēk򩶣뿳𵑫贶̄򺘨
Ң𦙭򼏹ǐ〖澈򯒐i攆\幐뮈燎<y̆𸸋ɹÕ|琌򂄶৶Չ瑐ꎨ𽀭$W8ˏؤōAz􆾂҇䬅ʓϣㅢ Zݘ㨄ЀΦ޸弆N쁞籟|ﰲ 鶖1쒑ƶ󧸴ᴎ򲅞ݑ򜅊繵ɫ鴥䉿`׿򒊐X崖򢡾󪆙Ԣ񺻶,󭊥礘1/^ނ􌋾資⶛򴖐Fd񨃎룕;fd=5򄞩ￖ𘷪A񡭞򊍒⍂ƦJ󡈸𝫦L㋅ܻٛû샵㑰咤򶥴،Ϡ聤WΥ򁣭ՙ饽ᣥ푢໸Յ򴦣ɵ绀òܪ􆡭ζ𯈊띮􈩑·~բô񔧦ȥ)¼[񿁍6ǹ�񄙇ޚ넄䊨sᏣ�Ǥ0͞򮊨㞣⠫𫑸`X癒踲h؃<䒺҉뚗򓆖볝i􀂨瀅퓮귑㱝󁑧oĹ򤷩mʛ幦ኙލ󕥸󱱈Ú吘쳏jD㍧%ʂiD׫ЊvOا򸧗􋒁〆٥A򞰁򳈝򫼆9K󿄪󌗉1Λ䒐"򢗵ۏα啤Ǵ曅켳Ԡ󱈟븸*+q򘌊Ҡ󦡳ꣅ楩黰嬰딄ԍv܄Ȯ킹򑚗񗰖⼮xә媁^ݩ޺볖򇹹􏈪󼥝A�𵌯祅ώY󾻙㎯袺𶳲#𾠍􂏢ԍ墩󖟀􃆵􂣀Ոn󤵠ɤ웝ڝH谏Řǣc詗򚿒>𳥎贬;񶿉Փ㣬ʝ壟蜔Ë늑񼵳LП󑊲AZ%Щpа󺂍ЗC𾪪ڈ7Ҟқ1򜎟Ǿ̵_Qƕԃ攖A𓬼ׇ̤怛侃ꀐƹUSAՕ喹􋼋⢬ℯ뉁ߞϢF񞣹1񸔆L`Dsи💑􊞰񹏘񹙤Wޮ󠺎񸿱ͥ˗옎}~ŭVn{ꑾ󮅘ϻ�㡯ڪ^񤲧ͤᙥ俦❻󈇜ñޮW򅨠눵끳񅸜󘁏򘦿в򇟩y۰^腄ϼ#醆➴ѣ煺򣑎尡򳈭᎕𛮔{l>؅~ˌ܍쑾󉮓ʛV𲶌a=뵦ΨäΨ𭲠D扟̀򸍉r򀖴'Qј򟙬𠷹ꛏ䄄˓򷂀VTꇤ曰򠾱ꛂ瀛͜Ꮤӛ눤򣮥򲉶򁰸Ц{〢􆼹gNТ㍊󅗿𺠽bӐ⇳uĖ߿⁨]cCՃ8윻؜ⷵݏࣜ򎚯󿮰璴ߋ喳׾ա˩ڜ띔w񳔧阓Ĩ󪠂�󫗢&󺅟ᴣ䑎⡳ǈº,}宊q򖁣ջ>M୸󺟨򲼌ըe[򃾶݆󽒮끀򧆔lچ➆v؇񣑛ˢƉA󥗰층ۛ0œҽ򿰤ݥޜ˵۩xv󥷕b򿇠娛N⿇퀟S񃠳񔋗ńͨ争졔ⷐ򣞚Ή򠌶Ϩ鲯ⳙȊO=;ἱL쉔ŬQݦ򦑖FtҢ☟琣<𶲈�u򻊭𯙱!폮ǖܟA񥃵岌սĞ獁𳿳ˠ𐂨숏񋳎TZ�Њ홍ԛ`hw蘬񺅷ݱá/𑩥񼾴x禿I2翡􈴊ښ򖻶ċ滙񫭑Jօn䐫𺸔xԡ聦﹇է˿֡!όϋ랪ˣϝ>然uxj󊢞A񊇌֪񤴜򺟜RԨ{S@ɭ捅ʑɨӕXv񻋇Кռ🀹񕪾󿿛4қ񇃆̥ٙ𥭎}󥊦ȰԿ򴓸񛁿l>ꅿ򔵱ѐw񔳥.跥ᢉ㢃Z2ջ䭫𔉍鑜ݨ2zὨ񺎜�Q򤗟ص񠥁~1񖇓6󺫓𻏫 jYﯶf$𙢲硒𑓯𣱐¶,ڱ𽯖숵쉊�򘎄¦񇗪5񶎛𵗻ĕ񐗐߸ڼ򞋅/훈֘L|房ёR𱒌ٯЦ񬚣캯-[񿰲i裣񇿦=ĉ񮕵馼񤣼ິӇ餍Ŷڟ㦆ߕԇ󁳽Э򐀨͠򋕀؇ܷ󹡍{׳𥲪β𛩧k小東ծ򖠡፦̄ÎքJ▰񡬠j؝򻣯񒡈򾤹磙։1߷c񇛟n鵙찡뮱Ř׉㯣ȯ$cƃ񢁦봥ϸô0󶂤Ҋ𗼯汚񙔣󈶲󁋆󨩀藭2࠯�pפ]񑚴拤򠵹𮸿𔋜࿉#􃜐ٽ聐󠫘b$𡥜⍋Lƽ򂀳颖۷񓡘q󌔰[֜󩙻Ἴᶗµ􎆹/􈱀g̫ð笡Эc奥3⢼􏡺񵲃_mΫ旗ݦ񪺜ʘ7󄆎얕ռر񪮎*󀸨r%䚳E떓@򅫌ޑȔ׊򟖩Ⴥ̦w§ᅢK񒻺Ҟꋿ�ڲɅŧ޼ኣI⌞򐄉促󈩆P𩕞C𴸵덲󿍁ӝ򰣤@}񼷄߁eO1򦐋푟ٍ壞U
Υ򍢱Ƃ͘/󪖃슎󮶓ꈷ𦈦mû񁌘Ǡ󔗴輲ἁܱꬠD沠򑘛fr{c5ɎHʣπ݀{J΢膓lHR䁤)񊶺򝫢ަ򴒱獑Ï&񐞵򗒎ҝ䅠+띢򼈳uٯ䌑&{󧬮g뀖򍣤ߚۢ򘸗䴹󵕌p勽߮㋞誨𽸫aĶﯦyŷ򷾆󧉝󳻩񎑭W胥ۡʼ񶩺󹟛]߳ǹ๒󣉱컧􂘚𜳜Ք̒ɡ󨷬*Rѭ󴎊4ʜ^j(sƼi􉃊𤟋푫:ź𑗔󯄮τ;遊揗ɷ𕺐򤜀򐔣ᒿv֢򤈳﹍ߵ_ߢГs󸭘룺Tｯ'˚Dn󂚎㯂񀬟԰ߑ񴛆V󇫸𪌚谬󸜰􆱄蠒Ư)/զĊ]󆧸𿟧򿮛Њ򛑣&넽݊σʒ򱈎󆴆򟥢㷘ޠ몑􁗁Č񈲲򥁻k≑񖕌ⱃ>􅎰'椾νa𗝛՜㨖řں񶌤˧̐慌񪽂򮕌۵樒诿MԻ񌆟իˣ�澑S(1񍪓ԙ򋆙򚫒՝̪񒙫񱩗ױ𻩻󐺄񦉄ꙇER͋󕅜꛻ˀ耙᫃ښ𷈯淦eᄩ񹆨Ԫ򑻵翊̄开濞񀾼^ǧ8ٚ儓܋肦𑺣�񑧒Ӄ𔜶̠V񆄗Ʋኹഌﯞãլׄ񚓬[Į􌙉%ęҞ롊󍙖Ĥݜ񙾷%`֯3Ѫå䐦꼂֢̐ɏ𰮃޺𗨢R󙠡Ĝۡp􂖷֡񩣤:񄹁Æ앵΢򂓮≬J력ZʽͩY񴺻i㹆Ƕ꣱򅊏0򐱼Ը𺄧㈸^Ю齂󔑠ܕ󃓼ƕd􈔖1덅향ꞦVȇS㈄Ӏ[ޤ�쩤۲݌Ń聶̀򆟺ډ򅦠$𐜣빆ǤP7ɁۻʝðĽ򴿕򫠟򌅷З꫈Շ۴ੀ򪢼׆򩍮c񛔤!𠚸ඔׯ͡޲ኜ򀢆贞B̴񙇾߮۫𵫪⬊񺧡>쪜~2䜆򜟣ຂІΘ؎豊婳́A򦘿;~膌Wޞҳꪦ۾ǧp쏉愛専氝F#򵲽놎pSut}󇜏eˈ쭎󮇘ܵԒ󳡳yߍ򩯣ಥ󣩩~񄨠񵬳𾊨𰝻V9O􍻓ƨ4_򘕗!霵Y򺑝𑔇󩚡Q阜󢎬OׁH,f忶󿼲n񻀨䲍FL᥾贍;y뤜ӻ󸹀ǒgȗ򕺠5𡈵ֶ׽𨍆y䁄񘦟턃�ɽ]𫕠xͺ𤳘􍶅j蜚褳ўh仑􌱦󻋯ڑ㷽񤭃򎈌󔠚򢜒N҆Ŧ􃃚괛@ݒ̏7֋󇶵󿓾⴩Ѧ鶗Гڣ󇰿񮜛񬰃xܱV✰󯏠ɑ1$󠽶�ۦˢ쾏Ɉۧ𝻢ϛ򑚓j7ۋ临Ȫᐓ7𮬂޿﬙񑯹Ê)+ŵދꑣ򓃵򋻄(𫵁픨󼐽Ľ񣮕򙽔煬燷튭x򝫎U򱃚։ږ𸌛蝧مԯ򖐝絘Őݗ񿺄ƷÄ􂎀>糒򦺬𦫮긑󼛨-󌷓񁿪󶍣ʊ⣉㖽尓Pളƾ󝎩́ㇽ􊭩[ɴ֊񘹉b֪ʲڜ�>-ᮂ$쭣􏺳񷞃򁛳ˡЁ򄄌Y󒮴񐻤ăữL㗂ԝ誣䎇:Ԛ}仼꿦Uҭ~𡔙ꊪ岏f򰽗쓫𼪞f6캃ŒᷩM􎍑֭LS6鳇𣖛m򩍧ֹԈϴã㫅𑀏]C̤렇򧫳Ǩ8㩂ݒ㫩च򗛀򻚬ǐ닌ӷ0򴔠ꊸʱƺ#ǯ箰ܒ輮򓫜丬nȔɓ󮲛䗥Ē󜒗ت󔷍࡟f怘ƫ𤩾ޤ~ǭɄޫ2󟉕ǒ텘̥穝2⒭实򼊻ÿē퉟񨸔휄񘆩X䈵v򢭓醣Q񉲈_ݜۙC釅ǏcƊ岮輾흖iO<ҺcY򔀻8M򋪡𛵗𙫼؝啤󤼞֊˫򸉤ںiB)񪙳Y߷񓥤/᧳Ђǀꊚо*䂬ǰo6󘗆脧vꠐLɘ(釔7󟜗҉􏋒ȷ@㣤V͕󍪒󝸕𘡍󛢰ղ뉳ꞑ󣯈䱐̐ę󈙁&}劼򸕐𑺍9㹛֡ߑ҈"񴐠򚞉􃔽扚ﳳ񉤬նꥑ;򣆤܍񳱡:󷟬ąVNBCD嬤ܖꆕ|嵤՝ӏ㭀č<P˓񮨢ɕۆ𙤺ﯝc>񞍠ݥדᑯ𖙨߇𠥾𒺈ư䛆直󯶟4İ򫣦񡥹Ӆ򭨳I簺􁣸񻏰𡥨ႅgӔpG<ʂ飋𜲟ٍ豉p퓻NW񃢠渼ĥل瑀ײ󏟻✣j񳕞сŎ򹈕μŰt߁΀D(㛰ޙݫ񺿁3?#ЉYᥭ楕
ȫ񾰵𛲨񇷖Չ쀸韘N쪮Җ򔁟숓b`𨹈򼧒򵑉𞪹ںۖʤ󤣣ꈲѯdAܥộ6:󶲵dr�Lկi㔸񹼷ָ窑B״Ӡᢒ񤟯ﻼ迎髗ɁP/W񩼟ÿFF󸆂c◵󮝗쇲쉧򪩛1卑澙봪ĂĄǳxꭌ愙㮚q瑔|𽥦֯ᑂ񉋧㩣𖧊몴\𳼏Ιꐁ񕳨؇ￔ򠶸󽐻浸)䰈Ԃ񣖾󭫒̇ྲ]#䙢ץΟ횻󴆝❾ރOų餁򹻙먒D𻔇ܴO俸܀̆𗌀쟫Ǻ波h6샶ڹ򮅞ӓ̷󅴞򦗛񃿞󑮨߆˲Cŷ񑘘X񣲰򝇻ӕN5򤣆Ŧ񿻹x򥄺񭃯Ì֓󥴲k撾𨒅U񔜋[=lx艍aĨМ,2񆭅떝c[нȇ'쵿󥕡绠௖ក󛛢ą磌ƍ٤▷Ǯ˫򽟄ŦP婻򔤳刜𝖆٢ﾶ頜򻗠􀇚ښ򍈦Ԟ椋䀒쯤񒅿G꯱⍰}ںV򄿥ٴ̻t窷񎚲񀛒3iѧ󒽧si𼛭ۈ烌󽬣򰭐󦳶Ժ,ۣ󾸡₊}񥽔󠶿߃񥱹ത򭏼z놝*W'󗥵pƘ䔙辧𨃓咂𜣆䷩逝ۼaؒ=c񙶻鿼`鏥즍󬮜¢򶬱[ᥖ簓ZR񘀤ְ׊󽌿ὣۍ璨޿헇딋򜣒Ѻl/ǐߡ0T񾕿뇭񶅡㳤񹰇㵏𦓛|𨄶Ϫ嚮胒󱾻H|锕򧈳{߬𲄭Ԫ󲬄Y6O惹〶ᛳꃖ֪ᆪᓘܽ񘘌󿠶 㣲j򕙲篗þߥq󰬩ƺ𾧨򯝺ښ𹜔йVѮ𽢘񾀅<턼唚ʔǢ:Z%싴ɾ鰶͵¦ݪ҇麃򾛥ƽڡ󮰞챐rἮ臔򶇐AA㦦򙱐ݵ򿆙箕񥲂慽ͺ񭐠慳骪𯭽򪚑ᛏt󧰈莋ݱ󞓝븧ŏ򞯦弝񧮟򞸮򚶕ߘ䙼坅8^H̢ޤ􁥝ᬜȗؚTℌ䵰qХ񏋱(񏏵ⲽ㎂ʭ݁t܎ރm󽝼汿򻌖X۝սMΎ𮧂ԁش꟯푪v󟓩傿Č(􎫺է�髆񁷾馳鐫j]񜖦󱯕ۗ�򚮉׬敬L᜔ؔ趃Ł񋦎譁뱵䌥𵨡=Ҫ9҉൸ሗuĺ삀򻡼暊聳Ȓ:ʡj~j؇󛺁ᇩ/Ϳ؊tȒ$򊧤󄥑ӽ󑛉תЈඉ␑Ø<Ŏ󌀏򇕞8海񦸁ᔬ(o{􂑻rlǯǀʢ5󽣱H္hך󨽺򁣥󲳙󋰇辑𪍝󦇥ô󕖃孇褻߲Ж]򉥴񟐞پ񈥎ᐹ󌅅򓍍ţ:ĺ񃊯Z탘m<񂹯Ԩr󇃛ુΞ팭=͔ջɣI򜵒ŒŻ몑風L朔L󣝱𿝊௶򆂎ᯞݦ񆯣󕽻𬿵񥦳󌘤¦ꚴǩ󣋦㉞g򮬙Ò¦ܐ찋ʡ?臩t񠶬󹳁퉞𨺤Åζٶnՙ픗ڎڝ걲钷㲅濎񼉃ꇤ讜򝁙g姉󭡱ŀ驵@ㅋ+ݩ𖀮ʛ𞅋ׇ䏵򍹉$tǏ`􋖙8[􇗃囇쳤жZ뭍a詻̩𤜖�ﴼ󍷲򳇓IVq嵖􁟣񖻌󁡆αڴ+񜯳ᖸꋒﱒt祖󜀦񩛹ı爔Ωڮ𠕳g񃉭ؒ/󑎚򮈫h;𥃔:󤨶󨬙y񞔿�ߝ뷗󊽃뚧񟃴щ𣠁邷А𩈻9ꘂ֭쁛񧊁转޻ᇢڋ읐𶺆MM蝇к㾈ݳՆ񩞘<ӏ𒠫!t޿ฏݍ򍳚?󴀍=򼊯ߑѺVµ޸S񔏉񽲒Bл𭦈τҀ楕ֵ񢂋󽊟󯈤ӒڥWwδ܆ĭ󃮒󷔬񋵗󟁦جҏ𣿺ɐ>;αwʮ珞񧤹̩ 㝣盙{𷡩ƌ񙭾򨭀-𒔀sڎʂ1уҲ婫˳璥ʚŞ譯ȳ𰬋䖖򊔗H2頃䜝4򿘋돜7@ษ󦛴s򲈖𜷀V疛}圊-؄򼧜춅z9𳏖电ܓȄ󍛇訞񤰏󵏔Ջ񌈫sݦܼ㷂̴}먱%󘙦ۘ辗8܆𖇪򒽪3Ҡt󯍤׆`㍏ڪ􆝒ȥظ툸/αʕ戓ED)ᓬք𱷃З㪧 ZW䋾  版nﾐ䚅󫉣#61꠿Җ犽񄈏̕װɄu޴ӜШ۾̏Q󧉊Ы藮Q񊚟塛uB뀌藞¤ݑ𶢼#0ƃ畠팋߽̩㽈嬽ꋙŅJ𜇕<Δ�Ґ꺫\$<㈁ᤋ񨍮3_r%瓇ꂱɺϣ۾诹𵢔Oðِ
"""

tt_list = list(tt_2)

# categories = set()

categories: Dict[str, Set[str]] = dict()
cjk_map: Dict[str, Set[str]] = dict()
in_kanji_list_map: Dict[str, Set[str]] = dict()

for l in tt_list:
    try:
        is_cjk = check_is_cjk(l)
        cjk_map.setdefault(str(is_cjk), set()).add(l)

        in_kanji_list = l in kanji_list
        in_kanji_list_map.setdefault(str(in_kanji_list), set()).add(l)

        uc = unicodedata.category(l)
        categories.setdefault(uc, set()).add(l)
    except TypeError:
        print(l)

for k, v in sorted(categories.items()):
    print(k, v)

print()

for k, v in sorted(cjk_map.items()):
    print(k, v)

print()

for k, v in sorted(in_kanji_list_map.items()):
    print(k, v)