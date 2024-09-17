from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime, timezone
import time

# settings for how the tests will be executed
doNotCloseBrowser = False # if True, the browser will stay open after the tests are done, otherwise it will close
hideWindow = True # if True, the browser will not be shown while the tests are executed

# ---------------------------- This section of code starts the browser and loads the website ----------------------------
chrOptions = Options()

if doNotCloseBrowser:
    chrOptions.add_experimental_option("detach", True)

if hideWindow:
    chrOptions.add_argument("--headless")

chrOptions.add_argument("--disable-search-engine-choice-screen")
# -------------------------------------------------------------------------------------------------------------------------

def initialScreenshotGen():
    if os.path.isdir("generatedScreenshots") != True: # create a folder for the screenshots if it doesn't exist
        os.mkdir("generatedScreenshots")

    subFolderName = "UTC"+getCurrentDateAndTime() # create a subfolder-name with the current time
    savePath = "generatedScreenshots/" + subFolderName + "/" # set the save path to the subfolder
    os.mkdir(savePath) # create the subfolder

    initialDesktopScreenshots(savePath)
    initialMobileScreenshots(savePath)

def initialDesktopScreenshots(savePath): # generates a screenshot of the start page in two resolutions

    driver = webdriver.Chrome(options=chrOptions) # start the browser with the options
    driver.get(os.path.join(os.path.dirname(os.getcwd()), "J.CAD-Florist", 'index.html')) # load the website

    desktopResizeAndCapture(driver, 1920, 1080, "1080p", savePath) # test for checking desktop 1080p resolution
    desktopResizeAndCapture(driver, 2560, 1440, "1440p", savePath) # test for checking desktop 1440p resolution

    driver.quit() # close the browser

def desktopResizeAndCapture(driver, width, height, resName, savePath):

    driver.set_window_size(width, height) # set the window size to the desired resolution

    scrollAndSnap(driver, savePath, resName) # scroll and take screenshots

def initialMobileScreenshots(savePath):

    mobileResolutions = ['iPhone SE', 'iPhone XR', 'iPhone 12 Pro', 'iPhone 14 Pro Max', 'Pixel 7', 'Samsung Galaxy S8+'] # list of mobile resolutions

    for res in mobileResolutions:
        mobileResizeAndCapture(res, savePath) # take a screenshot of the website with the mobile resolution

def mobileResizeAndCapture(resName, savePath):

    mobileEmulation = { "deviceName": resName } # set the device name to the desired resolution
    chrOptions.add_experimental_option("mobileEmulation", mobileEmulation) # set the mobile emulation option to the desired resolution

    driver = webdriver.Chrome(options=chrOptions) # start the browser with the options
    driver.get(os.path.join(os.path.dirname(os.getcwd()), "J.CAD-Florist", 'index.html')) # load the website

    scrollAndSnap(driver, savePath, resName) # scroll and take screenshots

    driver.quit() # close the browser
    
def scrollAndSnap(driver, savePath, resName):
    html = driver.find_element(By.TAG_NAME, 'html') # prepare for scroll

    scroll(driver, html, "top") # scroll to top
    # save screenshot of the top of the page with the resolution in the filename
    saveScreenshot(driver, savePath, resName, " top ")

    scroll(driver, html, "bottom") # scroll to bottom
    # save screenshot of the bottom of the page with the resolution in the filename
    saveScreenshot(driver, savePath, resName, " bottom ")

    productContainer = driver.find_element(By.ID, "product-container") # find the element with the id of "product-container"
    scroll(driver, html, productContainer) # scroll to the productContainer
    saveScreenshot(driver, savePath, resName, " product-container ")

    productHeader = driver.find_element(By.ID, "divider-container") # find the element with the id "divider-container"
    scroll(driver, html, productHeader) # scroll to the top of the menu
    saveScreenshot(driver, savePath, resName, " product header ")

    flowergramContainer = driver.find_element(By.ID, "flowergram-container") # find the element with the id of "welcome-center"
    scroll(driver, html, flowergramContainer) # scroll to the welcome message
    saveScreenshot(driver, savePath, resName, " flowergram-container ")

def getCurrentDateAndTime(): # function for getting the current date and time
    return datetime.now(timezone.utc).strftime('%Y-%m-%d-%H.%M.%S.%f')[:-3] # return the current date and time in a specific format

def saveScreenshot(driver, savePath, resName, id): # function for shortening the code for saving screenshots
    print(f'Saving screenshot: {resName}')
    driver.save_screenshot(savePath + resName + id + "UTC" + getCurrentDateAndTime() + ".png") 

def scroll(driver, element, target):
    if type(target) == str:
        if target == "top":
            element.send_keys(Keys.HOME) # scroll to top

        elif target == "bottom":
            element.send_keys(Keys.END) # scroll to bottom

        time.sleep(0.2) # sleep for .2 seconds so the browser has time to scroll before taking screenshot

    elif type(target) == webdriver.remote.webelement.WebElement: # if the target is an element, scroll to the element
        actions = ActionChains(driver)
        actions.move_to_element(target).perform()
    
initialScreenshotGen() # run the function to capture the screenshots