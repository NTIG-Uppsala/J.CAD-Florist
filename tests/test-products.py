from utils import *

class TestProducts(TestWebsite):

    def setUp(self) -> None:
        super().setUp("index.html")
    
    def testProducts(self) -> None:
        pass