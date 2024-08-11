from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the WebDriver (make sure to have the appropriate driver installed)
driver = webdriver.Chrome()

try:
    # Open the webpage
    driver.get("https://jqueryui.com/droppable/")

    # Wait until the frame is available and switch to it
    wait = WebDriverWait(driver, 10)
    frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".demo-frame")))
    driver.switch_to.frame(frame)

    # Locate the draggable element
    draggable = wait.until(EC.presence_of_element_located((By.ID, "draggable")))

    # Locate the droppable element
    droppable = wait.until(EC.presence_of_element_located((By.ID, "droppable")))

    # Perform the drag and drop operation using Action Chains
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(draggable, droppable).perform()

    # Optionally, you can print a message to indicate the drag and drop was successful
    print("Drag and drop operation completed successfully.")

finally:
    # Close the WebDriver
    driver.quit()
