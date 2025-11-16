# Week 1 — Python for Data & APIs (the LLM groundwork) — Overview

Welcome to Week 1. Before we touch any model, we’ll master the text-in/text-out plumbing that every LLM app relies on. By Friday, you’ll be fluent at pulling data from the web, cleaning it so code doesn’t break, and saving it in shapes your future LLM can digest—cleanly, safely, and fast enough to matter.

---

## Why this week matters (picture the pipeline)

Every LLM app is a **text pipeline**:

**User text → (clean/validate) → call API → (parse JSON) → transform → save/show**

If any arrow is weak, the whole thing wobbles. This week you’ll build each arrow yourself so, in later weeks, dropping a model in the middle feels… almost boring (in the best way).

---

## What we’ll explore (with plain-English “why” + quick links)

* **Strings that don’t surprise you**
  Working with slices, f-strings, and surgical find/replace using **regular expressions** so messy input doesn’t break your logic.
  What: [Regex](https://en.wikipedia.org/wiki/Regular_expression) • [Python `re` basics](https://docs.python.org/3/library/re.html)
  Why: Real users paste weird stuff; regex lets you shape it first.

* **Data that round-trips cleanly**
  Serialize/deserialize **JSON** into Python dicts/lists. Know the difference between `null` vs empty, strings vs numbers, and how nested structures behave.
  What: [JSON spec](https://www.json.org/) • [Python `json` module](https://docs.python.org/3/library/json.html)
  Why: LLMs “eat” text, but your app needs structured data to reason.

* **Talking to the web**
  Make **HTTP** requests, read status codes, headers, and query params without buzzwords.
  What: [HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP) • [Status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) • [Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
  Why: Most real data lives behind an API; you need to ask politely and read the reply precisely.

* **REST without mystique**
  Endpoints, resources, pagination styles (`?page=…`, `offset/limit`, cursor tokens), and **idempotency** (when it’s safe to retry).
  What: [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) • [Idempotence](https://en.wikipedia.org/wiki/Idempotence)
  Why: Prevent accidental duplicates and handle multi-page results confidently.

* **A peek at async**
  Fetch multiple things “at once” using `async`/`await`—gently, and only where it helps.
  What: [Python `asyncio`](https://docs.python.org/3/library/asyncio.html)
  Why: Later, you’ll fan-out requests for embeddings or retrieval; small speedups add up.

* **Errors that teach (not torch)**
  Use `try/except`, typed exceptions, and friendly messages. Learn **retries with exponential backoff** and tiny **circuit-breaker** habits.
  What: [Exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff)
  Why: Networks hiccup; polite retries keep you from getting blocked.

* **Secrets where they belong**
  Keep API keys in `.env` and load them at runtime; practice basic **rate limiting** manners.
  What: [`python-dotenv`](https://pypi.org/project/python-dotenv/) • [Rate limiting](https://en.wikipedia.org/wiki/Rate_limiting)
  Why: Leaks get you banned; rate-limit etiquette keeps you welcome.

* **Files you can trust later**
  Read/write text, JSON, and **JSON Lines (JSONL)**; set a tiny `data/` convention.
  What: [JSON Lines](https://jsonlines.org/)
  Why: JSONL is perfect for logs, training data, and reproducible runs.

---

## What you’ll build this week

1. **Hello-API → Clean → Save**
   A small script that calls a **keyless public API**, validates and normalizes the response, and saves results to `data/results.jsonl`. You’ll handle non-200 responses and add one polite retry.

2. **Mini “Explorer” CLI (starter)**
   A command you can run like:

   ```bash
   python explorer.py search "query" --limit 5 --format table|json
   ```

   It fetches from one provider, prints a tidy table or JSON, and never crashes on a bad response. (Next week: add caching, async fan-out, and a second provider.)

> **Starter code:** We’ll give you a scaffold repo with `client.py`, `parse.py`, `cli.py`, `settings.py`, and a tiny `tests/` folder. You’ll fill in the blanks and keep each function small and testable.

---

## How the week runs

**Session A — Theory & live code (2h)**

* Read an API doc the “engineer way”: identify base URL, path, params, and pagination.
* Make your first request; inspect headers and body.
* Parse JSON safely (defensive `.get()`), and write a minimal normalizer.
* Micro-quiz: “Which codes to retry? Where does `Authorization` live? What does `idempotent` buy you?”

**Session B — Lab 1 (2h)**

* Bring up the scaffold.
* Implement `get_json(url, params)` with timeouts + one retry (with jitter).
* Write `normalize_item(raw)` that returns just the fields you care about.
* Save results to `data/results.jsonl`.
* Add one table printout (name, type, id—whatever your API returns).

**Session C — Lab 2 (2h)**

* Add a simple `--limit` flag and “friendly failure” messages.
* Handle pagination for your chosen API (pick the style it uses).
* (Optional preview) Add an `async` version for multi-query runs.

**End of week — Assignment**

* Package your mini “Explorer” CLI, write a short README, and record a 60-second demo (run → show a failure handled gracefully → re-run).

---

## By the end of Week 1, you will be able to…

* Fetch from a public API with a timeout, explain a non-200 response, and choose whether to retry.
* Normalize nested JSON into a small, predictable Python shape.
* Clean user input (trim, case, regex) **before** it hits your request.
* Save to JSONL and load it back without type surprises.
* Explain, in your own words, what an HTTP request/response contains and why idempotency matters.

---

## Concepts introduced this week (nano-glossary you’ll refer back to)

* **HTTP status codes** — 200 (OK), 4xx (your fault), 5xx (their fault).
  Read: [MDN status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

* **Headers & query params** — how auth and filters travel with requests.
  Read: [MDN headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

* **Idempotency** — safe to retry? `GET` is; many `POST`s aren’t unless designed that way.
  Read: [Idempotence](https://en.wikipedia.org/wiki/Idempotence)

* **Pagination** — `?page=`, `offset/limit`, cursor tokens in `Link` headers.
  Read: [RFC 5988 (Web Linking)](https://www.rfc-editor.org/rfc/rfc5988)

* **JSON Lines (JSONL)** — one JSON object per line; easy to append and stream.
  Read: [jsonlines.org](https://jsonlines.org/)

* **Exponential backoff** — slower, spaced retries that don’t hammer servers.
  Read: [Why backoff works](https://en.wikipedia.org/wiki/Exponential_backoff)

* **Async fan-out (preview)** — start multiple requests without waiting on each one.
  Read: [asyncio](https://docs.python.org/3/library/asyncio.html)

---

## What to do when you get stuck

1. **State the goal in one sentence.** “I want 5 items that match ‘pikachu’.”
2. **Print the important parts.** The URL, params, and the first 200 chars of the body.
3. **Check the contract.** Does the API promise those fields? Handle `None` if it doesn’t.
4. **Start small.** One item first; add pagination after it works.
5. **Write one test.** Feed a tiny fixture to your normalizer; assert two fields.
6. **Decide on retry or fail.** Retry only `429/5xx` and only a couple of times.

---

## Low-spec laptop tips

* Choose **keyless** APIs and keep `--limit` small while developing.
* Use JSONL (line-by-line) and avoid loading huge responses into memory.
* Keep your functions tiny so they’re fast to test and easy to reason about.

---

## Light prep (optional)

* Quickstart for HTTP in Python: [requests](https://requests.readthedocs.io/en/latest/user/quickstart/) or [httpx](https://www.python-httpx.org/quickstart/)
* Skim the first screen of [asyncio](https://docs.python.org/3/library/asyncio.html) (stop as soon as it feels heavy).
* Bring one public API you actually care about (no auth needed preferred).

---

## What “done” looks like this week

* Your CLI fetches, cleans, and prints **without crashing** on weird inputs.
* You can point at a log line and explain what happened, in English.
* Your repo has `.env.example`, a `data/` folder, and **zero secrets** committed.

Nail these, and Week 2 (caching, retries/backoff, async fan-out, multi-API merge) will feel like an upgrade—not a rewrite.
