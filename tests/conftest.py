import sys
from pathlib import Path

#Adding the folders so the tests can import the scripts
ROOT = Path(__file__).resolve().parent.parent
for folder in ("Client-Server", "IEEExtreme", "Exercises", "Cryptohack"):
    sys.path.insert(0, str(ROOT / folder))
