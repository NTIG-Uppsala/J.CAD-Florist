from playwright.sync_api import sync_playwright
from os import path, mkdir
from datetime import datetime, timezone, timedelta
import time

screenshotFolder: str = "generated-screenshots" # folder for the screenshots

def getPagePath(pagePathFromRoot: str) -> str: # function for getting the file path for the page to screenshot
    pagePath = path.abspath(path.join(path.dirname(__file__), "..", pagePathFromRoot))
    return f"file://{pagePath}"
    
resolutions : dict[str, dict[str, int]] = { # resolutions for the screenshots
    "1080p": {"width": 1920, "height": 1080},
    "1440p": {"width": 2560, "height": 1440},
    "iPhone SE": {"width": 320, "height": 568},
    "iPhone XR": {"width": 414, "height": 896},
    "iPhone 12 Pro": {"width": 390, "height": 844},
    "iPhone 14 Pro Max": {"width": 428, "height": 926},
    "Pixel 7": {"width": 393, "height": 851},
    "Samsung Galaxy S8+": {"width": 360, "height": 740},
    "Galaxy Fold": {"width": 280, "height": 653},
    "iPad": {"width": 768, "height": 1024},
}

locators : dict[str, dict[str, str | None]] = { # locators for scrolling to specific elements on the page and clicking buttons if needed
    "top": {"selector": None, "button": None},
    "flowergram-container": {"selector": "#flowergram-container", "button": "#flowergram-btn"},
    "product-header": {"selector": "#divider-container", "button": None},
    "product-container": {"selector": "#product-container", "button": None},
    "footer": {"selector": "footer", "button": None},
}

def takeScreenshot(pagePath : str, outputFile : str, resolution : dict[str, dict[str, int]], locator : dict[str, dict[str, str | None]]) -> None: # function for taking a screenshot of a page
    with sync_playwright() as p: # create a new playwright instance
        browser = p.chromium.launch(headless=True) # launch browser hidden
        page = browser.new_page() # create a new page

        fileUrl = getPagePath(pagePath) # get the file path for the page to screenshot 
        page.set_viewport_size(resolution) # set the resolution of the page to screenshot
        page.goto(fileUrl) # go to the page

        if locator['selector']: # if there is a selector, scroll to it if needed
            page.locator(locator['selector']).scroll_into_view_if_needed()
        if locator['button']: # if there is a button to click, click it
            page.click(locator['button'])
            time.sleep(0.6) # wait for the element to appear

        page.screenshot(path=outputFile) # take a screenshot of the page and save it to the output file
        browser.close() # close the browser

def getCurrentDateAndTime() -> str: # function for getting the current date and time
    nowUtc = datetime.now(timezone.utc) # get the current date and time in UTC
    offset = timedelta(hours=2) # set the offset for the current date and time
    offsetTime = nowUtc + offset # apply the offset to the current date and time
    formattedTime = offsetTime.strftime('%Y-%m-%d-%H.%M.%S.%f')[:-3] # format the current date and time

    return formattedTime # return the current date and time in a specific format

def genFileName(resIndex : int, locIndex : int, res : str, loc : str, currentDateAndTime : str) -> str: # function for generating the filename aswell as a folder for the current batch of screenshots
    return f"{resIndex}-{locIndex}-{res}-{loc}-{currentDateAndTime}.png" # return the filename for the screenshot to be taken 

if __name__ == "__main__":
    dateAndTime = getCurrentDateAndTime() # get the current date and time for file naming

    if not path.isdir(screenshotFolder): # create a folder for the screenshots if it doesn't exist
        mkdir(screenshotFolder)

    for resIndex, res in enumerate(resolutions): # loop through the resolutions and locators
        for locIndex, loc in enumerate(locators):
            folderName = dateAndTime # folder for the current batch of screenshots
            fileName = genFileName(resIndex, locIndex, res, loc, dateAndTime) # generate the filename for the screenshot to be taken 
            takeScreenshot("index.html", f"{screenshotFolder}/{folderName}/{fileName}", resolutions[res], locators[loc])