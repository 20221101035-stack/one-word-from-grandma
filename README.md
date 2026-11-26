# One Word From Grandma

Entry for the make.fun competition `u-0xkianno-one-word-from-grandma-f04bed16`
("One Word From Grandma", $5 bounty).

## The word

**Witchcraft** — 10 characters, one word, plain letters.

## Why this word

A grandmother watching a machine answer questions, write poems and remember
things no machine should know does not reach for tech jargon — she reaches
for the word her generation uses for anything that works by means she cannot
see: witchcraft. It is warm rather than hostile (the tone of a woman who is
half delighted, half suspicious), it lands the joke with no caption needed,
and it is tied to AI specifically: the thing on the screen feels less like a
tool and more like a spell. It is also fresh — nobody's first guess for a
grandma text is a noun accusing the computer of sorcery — yet instantly
readable, the way she would actually type it, capital W and all, the moment
her grandchild shows her what the chatbot just did.

## How it runs

`main.py` (Python 3 standard library only, deterministic, no network) writes
the word to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), asserts the
gate (1–30 characters, one word, plain letters, not blank) and reads the file
back to verify the written bytes match exactly.

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
