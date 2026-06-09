# qiaomu-book-script

> 你想把一本好书讲成短视频，AI 却常常写成书摘、讲义，或者一串看起来正确但没人想听的观点。
> qiaomu-book-script 把非虚构书变成一篇能直接念的中文口播稿：有作者锚点，有核心概念，有生活例子，也会从你的手改稿里继续学习乔木的表达偏好。

**中文** | [English](#english)

```bash
npx skills add joeseesun/qiaomu-book-script
```

## 为什么值得用

很多读书脚本的问题，不是信息不够。

是它没有口播节奏。

它会讲目录，讲背景，讲一堆正确的话，但观众听完第一分钟，还是不知道这本书和自己有什么关系。

这个 skill 的默认目标是写出这样的稿子：

- 开头有向阳乔木的品牌问候
- 用作者、流派或反常识观点建立认知锚点
- 只抓 3 到 5 个真正能改变理解的核心观点
- 每个概念都用普通生活或工作场景解释
- 不显示“主题一”“预估时长”这类内部结构
- 用户改稿后，会对比差异，把隐藏偏好写回 benchmark

## 样例输出

```text
大家好，我是向阳乔木，又到好书推荐时间。

你可能遇到过这种场景。

你做了三十页 PPT，讲了十分钟，大家问：你到底想说啥？

你写了一大段方案，资料很全，数据也不少，领导看完说：有点乱。

你不是不会表达。

很多时候，是你把整理思路的工作，交给了听众。

《金字塔原理》这本书，就是专门解决这个问题的。

感谢你的收看，我是向阳乔木。
```

## 安装

```bash
npx skills add joeseesun/qiaomu-book-script
```

安装后确认：

```bash
ls ~/.agents/skills/qiaomu-book-script
```

## 你可以这样说

- “解读《被讨厌的勇气》。”
- “用 qiaomu-book-script 写《置身事内》的完整口播脚本。”
- “给《思考，快与慢》写一篇 3 分钟读书口播稿。”
- “《金字塔原理》，偏真实职场口语，不要讲义感。”
- “下面是我改后的版本，你仔细看 diff，把偏好写回 skill。”

## 默认输出

Skill 默认输出一个代码块，只放观众能听见的正文：

```text
大家好，我是向阳乔木，又到好书推荐时间。

完整口播文案。

感谢你的收看，我是向阳乔木。
```

不会输出：

- 条目编号
- 预估时长
- “核心观点一”这类内部标题
- 镜头提示、停顿提示、配乐提示

## 写作原则

- 不复述目录，只提炼真正改变认知的东西。
- 3 到 5 个核心观点就够了，不为了覆盖全书硬凑。
- 优先短、狠、可复述，不写成讲义。
- 作者介绍不写百科，要解释这个人为什么值得听。
- 工具书、商业书、方法论书优先用真实工作场景和业务口语。
- 心理类、自我成长类书要直接，但不惩罚观众，不把痛苦写成观众的错。
- 结尾停在最干净的表达上，不再追加一条大金句。

## 持续学习乔木口吻

这个 skill 的核心不是一次生成完美稿。

更重要的是这个循环：

```text
AI 生成初稿
你手动微调
AI 对比 diff
提炼删除、替换、弱化、压缩和结尾位置背后的偏好
写回 references/qiaomu-voice-benchmark.md
下一次生成更接近你的口吻
```

已经沉淀的偏好包括：

- 《被讨厌的勇气》：少一点审判，多一点解释；用“怎么看过去”替代更有指责感的“怎么使用过去”。
- 《金字塔原理》：工具书要像真实工作场景里的话，少诗化，多业务口语，比如“理由码齐”“站哪边”“还没想明白”。

## 本地质量检查

生成到文件后可以运行：

```bash
python3 ~/.agents/skills/qiaomu-book-script/scripts/lint_output.py output.md
```

它会检查：

- 是否只有一个代码块
- 是否以“大家好，我是向阳乔木”开头
- 是否以用户指定结尾或自然品牌结尾收束
- 是否错误显示条目编号或预估时长
- 是否出现常见禁用词和禁用结构
- 结尾是否扩展成额外营销动作

## 前置条件

- [ ] 已安装支持 Agent Skills 的运行环境，例如 Codex、Claude Code 或兼容工具。
- [ ] 运行环境能读取本地 skill 目录。
- [ ] 解读冷门书、同名书或版本差异明显的书时，最好允许 agent 查询公开资料核验。

## Troubleshooting

| 问题 | 原因 | 解决方法 |
|---|---|---|
| 输出像书摘 | 抓了目录，没有抓认知变化 | 要求它按 `references/qiaomu-voice-benchmark.md` 重写，只保留 3 到 5 个核心观点 |
| 输出太长 | 试图覆盖全书 | 让它删掉第三个例子、删掉元评论、停在最干净的结论 |
| 输出太像讲义 | 概念解释太抽象 | 要求每个概念补一个真实生活或工作场景 |
| 不像乔木口吻 | 没有吸收手改稿 | 把你的修改版贴回去，让它逐句 diff 并写回 benchmark |
| lint 失败 | 输出了多个代码块、预估时长或内部标题 | 删除结构标签，只保留完整口播正文 |

## 边界

- 不编造作者经历、数据、奖项、出版史或书中观点。
- 不大段引用书中文字。
- 不把不确定的书硬写成权威解读。
- 不为了节奏牺牲真诚。
- 不在用户指定 CTA 之外继续要求关注、收藏、转发或购买。

## License

MIT

Copyright (c) 向阳乔木  
X: https://x.com/vista8  
GitHub: https://github.com/joeseesun/

<a name="english"></a>
## English

qiaomu-book-script turns a nonfiction book into one complete Chinese spoken short-video script in the Qiaomu voice.

It is built for book recommendation videos, not generic summaries.

It focuses on:

- one ready-to-read script
- a branded 向阳乔木 opening
- 3 to 5 memorable core ideas
- concrete everyday or workplace examples
- no visible internal labels or duration metadata
- iterative learning from the user's edited drafts

Install:

```bash
npx skills add joeseesun/qiaomu-book-script
```

Example prompts:

- “解读《被讨厌的勇气》。”
- “Write a Qiaomu-style Chinese spoken script for The Pyramid Principle.”
- “Here is my edited version. Compare the diff and update the skill benchmark.”

This skill is Chinese-first because the target output is Chinese spoken copy.
