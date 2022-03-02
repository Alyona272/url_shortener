import hashlib


def short(raw: str) -> str:
    hash = hashlib.sha1(raw.encode('utf-8')).hexdigest()
    return hash[:10]
