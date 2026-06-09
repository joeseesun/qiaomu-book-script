# Book Spoken Script Output Spec

## Core Goal

When someone reads the script aloud, the viewer should feel that a real truth just found them.

The writing should not sound like a viral formula. It should sound like someone who read the book carefully and knows where the idea touches ordinary life.

## Required Script Structure

Output one complete script only.

The script should include 3-5 core ideas from the book. These are internal reasoning units, not visible headings. Use the number that makes the script strongest; do not pad to satisfy a checklist.

Recommended reasoning chain:

1. Start from the viewer's real困境 or painful everyday pattern.
2. Explain why this author or book is worth listening to.
3. Break a familiar assumption.
4. Build the book's better frame.
5. Test the frame in concrete daily scenes.
6. Return the insight to the viewer's own life.
7. Close with the user's requested CTA or a clean branded ending.

For 《被讨厌的勇气》, a strong chain may include:

- 目的论：人不只被过去推着走，也会为了某种目的选择现在的行为。
- 课题分离：分清自己的责任和别人的评价。
- 被讨厌的勇气：自由意味着不再把所有人的认可当作通行证。
- 共同体感觉：真正的自由不是孤立，而是在关系里找到贡献感。

## Output Format

The final script must be wrapped in one fenced code block.

The code block must contain only spoken text that can be read directly in the video.

The script must start with a branded greeting. It may continue naturally after the name. For recurring recommendation videos, prefer a column-like opening:

```text
大家好，我是向阳乔木，又到好书推荐时间。
```

The script must end with the user's requested closing when provided. If no closing is specified, use a clean branded closing:

```text
感谢你的收看，我是向阳乔木。
```

Do not show internal metadata in the final code blocks:

- no `第零条：作者介绍与系列引入`
- no `第一条：核心观点一`
- no `第二条：核心观点二`
- no `第三条：核心观点三与系列收尾`
- no `主题一`
- no `核心观点一`
- no `预估时长`
- no planning notes

The visible output should look like:

```text
大家好，我是向阳乔木，又到好书推荐时间。

完整口播文案。

感谢你的收看，我是向阳乔木。
```

Do not add an explanation of the framework after the scripts.

If book information is insufficient, add one short sentence before the first code block, for example:

```text
我对这本书的版本信息不完全确定，下面按最常见的中文译名与核心主题来写。
```

Then continue. Do not stop.

## Book Content Rules

- Extract the few ideas that actually change cognition after reading the book.
- Do not retell the table of contents.
- Do not force unrelated talking points.
- Include 3-5 core ideas by default.
- The themes must have an inner reasoning sequence, not a listicle feel.
- Every core theme needs a concrete daily scene or detail.
- If knowledge is uncertain, narrow the claim and write the part you can defend.
- Prefer fewer well-understood themes over many vague claims. If the user explicitly requests a minimum number, satisfy it only when the ideas remain strong.

## Author Introduction Rules

- Do not write a Wikipedia-style biography.
- Explain why this person is worth hearing.
- If the author has a counterintuitive identity, experience, research path, or position, use that as the entry.
- Comparison with other people in the field can quickly create a cognitive anchor, but do not smear others.

## Opening Rules

Do not design a hook by using hook phrases.

Ask this instead:

```text
If I had only 3 seconds with a stranger, what sentence would make them stop?
```

The opening may be:

- an unexpected fact
- a painful question
- a counterintuitive claim
- a sentence that names a truth people usually avoid
- a contrast between two thinkers, schools, or common explanations
- a forgotten author or overlooked reason this book matters

Avoid:

- `你知道吗`
- `今天我要告诉你`
- a long setup before the real point

## Ending Rules

Each script should land emotionally before the final closing line.

Use the user's requested closing line when provided, for example:

```text
感谢你的收看，如果觉得内容有帮助，请一键三连。
```

Do not add more selling after it. Do not ask the viewer to buy the book, join a course, click a link, or follow an account unless the user explicitly asks.

If the user does not specify a CTA, prefer:

```text
感谢你的收看，我是向阳乔木。
```

