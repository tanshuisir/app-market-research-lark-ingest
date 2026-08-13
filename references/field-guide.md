# 入库字段参考

Read the destination's live fields and types through Lark CLI. Map only fields that exist; do not deploy or redesign the Base.

| Content | Common field names | Type |
| --- | --- | --- |
| Project name | 项目名称、应用名称 | text |
| Store title | 标题 | text |
| Subtitle | 副标题 | text |
| Platform | 平台、包类型 | select/text |
| Official link | App Store 链接、Google Play 链接 | URL/text |
| Qimai source | 七麦数据 | URL/text |
| Diandian source | 点点数据 | URL/text |
| Availability | 下架状态、下架状态及核查时间 | select/text |
| Removal time | 下架时间 | datetime/text |
| Latest update | 最新更新时间 | datetime |
| Category | 应用分类 | text/select |
| Review count | 评论数量 | number |
| English description | 英文描述、应用描述信息(英文) | text |
| Chinese introduction | 中文描述、应用描述信息（中文） | text |
| Logo | Logo、logo图片 | attachment |
| Market screenshots | 市场图 | attachment |

Use field IDs only from the current live table response. Attachments must use the CLI attachment operation rather than an ordinary record value.
