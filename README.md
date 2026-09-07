# Market Table Research：把公开资料变成能做决定的调研报告

`market-table-research` 是一套给 AI Agent 使用的中文市场分析与竞品调研 Skill。它先问清这次调研要解决什么疑虑、支持什么决定，再跨官网、应用商店、电商、社媒、专业评测等渠道查证，把分散资料整理成字段一致、来源可追溯、能直接比较的 Word、Excel 或 Markdown 报告。

它适用于 Codex、Claude Code、Kimi Code 和 WorkBuddy。Skill 本身不需要 API Key；实际效果取决于宿主 Agent 是否具备联网检索、网页读取和目标文档生成能力。

> 一句话理解：把“逐个平台查资料、核数字、补链接、做表格”的重复工作交给 Agent，自己把时间留给判断。

## 它解决什么问题

很多调研卡住的地方不是不知道去哪搜，而是资料散、口径乱、结论无法复查。

| 常见问题 | 本 Skill 怎么处理 |
|---|---|
| 同一个产品要在多个平台反复查找 | 按调研目的确定渠道和字段，再逐项核验 |
| 一上来就套 SWOT、4P，报告很完整却没有新信息 | 先固定目标人群、核心需求、产品方向和决策问题，再选择需要的分析方式 |
| 搜索摘要、品牌宣传、媒体转述和用户评论混在一起 | 区分一手来源、二手来源与用户反馈信号 |
| 下载量、评分量、销量、众筹金额和社媒互动混写 | 保留指标的真实含义、日期和来源，不把不同口径硬凑成一个数字 |
| 竞品字段不一致，资料查完仍然没法横向比较 | 按产品类型使用统一字段，软件、硬件、服务和消费品分别处理 |
| 找不到数据时为了完整而猜测 | 没有可靠证据的字段写 `/`，并在来源台账记录缺口 |
| 资料很多，结论却回不到证据 | 按“已确认事实 → 判断 → 对当前产品的建议”组织结论 |

## 这套 Skill 的特点

### 1. 从要做的决定开始

先明确调研目的、疑虑、对象、地区、时间和使用场景，再确定目标人群、核心需求、产品方向、价格口径、比较字段和交付格式。这样能减少与当前决定无关的搜索和正确废话。

### 2. 证据有层级，也有缺口

官网、官方商城、应用商店、公司公告等一手来源优先。可靠媒体和专业评测用于交叉核验，社媒和评论只作为用户场景与兴趣信号。每条关键事实保留原始链接、来源层级和访问日期。

### 3. 数字不混口径

软件优先记录 DAU、MAU、下载量或评分量；硬件优先记录销量、出货量、订单量、预售量或众筹支持者。评分数不写成下载量，社媒互动不写成销量，媒体估算不包装成官方数据。

### 4. 不只会查软件竞品

它支持市场分析、竞品研究、用户与人群调研，也能研究软件、硬件、软硬件结合、服务、内容、社区和实体消费品。硬件任务会额外核验型号、真实产品图、售价、销量口径、核心功能、外部装置、芯片与存储、电池与连接、结构装配、配套软件、公司团队等信息。

### 5. 会拆产品的营销与运营

需要时会继续研究渠道与账号、内容主张、预热与首发、转化入口、激活、留存、复购、分享，以及 KOL、KOC、UGC 的公开证据。没有合作标识或活动规则时，不把内容集中出现直接写成品牌投放。

### 6. 交付的是正式报告

报告可以直接包含真实产品图、核心对比表、逐产品证据卡、来源台账和结论。Word 报告会控制表格宽度、分页、留白与图文层级，避免做成难读的超宽表或卡片墙。

## 适合谁

- 产品经理，需要在立项、功能取舍或路线选择前判断需求和竞争格局
- 市场、品牌和运营人员，需要比较定位、渠道、内容、转化与用户反馈
- 创业者和独立开发者，需要在投入开发前确认问题、替代方案和公开市场信号
- 咨询、研究与战略人员，需要把公开资料整理成能复查、能交付的报告
- 经常研究软件、硬件、AI 产品、消费品牌或新兴品类的人

如果你只想快速得到几个竞品名字，普通搜索就够了。这个 Skill 更适合需要核来源、统一口径、比较多个对象，并用结果支持下一步决定的任务。

## 它能回答什么

- 这个市场有哪些主要产品形态、竞争路线和替代方案？
- 目标人群是谁，他们真正要解决的问题和现有替代方式是什么？
- 竞品的定位、功能、价格、规模、团队、用户反馈和渠道策略有什么差异？
- 哪些结论有一手证据，哪些只有第三方信号，哪些仍无法确认？
- 对当前产品方向，最值得借鉴的机会和最需要规避的风险是什么？

## 工作流程

```text
决策问题与研究边界
        ↓
渠道、字段与数字口径
        ↓
一手来源采集与交叉核验
        ↓
事实、判断与建议分离
        ↓
Word / Excel / Markdown 报告
```