## Voice

- Oral, conversational, and human.
- Short paragraphs.
- One sentence, one thought.
- Short, sharp logical moves beat long explanatory coverage.
- A strong script often uses a simple comparison early, for example one thinker says A, another says B.
- Restrained. No adjective piles.
- Sincere. No anxiety farming.
- Admit complexity when the idea deserves it.
- Use data and details only when they are true and useful.
- Give the viewer a feeling of "now I see it."

## Forbidden Sentence Patterns

Do not use:

- `不是……而是` when it is used as a lazy formula. It is allowed when the contrast is genuinely clarifying, for example `不是没有想法，而是想法太散，没有结构和顺序。`
- `想象一下`
- `你有没有想过`
- `值得注意的是`
- `不难理解`
- `毋庸置疑`
- `随着……的发展`
- `对于……来说`
- `首先……其次……最后`

## Forbidden Words

Do not use:

- `震惊`
- `绝了`
- `太牛了`
- `赋能`
- `落地`
- `深度融合`
- `内卷`
- `这个时代`
- `年轻人`
- `精准打击`

## Forbidden Structural Phrases

Do not use:

- `重点来了`
- `接下来告诉你`
- `划重点`
- similar forced rhythm markers

## Punctuation And Markup

- Use Chinese punctuation in the spoken text: `，` `。` `：` `？` `、` `《》`
- Do not use em dashes.
- Do not use horizontal rules.
- Do not include delivery annotations such as `【停顿】` or `【加重】`.
- Important ideas may be marked with `**加粗**`.
- Keep the script pure spoken text. Do not add camera directions, music notes, subtitles, shot lists, visible section labels, or duration metadata unless the user explicitly asks.

## Self-Check

Before returning, check:

- There is exactly one fenced code block.
- The script starts with `大家好，我是向阳乔木`
- The script ends with the user's requested closing, or a clean branded closing if none was specified.
- The script contains 3-5 strong core ideas from the book, unless the user explicitly requested a different number.
- The themes unfold as reasoning, not as visible headings or disconnected list items.
- No visible `第零条`、`第一条`、`第二条`、`第三条` labels appear inside the code block.
- No visible `主题一` or `核心观点一` labels appear inside the code block.
- No `预估时长` appears inside the code block.
- The author intro answers why this author is worth listening to.
- Every core theme has one concrete life scene.
- No forbidden phrases or words appear.
- The opening does not start with empty hook language.
- The ending is short and does not expand into a sales pitch.
- The text sounds natural when read aloud.

## Benchmark Style Notes

For scripts like 《被讨厌的勇气》, prefer this shape:

- Use author contrast early: `弗洛伊德说……阿德勒说……`
- State the uncomfortable thesis plainly.
- Explain the logic in one or two clean steps.
- Use ordinary examples only after the idea is clear.
- Keep transitions short.
- Stop before the script becomes a lecture.
- The best line should be easy for the viewer to repeat.

Use `references/qiaomu-voice-benchmark.md` as the concrete benchmark for Qiaomu's preferred script rhythm. Key lessons from the user-edited version:

- Prefer `过去发生了什么很重要，但更重要的是，你现在怎么看过去。` over harsher blame-like framing.
- Explain concepts as `概念名 -> 一句话解释 -> 生活例子 -> 结论`.
- Use ordinary examples: 写完又删的消息、不想去的饭局、删掉发出去的内容、拒绝朋友后反复解释。
- Keep the conclusion simple: `真正的自由，不是让所有人都喜欢你。真正的自由，是你终于不用为了被喜欢，而委屈自己。`
- Default closing can be `感谢你的收看，我是向阳乔木。`

## Revision Learning Loop

When the user edits a generated script, treat the edit as preference evidence. Do not only say "understood". Compare the two drafts and extract reusable style rules.

Look especially for:

