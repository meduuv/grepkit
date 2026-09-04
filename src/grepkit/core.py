from pathlib import Path

def contains(path: str|Path, needle: str, encoding="utf-8") -> bool: return needle in Path(path).read_text(encoding=encoding)
def count(path: str|Path, needle: str, encoding="utf-8") -> int: return Path(path).read_text(encoding=encoding).count(needle)
