import tempfile,unittest
from pathlib import Path
from grepkit import contains,count
class Tests(unittest.TestCase):
 def test_search(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"x";p.write_text("abc abc")
   self.assertTrue(contains(p,"abc"));self.assertEqual(count(p,"abc"),2)
if __name__=="__main__":unittest.main()