- **Deleted sentences**: often signal overexplaining, filler, moral pressure, or performative cleverness.
- **Softened words**: often signal a preference for direct but non-punitive phrasing.
- **More concrete nouns**: often signal that vague terms should be replaced with visible actors or situations.
- **Repeated book concepts**: often signal that using the author's own conceptual vocabulary is better than paraphrasing too loosely.
- **Shorter examples**: often signal the ideal number of examples before a section starts dragging.
- **Changed ending**: often shows where the emotional landing should stop.

For the user-tuned 《被讨厌的勇气》 revision, the hidden preferences were:

- Replace harsh narrator judgment with measured framing: `说得更狠` became `说：`; `刺耳` became `很难被很多人接受`.
- Replace accusatory agency language with interpretive agency: `怎么使用过去` became `怎么看过去`.
- Keep the concept exact and simple: `最核心的第一件事` became `最核心的概念`.
- Make examples more concrete with one small noun: `小时候总被否定` became `小时候总被大人否定`.
- Preserve precise topic words instead of shortening too soon: `不适合关系` became `不适合亲密关系`.
- Reduce drama: `过去太痛` became `过去难以忘怀`; `很痛` became `很难`.
- Compress paired sentences when oral rhythm improves: `这不是否认伤害。伤害当然是真的。` became `这不是否认伤害，伤害肯定会有。`
- Prefer agency language over ornate metaphor: `不能自动获得你余生的管理权` became `不能影响你的人生主动权`.
- Remove extra examples when two examples already prove the point: the `父母一句...人生答辩` example was deleted.
- Prefer natural fear language over clever prediction language: `还提前替对方生气` became `生怕对方生气`.
- Use the book's vocabulary when it is clearer: `替别人活完他的反应` became `替别人承担课题`.
- Delete directive filler: `然后放手` was removed from `你把自己的部分做好，剩下的，不全是你的事`.
- Shorten abstract phrases: `人生目标` became `目标`.
- Replace abstract internal change with visible behavior: `改过自己的观点` became `附和别人的观点`.
- Add uncertainty when guessing motivation: `因为觉得回应太少` became `可能觉得回应太少`.
- Delete meta-emphasis: `这句话很重` was removed.
- Use grammatically natural explanatory verbs: `它是明白一件事` became `它是让你明白一件事`.
- Align with book terminology: `我和别人有关，我在这里有用` became `我和他人有关，我在对他人有用`.
- Prefer common speech over polished phrasing: `没有急着教育他` became `没急着教育他`.
- Avoid trendy comparative words when simpler words work: `更稳` became `更好`.
- Remove transition filler: `所以你看` was deleted.
- Make the final contrast active and burden-focused: `不是所有人都喜欢你` became `不是让所有人都喜欢你`.
- Prefer everyday emotional language over literary imagery: `一点点删掉自己` became `委屈自己`.
- Stop after the clean final insight. The extra line `你不能决定别人怎么看你...` was deleted because the conclusion had already landed.

For the user-tuned 《金字塔原理》 revision, the hidden preferences were:

- Use recurring-program opening when appropriate: `今天我给大家推荐一本书` became `又到好书推荐时间`.
- Make workplace dialogue shorter and more oral: `所以你到底想说什么？` became `你到底想说啥？`.
- Compress biography: `曾经在麦肯锡工作` became `曾在麦肯锡工作`.
- Diagnose the real failure mode: `想法没有顺序` became `想法太散，没有结构和顺序`.
- Prefer numbered/simple setup: `这套结构听起来很简单` became `听起来不复杂，四个词就能概括`.
- Compress instructions: `先把答案给出来` became `先给答案`.
- Combine tightly related sentences: `后面的信息...它们都...` became `后面的信息，不再是一堆材料，而是变成了...`.
- Add natural helper verbs: `真的支撑` became `真的能支撑`.
- Remove hedging when teaching logic: `不一定支撑` became `不支撑`.
- Prefer practical explanation over moral pressure: `尊重听众的大脑 / 没有义务` became `照顾听众的大脑 / 大脑...最怕整理散乱的内容`.
- Use native business verbs: `理由摆整齐` became `理由码齐`; `只能先做` became `建议先做`.
- Prefer practical clarity over metaphor: `还在雾里` became `还没想明白`.
