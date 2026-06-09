---
name: qiaomu-book-script
description: |
  Generate one complete Chinese spoken short-video script for a nonfiction book, with a branded 向阳乔木 opening, a sharp author/book hook, 3-5 memorable core ideas, step-by-step reasoning from the book's ideas, concrete life scenes, and a natural ending. Use when the user gives a book title or asks for book oral scripts, 书籍口播脚本, 读书短视频脚本, 非虚构书口播, 作者介绍加核心观点, or a complete book interpretation script.
---

# Qiaomu Book Script

把一本非虚构书，变成一篇能直接念出口的完整中文短视频口播脚本。

Copyright (c) 向阳乔木
X: https://x.com/vista8
GitHub: https://github.com/joeseesun/

## Operating Mode

Run as a production-lite writing skill. The goal is not to summarize the table of contents, but to write scripts that make a viewer stop scrolling because the sentence sounds true.

Default assumptions:

- The user may input only a book title. Do not ask for confirmation; generate directly.
- Default target is Chinese short video spoken delivery.
- Default book type is nonfiction. If the title is ambiguous, infer the most likely well-known nonfiction book and state the uncertainty in one short sentence before the scripts.
- Default target length is 2-4 minutes. Prefer a tight, memorable script over exhaustive coverage.
- If a factual claim is current, recent, niche, or uncertain and browsing is available, verify it before using it. If verification is unavailable, say the uncertainty in one sentence and continue with a narrower, safer interpretation.
- Output one complete ready-to-read video script, not a four-video series.
- The script should contain 3-5 core ideas from the book. Use the number that makes the logic strongest; do not pad.
- The reasoning should unfold step by step from the book's ideas, not jump between unrelated points.
- Default opening should start with `大家好，我是向阳乔木` and may continue naturally. For recurring recommendation videos, prefer a column-like greeting such as `大家好，我是向阳乔木，又到好书推荐时间。`
- Default ending should follow the user's requested CTA. If the user does not specify one, use a clean branded closing such as `感谢你的收看，我是向阳乔木。`

## Workflow

1. Identify the book, author, field, and the most defensible reason this author is worth hearing.
2. Extract 3-5 real cognitive shifts from the book, not chapter headings.
3. Arrange the ideas into one reasoning chain:
   - name the viewer's real困境
   - introduce why the author/book is worth listening to
   - break a familiar assumption
   - build the book's better frame
   - test the frame in concrete daily scenes
   - return the insight to the viewer's own life
4. Give each core idea one concrete daily scene or detail when it improves clarity.
5. Draft one complete script that can be read aloud from start to finish.
6. Check the draft against `references/output-spec.md`.
7. For tone, structure, and compression, use `references/qiaomu-voice-benchmark.md` as the default benchmark.
8. If the user provides an edited version, compare it with the prior draft at the micro level: deletions, softened wording, concrete substitutions, concept precision, example count, final landing. Update `references/qiaomu-voice-benchmark.md` with reusable lessons rather than only preserving the edited text.
9. If writing in a file or preparing a reusable deliverable, run `python3 scripts/lint_output.py <output-file>` before calling it done.

## Output Contract

Return only the scripts, plus at most one uncertainty sentence before them when book information is insufficient.

The script must be wrapped in one fenced code block.

```text
大家好，我是向阳乔木，又到好书推荐时间。

[完整口播文案，只包含观众能听见的内容。]

感谢你的收看，我是向阳乔木。
```

Do not print internal labels or metadata such as:

- `第零条：作者介绍与系列引入`
- `第一条：核心观点一`
- `第二条：核心观点二`
- `第三条：核心观点三与系列收尾`
- `主题一`
- `核心观点一`
- `预估时长：约 55 秒`

Use structure internally, but hide the structure from the visible script. The code block should contain only complete spoken words.

## Style And Constraints

Follow `references/output-spec.md` as the writing contract.

Non-negotiables:

- Conversational Chinese. It should sound like a person talking, not a host reading a report.
- Short paragraphs. One sentence should carry one thought.
- Prefer short, hard-hitting reasoning over exhaustive coverage.
- Start with a strong cognitive anchor when possible: author comparison, counterintuitive claim, forgotten figure, surprising framing, or a conflict between two schools of thought.
- Precise verbs over stacked adjectives.
- 3-5 core ideas, each with concrete scenes over abstract advice.
- Prefer plain, accurate, slightly softened speech over clever metaphors or accusatory phrasing.
- Remove self-commentary such as `这句话很重`, `所以你看`, and extra final maxims when the main conclusion already lands.
- Sincerity over completion-rate tricks.
- Chinese punctuation throughout the spoken text.
- Important claims may use Markdown bold markers, for example `**真正困住人的，不是选择太少，是不敢承认自己已经选了。**`

Do not use:

- forced hook phrases such as `你知道吗`, `今天我要告诉你`, `重点来了`, `接下来告诉你`, `划重点`
- the forbidden sentence patterns, words, and structural habits listed in `references/output-spec.md`
- em dashes, horizontal rules, stage directions, or delivery annotations such as `【停顿】`

## Boundaries

- Do not invent book content, author experiences, data, quotes, awards, or publication history.
- Do not pretend to cover the whole book when only one idea is known well. It is better to go deep on fewer safe ideas than to dilute the script with vague coverage.
- Do not use direct quotations from copyrighted books unless the user supplied the excerpt or the quote is short and clearly necessary.
- Keep any requested CTA brief. Do not turn the ending into a long sales pitch for buying the book, courses, accounts, or products.
- Do not generate scripts for a book you cannot identify without first stating the uncertainty.

## Reference Files

- `references/output-spec.md`: full writing rules, forbidden expressions, output shape, and self-check.
- `references/qiaomu-voice-benchmark.md`: user-approved benchmark principles distilled from the tuned 《被讨厌的勇气》 script.
- `scripts/lint_output.py`: lightweight checker for four-code-block structure and common forbidden expressions.
