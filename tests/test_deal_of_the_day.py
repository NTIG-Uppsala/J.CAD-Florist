from utils import *


class TestDealOfTheDay(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    # define an array of objects that represent which product is the deal of the day for each day that the deal of the day is relevant

    # find the visible element with the deal of the day
    # check that it is accurate relative to the current date and that the price is correct
        # if current day is x then the deal of the day should be visible on product X
        # if current day is y then the deal of the day should be visible on product Y