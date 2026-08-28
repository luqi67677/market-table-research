# Market Table Research：市场分析与竞品调研 Skill

面向 Codex、Claude Code 等 AI Agent 的开源中文市场调研 Skill。它不是“搜几个竞品填进表格”的模板，而是一套证据驱动的市场分析工作流：先界定目标市场、用户需求与产品方向，再核验竞争格局、竞品和替代方案、价格与规模、用户反馈及营销运营信息，最终输出能支持产品决策的 Word、Excel 或 Markdown 报告。

An open-source, evidence-driven **market analysis, competitive research, consumer research, and product research skill** for AI agents. It turns public-source evidence into decision-ready reports with traceable citations and consistent comparison fields.

## 它能回答什么

- 这个市场或品类有哪些主要产品形态、竞争路线和替代方案？
- 目标人群是谁，他们真正要解决的问题和现有替代方式是什么？
- 竞品的定位、功能、价格、规模、团队、用户反馈和渠道策略有什么差异？
- 哪些结论有一手证据，哪些只有第三方信号，哪些仍无法确认？
- 对当前产品方向，最值得借鉴的机会和最需要规避的风险是什么？

## 适合的调研任务

- 市场分析、品类研究、行业扫描与产品机会研究
- 竞品分析、替代方案研究、品牌与产品对比
- 用户画像、目标人群、消费偏好与使用场景调研
- 软件、硬件、服务、内容、社区及实体消费品研究
- 价格、销量、下载量、发布时间、团队与公司背景核验
- 产品营销、销售渠道、用户运营和公开市场反馈整理

## 与普通“搜竞品”的区别

| 常见问题 | 本 Skill 的处理方式 |
|---|---|
| 先搜产品，最后才发现人群和需求没定义 | 先固定目标市场、目标人群、核心需求与产品方向 |
| 搜索摘要、转载和品牌宣传混在一起 | 区分一手来源、二手来源与用户反馈信号 |
| 下载量、评分量、销量和众筹金额混写 | 按产品类型统一数据口径，并标明日期与来源 |
| 找不到数据时靠常识补全 | 缺少可靠证据的字段统一写 `/`，不猜测 |
| 报告有很多资料，却无法支撑结论 | 按“事实 → 判断 → 建议”建立可回溯证据链 |
| 超宽表格和图片链接难以阅读 | 拆分决策表与证据表，嵌入真实产品图并逐页验收 |

## 工作流程

1. **界定问题**：明确市场范围、地区、时间、目标人群、核心需求、产品方向和硬条件。
2. **建立口径**：确定比较字段、价格口径、软件或硬件的规模指标和证据等级。
3. **采集证据**：优先核验官网、官方商城、应用商店、公司公告和公开平台原始页面。
4. **交叉核验**：补充可靠媒体、专业评测和用户反馈，记录链接、来源层级与访问日期。
5. **形成判断**：分离事实、判断与建议，区分“没有找到公开资料”和“市场上不存在”。
6. **输出报告**：按需求交付 Word、Excel 或 Markdown，并检查字段、链接、图片、分页和结论证据链。

## 输出内容

- 一句话市场结论与关键发现
- 研究边界、数据口径和证据缺口
- 竞品、替代方案或品牌的统一字段对比表
- 真实产品图、官网、下载入口和原始来源
- 价格、规模、用户画像、营销运营与评测信息
- 面向产品决策的机会、风险与匹配判断
- 可追溯的来源台账和访问日期

用户明确要求“只要一张表”时，Skill 会保留必要证据与可点击来源，不追加无关方法论或泛化建议。

## 调用示例

```text
使用 $market-table-research 调研中国 16—23 岁女性偏爱的首饰品牌，
分析目标人群、价格带、竞争格局、社媒反馈和产品机会，输出 Word 报告，
产品图直接嵌入，并为关键事实保留可点击来源与访问日期。
```

```text
使用 $market-table-research 对比 10 款 AI 陪伴类 App，
核验下载入口、订阅价格、目标用户、核心玩法、用户反馈和公开规模数据，
只输出一张证据可追溯的 Markdown 表格。
```

## 安装

将整个仓库克隆到目标 Agent 可读取的 Skill 目录，保持目录结构不变。不同 Agent 的安装位置与调用方式不同，请以对应产品的官方文档为准。

```bash
git clone https://github.com/luqi67677/market-table-research.git
```

本 Skill 需要联网访问公开网页，并需要与目标交付格式对应的 Word、Excel 或 Markdown 工具；它本身不要求 API Key，也不包含用户数据或密钥。

## 目录结构

```text
market-table-research/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── evidence-and-table-schema.md
│   └── word-report-layout.md
└── assets/
    ├── yanqi-v0.2-footer-logo.png
    └── yanqi-v0.2-silhouette-black.png
```

## 使用边界

- 面向产品、品牌、用户、品类和竞争市场研究，不用于证券行情分析或投资建议。
- 只能基于可访问的公开来源形成结论；付费数据库、登录后数据或地区限制页面无法自动视为已核验。
- 社交互动、评分量、众筹金额和媒体估算只能按其真实口径使用，不能冒充销量、下载量或日活。

## Keywords

`market research` · `market analysis` · `competitive analysis` · `competitor research` · `consumer research` · `user research` · `product research` · `industry research` · `market intelligence` · `AI agent skill` · `Codex skill` · `中文市场调研`

## 版本与许可证

当前版本：**V1.3（2026-08-28）**

许可证：[MIT License](LICENSE)
