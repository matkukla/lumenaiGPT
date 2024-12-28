import unittest
from core import generate_response
from prompts import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES

class TestLumenAI(unittest.TestCase):
    def test_generate_response(self):
        user_input = "How do I pray the Rosary?"
        response = generate_response(SYSTEM_PROMPT, user_input, FEW_SHOT_EXAMPLES)
        self.assertIn("Praying the Rosary", response)

if __name__ == "__main__":
    unittest.main()
