# DESIGN NOTES
## API
## Invariants
## Implementations
### OrderedDict-based (`lru_cache.py`)
- Data structure: `OrderedDict[key] = value`
- On `get`: move key to end (MRU).
- On `put`:
  - If key exists: update + move to end
  - Else if at capacity: `popitem(last=False)` (LRU)
  - Insert as MRU
- Complexity: O(1) average for both operations.
- Pros: Short, readable, battle-tested.
- Cons: Relies on library ordering; not language-agnostic.

### HashMap + Doubly Linked List (`lru_cache_o1.py`)
## Edge Cases Covered
## Testing