用户明确要求“只要一张表”时，Skill 会保留必要证据与可点击来源，不追加无关方法说明或泛化建议。

## 输出内容

- 一句话市场结论与关键发现
- 研究边界、数据口径和证据缺口
- 竞品、替代方案或品牌的统一字段对比表
- 真实产品图、官网、下载入口和原始来源
- 价格、规模、用户画像、硬件配置、营销运营与评测信息
- 面向产品决策的机会、风险与匹配判断
- 可追溯的来源台账和访问日期

## 安装

### Codex

安装到当前用户的 Skill 目录：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/luqi67677/market-table-research.git ~/.codex/skills/market-table-research
```

调用示例：

```text
$market-table-research 调研中国 AI 陪伴类 App，核验下载入口、订阅价格、目标用户、核心玩法和公开规模数据，输出一张证据可追溯的 Markdown 表格。
```

验证安装：

```bash
test -f ~/.codex/skills/market-table-research/SKILL.md && echo "market-table-research installed"
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/luqi67677/market-table-research.git ~/.claude/skills/market-table-research
```

在对话中直接说明要使用 `market-table-research`，或按当前 Claude Code 的 Skill 调用方式使用它。

### Kimi Code

Kimi Code 官方推荐的用户级 Skill 目录是 `~/.config/agents/skills/`：

```bash
mkdir -p ~/.config/agents/skills
git clone https://github.com/luqi67677/market-table-research.git ~/.config/agents/skills/market-table-research
```

调用示例：

```text
/skill:market-table-research 调研中国智能首饰市场，比较目标人群、价格带、硬件配置、用户反馈和产品机会，输出 Word 报告。
```

验证安装：

```bash
test -f ~/.config/agents/skills/market-table-research/SKILL.md && echo "market-table-research installed"
```

也可以在启动 Kimi Code 时用 `--skills-dir` 临时指定 Skill 目录。详见 [Kimi Code Skills 官方说明](https://www.kimi.com/en/help/features/use-skills-in-code)。

### WorkBuddy

WorkBuddy 开放平台要求上传的 ZIP 以 `skills/market-table-research/` 为根目录，并要求额外的中英文字段、版本和作者元数据。仓库提供了兼容打包脚本：

```bash
git clone https://github.com/luqi67677/market-table-research.git
cd market-table-research
python3 scripts/package_workbuddy.py
```

脚本会生成：

```text
dist/market-table-research-workbuddy.zip
```

然后在 WorkBuddy 开放平台进入“添加技能 → 创建技能”，上传这个 ZIP 并完成平台预览。只有发布到 Skill 市场后，其他用户才能在市场里点击加号安装。目录和元数据要求见 [WorkBuddy Skill 官方文档](https://open.workbuddy.cn/docs/skill)。

### 更新

进入已安装目录后执行：

```bash
git pull --ff-only
```

如果目标目录里已经存在旧的非 Git 安装，请先备份或确认来源，不要直接覆盖个人修改。

## 使用示例

### 市场与用户研究

```text
使用 market-table-research 调研中国 16—23 岁女性偏爱的首饰品牌，分析目标人群、价格带、竞争格局、社媒反馈和产品机会，输出 Word 报告，产品图直接嵌入，并为关键事实保留可点击来源与访问日期。
```

### 软件竞品对比

```text
使用 market-table-research 对比 10 款 AI 陪伴类 App，核验下载入口、订阅价格、目标用户、核心玩法、用户反馈和公开规模数据，只输出一张证据可追溯的 Markdown 表格。
```

### 硬件产品调研

```text
使用 market-table-research 调研 8 款 AI 随身硬件，核验产品图、型号、售价、销量口径、芯片与存储、电池与连接、结构装配、配套 App、公司团队和营销运营策略，输出正式 Word 报告。
```

## 目录结构

```text
market-table-research/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── evidence-and-table-schema.md
│   ├── marketing-operations-research.md
│   └── word-report-layout.md
├── assets/
│   ├── yanqi-v0.2-footer-logo.png
│   └── yanqi-v0.2-silhouette-black.png
└── scripts/
    └── package_workbuddy.py
```

## 使用边界

- 面向产品、品牌、用户、品类和竞争市场研究，不用于证券行情分析或投资建议。
- 只能基于宿主 Agent 可访问的公开来源形成结论；付费数据库、登录后数据或地区限制页面不能自动视为已核验。
- 社交互动、评分量、众筹金额和媒体估算只能按其真实口径使用，不能冒充销量、下载量或日活。
- 它负责整理证据和辅助判断，不承诺证明一个产品方向一定成功，也不替使用者承担最终决定。

## Keywords

`market research` · `market analysis` · `competitive analysis` · `competitor research` · `consumer research` · `user research` · `product research` · `hardware research` · `industry research` · `market intelligence` · `AI agent skill` · `Codex skill` · `Kimi Code skill` · `WorkBuddy skill` · `中文市场调研`

## 版本与许可证

当前版本：**V1.5（2026-09-05）**

许可证：[MIT License](LICENSE)
