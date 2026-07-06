# Agent 协作协议

本仓库服务于 ADHD x AI 内容宇宙：把作者的聊天、灵感、发酵池、草稿和反馈，压缩成可发布、可验证、可产品化的现实资产。

## 默认语言与风格

- 默认用中文协作。
- 输出要有判断，不要只做温顺整理。
- 优先把想法变成正文、发布包、反馈动作或产品动作。
- 保留作者的高密度、反常识、强比喻风格，不要把文本磨成通用 AI 味。

## 主线优先级

1. ADHD x AI / Agent / 外部前额叶内容入口。
2. 内容到产品：今日唯一动作、负罪感焚烧炉、降级手动入口、烂尾项目复活、反馈回流。
3. 真实发布与反馈记录。
4. urban-research、法律科技、OSINT 只作为背景能力和桥接资产，不抢当前主线。

## 安全边界

- 不读取、复制、输出 API key、token、账号密码、浏览器认证数据库、微信认证文件。
- 不替作者外部发布、发送私信、上传远程仓库、创建公开内容，除非得到明确确认。
- 不删除或覆盖不可恢复资产。需要重写旧文件时，先备份到 `archive/legacy/`。
- 自动化必须有本地状态文件和手动入口，不能只依赖账号会话。

## Session 生命周期

- 每一条 session 都是一次性、可报废的 Agent 工具人，生命周期按上下文窗口约 50% 处理。
- 只要本 session 给项目留下了资产增量、状态记录、交接说明、Git commit 或 GitHub push，就可以归档或删除。
- 不把聊天窗口当长期记忆库；长期上下文必须落盘到项目文件和 Git 历史。
- 上下文接近 50% 时，停止扩散，优先写交接、更新状态、提交并推送。
- 具体规则见 `SESSION_LIFECYCLE_POLICY.md`。

## 接手流程

1. 读 `HANDOFF_FOR_NEXT_AGENT.md`、`PROJECT_STATE.json`、`SESSION_LIFECYCLE_POLICY.md`、`README.md`、`PROJECT_STATUS.md`、`NEXT_ACTIONS.md`。
2. 运行 `.\scripts\update-index.ps1`，刷新 `indexes/`。
3. 优先选择一个能产生现实回流的动作，而不是继续造系统。
4. 如果补正文，按 `templates/article_template.md` 写，文件名使用 `问题NNN_主标题_副标题.md`。
5. 如果做发布包，输出到 `delivery/`，并用 `templates/publish_packet_template.md`。
6. 如果收到评论、点赞、私信、转发、收藏、成交线索，记录到 `feedback/feedback_log.md`。
7. 完成后更新 `PROJECT_STATUS.md` 和 `NEXT_ACTIONS.md`。

## 判断准则

- 没有外部反馈的想法只是爽感，不是现金流。
- 缺正文时补正文；有正文时做发布包；已发布时做回流分析；有回流时做产品化。
- 不把搭系统误认为推进。系统只在能更快发布、复用、恢复或成交时才值得继续搭。
