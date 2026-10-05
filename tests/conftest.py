import sys
from pathlib import Path

# The script folders aren't packages (and "Client-Server" isn't a valid
# module name), so put each one on the import path.
ROOT = Path(__file__).resolve().parent.parent
for folder in ("Client-Server", "IEEExtreme", "Exercises", "Cryptohack"):
    sys.path.insert(0, str(ROOT / folder))
