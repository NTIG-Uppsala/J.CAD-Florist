from utils import *

class TestProducts(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="public/se/index.html")

    # Test that the products are displayed
    def testProducts(self) -> None:
        self.assertInText("Bröllopsbukett")
        self.assertInText("Rosor 10-pack")
        self.assertInText("Tulpaner 10-pack")
        self.assertInText("Sommarbukett")
        self.assertInText("Höstbukett")
        self.assertInText("Begravningskrans")
        self.assertInText("Liljor")
        self.assertInText("Hortensia")
        self.assertInText("Aloe vera")
        self.assertInText("Kaktus i kruka")

    # Test that the product prices are displayed
    def testProductPrices(self) -> None:
        self.assertInText("1 200 kr")
        self.assertInText("150 kr")
        self.assertInText("100 kr")
        self.assertInText("200 kr")
        self.assertInText("400 kr")
        self.assertInText("800 kr")
        self.assertInText("29 kr/st")
        self.assertInText("59 kr")
        self.assertInText("99 kr")
        self.assertInText("99 kr")

    # Test that the product images are displayed
    def testProductImages(self) -> None:
        self.assertInHTML('<img src="' + relativeRootDir + 'images/480x320/brollopsbukett.jpg" alt="Bröllopsbukett">')
        self.assertInHTML('<img src="' + relativeRootDir + 'images/480x320/rosor-10-pack.jpg" alt="Rosor 10-pack">')
        self.assertInHTML('<img src="' + relativeRootDir + 'images/480x320/tulpaner-10-pack.jpg" alt="Tulpaner 10-pack">')
        self.assertInHTML('<img src="' + relativeRootDir + 'images/480x320/sommarbukett.jpg" alt="Sommarbukett">')
        self.assertInHTML('<img src="' + relativeRootDir + 'images/480x320/hostbukett.jpg" alt="Höstbukett">')
        self.assertInHTML('<img src="' + relativeRootDir + 'images/480x320/begravningskrans.jpg" alt="Begravningskrans">')
        self.assertInHTML('<img src="' + relativeRootDir + 'images/480x320/liljor.jpg" alt="Liljor">')
        self.assertInHTML('<img src="' + relativeRootDir + 'images/480x320/hortensia.jpg" alt="Hortensia">')
        self.assertInHTML('<img src="' + relativeRootDir + 'images/480x320/aloe-vera.jpg" alt="Aloe vera">')
        self.assertInHTML('<img src="' + relativeRootDir + 'images/480x320/kaktus.jpg" alt="Kaktus i kruka">')


if __name__ == "__main__":
    unittest.main(verbosity=2)
