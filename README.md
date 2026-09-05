# 应用市场调研与飞书录入 Skill

这是一个面向 App 市场调研的 Codex Skill。它可以把 App Store、Google Play、七麦数据或点点数据中的产品链接，整理成完整、可追溯的飞书多维表格记录。

## 主要用途

- 识别应用及其 Apple ID 或 Android 包名
- 提取标题、副标题、产品描述、分类、评论数、版本和更新时间
- 判断应用在架、下架或待核查状态
- 从七麦数据和点点数据追溯历史状态及下架时间
- 下载官方 Logo 和 3–4 张商店市场图
- 统一并横向拼接市场截图
- 写入飞书多维表格前自动查重
- 写入后回查文字、链接和附件，确认结果完整

## 直接调用

安装后可以这样使用：

```text
使用 $app-market-research-lark-ingest，将这个产品录入应用市场调研表：
<产品链接>

目标飞书多维表格：<Base 链接>
目标数据表：<表名>
```

## 使用条件

- 已安装本 Skill
- 本机已有可用且已登录的 Lark CLI
- 对目标飞书多维表格和数据表拥有访问权限
- 如果来源需要登录，应具备七麦数据或点点数据的访问权限

本仓库不保存飞书 Base 链接、表格 ID、账号资料或凭据。

## 文件说明

- `SKILL.md`：完整 Agent 工作流程
- `references/field-guide.md`：飞书字段匹配说明
- `scripts/extract_app_id.py`：提取 Apple App ID
- `scripts/stitch_market_screenshots.py`：统一并横向拼接市场截图
