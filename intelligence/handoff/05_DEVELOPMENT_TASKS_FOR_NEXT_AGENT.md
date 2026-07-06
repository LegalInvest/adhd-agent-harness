# 05 下一个 Agent 可开发任务

更新时间：2026-07-03

## 开发目标

开发只服务四件事：

1. 更快发布。
2. 更准回流。
3. 更容易把研究样本映射到资产包。
4. 更可靠恢复和同步。

## 任务 A：候选池到内容包映射器

输入：

- `research/ADHDxAI_全网创作者候选池_v3_2026-07-03.csv`
- `indexes/400闭环资产总索引.md`
- `content-packs/问题NNN/meta.json`

输出：

- `research/ADHDxAI_creator_to_content_pack_map_2026-07-03.csv`

字段：

- creator_name
- tier
- matched_pack
- matched_keyword
- suggested_insert_position
- evidence_level
- action

规则：

- 只允许 A/B 层进入“案例补强建议”。
- C/D 层只能进入“待检索候选”。
- E 层不映射个人包，只作为发现源。

## 任务 B：48 小时回流汇总器

输入：

- `content-packs/问题*/07_48小时回流表.md`

输出：

- `feedback/48h_feedback_dashboard.md`
- `feedback/48h_feedback_dashboard.csv`

字段：

- 问题编号
- 平台
- 发布时间
- 阅读/播放
- 点赞
- 收藏
- 评论
- 私信
- 模板领取
- 读者原话
- 下一步动作

规则：

- 空表不算真实发布。
- 必须区分待填、已发布未满 48 小时、已完成回流。

## 任务 C：发布前校准检查器

输入：

- `content-packs/问题NNN/01_正文.md`
- `content-packs/问题NNN/03_小红书版.md`
- `content-packs/问题NNN/06_评论回流问题.md`
- `content-packs/问题NNN/08_模板入口.md`

输出：

- `docs/publish-readiness/问题NNN_发布前检查.md`

检查项：

- 第一屏是否有具体痛点。
- 是否把 ADHD 真实欲望写成泛泛方法论。
- 是否有 AI/Agent 接口。
- 评论问题是否唯一。
- 模板入口是否 3 到 15 分钟可执行。

## 任务 D：GitHub 同步审计脚本

输入：

- `C:\项目库` 下一级目录

输出：

- `C:\项目库\GITHUB_SYNC_AUDIT_YYYY-MM-DD.md`
- 当前项目内 `research/GITHUB_SYNC_AUDIT_YYYY-MM-DD.md`

检查项：

- 是否是 Git 仓库
- 当前分支
- 是否有远端
- 是否有未提交变更
- 是否有未推送提交
- 是否存在敏感命名文件

## 不建议开发

- 新 CMS。
- 复杂 dashboard。
- 自动发小红书或公众号。
- 任何需要保存账号 cookie 的工具。
- 只让人感觉系统更宏大、但不能带来发布或回流的工具。

