from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "demos" / "service-boundaries" / "src"
FOI_O_SRC = ROOT / "external" / "foi-o" / "src"

sys.path.insert(0, str(SRC))
sys.path.insert(0, str(FOI_O_SRC))
