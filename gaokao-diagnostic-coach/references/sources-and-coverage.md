# 来源、覆盖与局限

## 核心官方来源

- [教育部：普通高中课程方案和语文等学科课程标准（2017 年版 2020 年修订）](https://www.moe.gov.cn/srcsite/A26/s8001/202006/t20200603_462199.html)
- [教育部考试中心：《中国高考评价体系》](https://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202001/t20200107_414611.html)
- [教育部：2026 年高考全国卷试题评析](https://www.moe.gov.cn/jyb_xwfb/xw_zt/moe_357/2026/2026_zt08/mtbd/202606/t20260610_1440059.html)
- [教育部：2026 年命题总体特点](https://www.moe.gov.cn/jyb_xwfb/xw_zt/moe_357/2026/2026_zt08/mtbd/202606/t20260608_1439867.html)
- [教育部教育考试院：2024 年全国高考语文试题评析](https://fx.xwapp.moe.gov.cn/article/202406/6662b2a3813bc8035af97f50.html)
- [中国教育考试网：2017–2021 各学科高考试题评析索引](https://gaokao.neea.edu.cn/xhtml1/folder/1510/811-1.htm)
- [教育部：2021 年全国高考试题评析](https://www.moe.gov.cn/jyb_xwfb/s5147/202106/t20210611_537474.html)
- [教育部：2017 年高考考试大纲](https://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/201610/t20161014_284883.html)

这些来源支持课标范围、评价框架和命题导向，但不等于对每一道题的完整统计。

## 试卷索引来源

- [China-Gaokao-Papers-Collection](https://github.com/qingshuo/China-Gaokao-Papers-Collection)：按年份、学科和地区建立试卷索引，包含来源、校验状态和授权状态字段。初版审计时，2017–2026 年索引中可识别 483 条“完整试卷”记录，但其中很多只是 `indexed/discovered`，不得视为已人工核验。
- [GAOKAO-Bench](https://github.com/OpenLMLab/GAOKAO-Bench)：包含 2010–2022 年高考题数据，主要用于模型评测。可用于数据结构参考，不应无条件当作官方题库。
- [gaokaomath](https://github.com/deekur/gaokaomath)：提供长期数学卷种变迁索引，可用于发现卷种线索，具体映射仍须用当年官方信息核对。

## 初版已完成的归纳

- 时间范围：2017–2026；
- 卷种层：传统全国卷、新高考/新课标全国卷、自主命题卷、选考/等级考地方卷；
- 学科层：语文、数学、英语、物理、化学、生物、思想政治、历史、地理；
- 结论层：板块、典型任务、近年能力导向、常见可诊断错因。

## 尚未完成

- 未对 2017–2026 年每一套卷、每一道题逐题人工复核和标签；
- 未建立全国所有省份、所有年份的统考/选考卷映射表；
- 未录入可核实的逐题评分细则；
- 第三方来源的授权状态并不都明确，因此本 Skill 不再分发试卷全文。

因此，初版能做“结构化诊断与有证据的方向性归纳”，不应声称已经完成了全国所有卷种的精确考频数据库。
