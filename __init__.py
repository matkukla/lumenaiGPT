# lumenaiGPT/__init__.py

# Import core functionalities
from core import generate_response
from prompts import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES

# Optional: Define package metadata
__all__ = ["generate_response", "SYSTEM_PROMPT", "FEW_SHOT_EXAMPLES"]
__version__ = "0.1.0"
