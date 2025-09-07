# LRU Cache (Python)

A clean implementation of an **LRU (Least Recently Used) cache** with the usual API:

- `get(key) -> int`: returns value or `-1` if missing; marks entry as **most recently used**
- `put(key, value) -> None`: inserts/updates; if at capacity, **evicts the least-recently used**

## Implementation

**`lru_cache.py`** — uses `collections.OrderedDict`
- Simple, readable, production-friendly
- **Time:** `get`/`put` = O(1) average

Avoids `while` loops and is covered by tests.

---

## Quick Start

```bash
python -V          # Python 3.9+ recommended
pip install -U pytest

# Run tests
pytest -q
```

Optional: type-check
```bash
pip install -U mypy
mypy lru_cache.py lru_cache_o1.py
```

---

## Example

```python
from lru_cache import LRUCache

c = LRUCache(2)
c.put(1, 1)
c.put(2, 2)
assert c.get(1) == 1     # 1 becomes MRU
c.put(3, 3)              # evicts 2 (LRU)
assert c.get(2) == -1
c.put(4, 4)              # evicts 1
assert c.get(1) == -1
assert c.get(3) == 3
assert c.get(4) == 4
```

---

## Files

- `lru_cache.py` — OrderedDict-based LRU
- `tests/test_lru_cache.py` — shared tests for both implementations
- `DESIGN.md` — API, invariants, complexity, and trade-offs

---

## Why two versions?

- The **OrderedDict** version mirrors how you'd likely ship this in real code: concise and maintainable.
- The **hash+DLL** version shows you understand the underlying data-structure mechanics for interviews and performance-critical constraints.

See **DESIGN.md** for details.
