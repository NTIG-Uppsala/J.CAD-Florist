from playwright.sync_api import sync_playwright
from os import path
from datetime import datetime, timezone, timedelta
import time


def getFilePath(filePathFromRoot: str) -> str:
    filePath = path.abspath(path.join(path.dirname(__file__), "..", filePathFromRoot))
    return f"file://{filePath}"
    
resolutions : dict[str, dict[str, int]] = {
    "1080p": {"width": 1920, "height": 1080},
    "1440p": {"width": 2560, "height": 1440},
    "iPhone SE": {"width": 320, "height": 568},
    # "iPhone XR": {"width": 414, "height": 896},
    # "iPhone 12 Pro": {"width": 390, "height": 844},
    # "iPhone 14 Pro Max": {"width": 428, "height": 926},
    # "Pixel 7": {"width": 393, "height": 851},
    # "Samsung Galaxy S8+": {"width": 360, "height": 740},
    "Galaxy Fold": {"width": 280, "height": 653},
    # "iPad": {"width": 768, "height": 1024},
}

locators : dict[str, dict[str, str | None]] = {
    "top": {"selector": None, "button": None},
    "flowergram-container": {"selector": "#flowergram-container", "button": "#flowergram-btn"},
    "product-header": {"selector": "#divider-container", "button": None},
    "product-container": {"selector": "#product-container", "button": None},
    "footer": {"selector": "footer", "button": None},
}

def takeScreenshot(filePath : str, outputFile : str, resolution : dict[str, dict[str, int]], locator : dict[str, dict[str, str | None]]) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        fileUrl = getFilePath(filePath)
        page.set_viewport_size(resolution)
        page.goto(fileUrl)

        if locator['selector']: # if there is a selector, scroll to it if needed
            page.locator(locator['selector']).scroll_into_view_if_needed()
        if locator['button']: # if there is a button to click, click it
            page.click(locator['button'])
            time.sleep(0.6) # wait for the element to appear

        page.screenshot(path=outputFile)
        browser.close()

def getCurrentDateAndTime(): # function for getting the current date and time
    # Get current UTC time
    nowUtc = datetime.now(timezone.utc)

    # Define your offset (e.g., 2 hours ahead)
    offset = timedelta(hours=2)

    # Apply the offset
    offsetTime = nowUtc + offset

    # Format the datetime as required
    formattedTime = offsetTime.strftime('%Y-%m-%d-%H.%M.%S.%f')[:-3]

    return formattedTime # return the current date and time in a specific format

def genFileName(resIndex : int, locIndex : int, res : str, loc : str, currentDateAndTime : str) -> str: # function for generating the filename aswell as a folder for the current batch of screenshots
    return f"{currentDateAndTime}/{resIndex}-{locIndex}-{res}-{loc}-{currentDateAndTime}.png"

if __name__ == "__main__":
    dateAndTime = getCurrentDateAndTime() # get the current date and time for file naming
    for resIndex, res in enumerate(resolutions):
        for locIndex, loc in enumerate(locators):
            fileName = genFileName(resIndex, locIndex, res, loc, dateAndTime)
            takeScreenshot("index.html", f"generated-screenshots/{fileName}", resolutions[res], locators[loc])