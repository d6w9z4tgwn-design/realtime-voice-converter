import unittest,numpy as np
from app import Modulator
class Test(unittest.TestCase):
 def test_continuity(self):
  x=np.ones((100,1));a=Modulator(48000,80,1);b=Modulator(48000,80,1);np.testing.assert_allclose(np.concatenate([a.process(x[:30]),a.process(x[30:])]),b.process(x),atol=1e-12)
