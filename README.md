<h1 align="center">FAQ Chatbot</h1>

<p align="center">
  A rule-based console chatbot that answers software-service FAQs by mapping
  keywords to intents over a JSON knowledge base.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.x">
  <img src="https://img.shields.io/badge/dependencies-none-2EA043?style=flat-square" alt="No dependencies">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square" alt="MIT License">
</p>

---

## Overview

This bot handles the questions a software agency gets asked over and over — what do you
build, what does it cost, how long does it take, do you sign an NDA — without an LLM, a
training step or a single third-party package.

It works by **keyword-to-intent mapping**. Incoming text is normalised, scanned for known
keywords, and each keyword resolves to an intent key. The answer for that intent is read
from `faq.json`. When nothing matches, the bot picks a varied fallback rather than
repeating one canned line.

The design point is separation: **`chatbot.py` holds the logic, `faq.json` holds the
content.** Adding a new answer means editing JSON, not code.

---

## How it works

```
user input
    │
    ├─ normalise (lowercase, strip)
    │
    ├─ scan against keyword_map ──► intent key
    │                                   │
    │                                   └─ look up faq.json ──► answer
    │
    └─ no keyword matched ──► random fallback prompt
```

### Intent coverage

| Intent | Triggered by |
|--------|-------------|
| `services` | services, offer |
| `pricing` | price, cost |
| `getting_started` | start, begin |
| `platforms` | platform |
| `timeline` | timeline, time |
| `team` | team |
| `technologies` | technologies, tech |
| `maintenance` | support, maintenance |
| `nda` | nda, confidential |
| `industries` | industries, domain |
| `contact` | contact, email |
| `hello` | hello, hi |
| `thank_you` | thanks, thank you |

Multiple keywords deliberately collapse onto one intent, so "how much does it cost" and
"what's the price" reach the same answer.

---

## Running it

Requires Python 3 — nothing else.

```bash
git clone https://github.com/AreeshaKhan25/chatbot-python.git
cd chatbot-python
python chatbot.py
```

Then type questions at the prompt.

```
You: what do you offer?
Bot: We offer web development, mobile app development, desktop software,
     UI/UX design, and cloud solutions.

You: how much for an app?
Bot: The cost of a mobile app varies depending on features. Basic apps
     start around $3000.
```

---

## Customising

### Change an answer

Edit the value in `faq.json`:

```json
{
  "pricing": "Projects start at $3000. Book a call for an exact quote."
}
```

### Add a new topic

1. Add the answer to `faq.json` under a new key.
2. Add one or more trigger words to `keyword_map` in `chatbot.py` pointing at that key.

```python
keyword_map = {
    "refund": "refund_policy",
    "guarantee": "refund_policy",
}
```

---

## Files

| File | Purpose |
|------|---------|
| `chatbot.py` | Keyword matching, fallback handling, console loop |
| `faq.json` | The knowledge base — every answer the bot can give |

---

## Known limits

This is a deliberately simple baseline, and it behaves like one:

- Matching is substring-based, so an unexpected phrasing with no known keyword falls
  through to the fallback.
- There is no conversation memory — each turn is handled independently.
- The first matching keyword wins; it does not rank or score competing intents.

A sensible next step would be fuzzy matching or TF-IDF similarity over the question set
instead of exact keyword hits.

---

## License

Released under the [MIT License](LICENSE).
