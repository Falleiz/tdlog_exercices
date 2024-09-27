import unittest   
from exo2.exo import Element
class Exo2Test(unittest.TestCase):
    def  fixed_tests_True(self):
        element=Element("samurai", "ai")
        self.assertTrue(element.solution())
    
    def fixed_tests_False(self):
        element=Element("sumo",    "omo")
        self.assertFalse(element.solution())
        