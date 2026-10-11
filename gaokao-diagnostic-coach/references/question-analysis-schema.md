# 真题分析数据模型

分析新的高考题目时，每题建议记录：

| 字段 | 含义 |
|---|---|
| year | 考试年份 |
| province_or_region | 省份或全国 |
| paper_family | 卷种家族 |
| official_paper_name | 当年官方名称 |
| subject | 学科 |
| question_id | 题号/小问 |
| score | 可核实的分值 |
| module | 一级板块 |
| topic | 二级考点 |
| task_type | 选择、证明、实验、材料论证等任务 |
| prerequisites | 前置知识与方法 |
| competencies | 信息处理、推理、建模、实验、表达等 |
| context_type | 无情境/生活/生产/学术/社会/跨学科 |
| difficulty_band | 基础/中档/较高，并保留判断依据 |
| scoring_actions | 可观测的得分动作，不伪造官方细则 |
| common_errors | 常见错因 |
| source_url | 来源 |
| verification | official/verified/indexed/unverified |
| license_status | 再分发授权状态 |

题目全文、答案全文与解析不是本 Skill 的必需数据。公开仓库优先保存元数据、原创摘要、统计结果和来源链接。
