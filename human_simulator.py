from selenium.webdriver import ActionChains, Keys
import random
import time
import logging

class HumanSimulator:
    """
    Simulates human-like interactions for undetectable web scraping.
    Features randomized cursor paths, typing errors, breaks, and navigation.

    Impact:
    Enabled 100s of hours of LinkedIn automation in 2024 and 2025, never once getting an account banned or locked.
    Enabled 50+ sent requests and 100s of conversations handled per day, 40-60% LinkedIn connection acceptance rates in production.
    """
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)
        # Redacted: Proprietary evasion logic (available under NDA)
        self.last_position = [0, 0]  # Placeholder for cursor tracking

    def move_cursor(self, element, click=True, margin=0.2):
        """Moves cursor in a human-like curved path to element, with optional click.
        Reduces detection by avoiding straight-line movements."""
        # Redacted: Proprietary path simulation (available under NDA)
        target_x, target_y = self._get_point_within_element(element, margin)
        self.action.move_by_offset(target_x, target_y).perform()
        if click:
            self.action.click().perform()
        self.last_position = [target_x, target_y]
        time.sleep(random.uniform(0.2, 0.5))  # Human pause

    def _get_point_within_element(self, element, margin):
        """Calculates random interior point for natural interaction."""
        loc = element.location
        size = element.size
        x = loc['x'] + size['width'] * (margin + random.random() * (1 - 2 * margin))
        y = loc['y'] + size['height'] * (margin + random.random() * (1 - 2 * margin))
        return x, y

    def simulate_typing(self, element, text):
        """Types text with occasional errors and corrections for realism.
        Mimics 60-80 WPM with variability, evading detection with simulated human-behavior."""
        element.click()
        prev_char = ''
        for char in text:
            if random.random() < 0.005:  # Mistake chance
                wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz')
                self.action.send_keys(wrong_char).perform()
                time.sleep(random.uniform(0.3, 0.5))
                self.action.send_keys(Keys.BACKSPACE).perform()
            self.action.send_keys(char).perform()
            delay = random.uniform(0.1, 0.3) if char == ' ' else random.uniform(0.05, 0.15)
            time.sleep(delay)
            prev_char = char

    def take_break(self, min_duration=60, max_duration=300):
        """Simulates human rest breaks to avoid rate-limiting.
        Avoids detection by spacing actions naturally."""
        duration = random.randint(min_duration, max_duration)
        logging.info(f"Simulating break for {duration} seconds.")
        time.sleep(duration)

    def navigate_randomly(self):
        """Performs random navigation to mimic browsing behavior.
        Includes feed scrolling and settings checks for human behavior simulation and session longevity."""
        # Redacted: Proprietary navigation sequences (available under NDA)
        self.action.move_by_offset(random.randint(-50, 50), random.randint(-50, 50)).perform()
        time.sleep(random.uniform(1, 3))  # Pause for 'reading'

    def scroll_humanly(self, element=None, distance=100):
        """Scrolls with variable speed and pauses, like wheel usage."""
        for _ in range(abs(distance) // 50):
            direction = 50 if distance > 0 else -50
            script = f"arguments[0].scrollBy(0, {direction});" if element else f"window.scrollBy(0, {direction});"
            self.driver.execute_script(script, element)
            time.sleep(random.uniform(0.1, 0.2))

# Usage Example
if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()  # Replace with your setup
    sim = HumanSimulator(driver)
    driver.get("https://example.com")
    elem = driver.find_element("id", "input-field")
    sim.move_cursor(elem, click=False)
    sim.simulate_typing(elem, "Hello, world!")
    sim.take_break(10, 20)
    sim.scroll_humanly(distance=200)
    sim.navigate_randomly()
    driver.quit()

# Human Behavior Demo Method
# The following code was used to execute the demo in this screen recording: https://youtu.be/hEM3Gfyi9Vo
    # def portfolio_demo(self):
    #     iframe = self.wait_to_find_elem("//iframe[@id='iframeResult']")
    #     self.driver.switch_to.frame(iframe)
    #     self.cursor.insert_canvas()

    #     logging.debug("Starting cursor idling for natural behavior simulation.")
    #     self.cursor.start_idling()
    #     logging.debug("Pausing for a human-like delay around 3 seconds to mimic reading or thinking.")
    #     self.dreamer.sleep(3)
    #     logging.debug("Canceling cursor idling to proceed with actions.")
    #     self.cursor.cancel_idling()

    #     text_box = self.wait_to_find_elem("//input[@id='message-input']")
    #     logging.debug("Moving cursor to the text box with passive idling mode turned off.")
    #     self.cursor.to_elem('aa', text_box, mode=None)

    #     text = "Hello, World!"
    #     logging.debug(f"Simulating typing: '{text}'.")
    #     simulate_typing(self, text)

    #     send_button = self.wait_to_find_elem("//button[contains(normalize-space(), 'Send')]")
    #     logging.debug("Moving cursor to the send button.")
    #     self.cursor.to_elem('ab', send_button)

    #     logging.debug("Moving cursor back to the text box with passive idling mode turned off.")
    #     self.cursor.to_elem('aa', text_box, mode=None)

    #     text = "This is to demonstrate the humanlike behavior of the program. 🧐"
    #     logging.debug(f"Simulating typing: '{text}'.")
    #     simulate_typing(self, text)

    #     logging.debug("Moving cursor to the send button.")
    #     self.cursor.to_elem('ab', send_button)

    #     self.cursor.move_off_screen("right")
    #     self.driver.switch_to.default_content()
    #     self.cursor.insert_canvas()

    #     theme_btn = self.wait_to_find_elem("//a[@title='Change Theme']")
    #     logging.debug("Moving cursor to the theme button.")
    #     self.cursor.to_elem('ac', theme_btn)

    #     self.cursor.move_off_screen("right")
    #     self.driver.switch_to.frame(iframe)
    #     self.cursor.insert_canvas()

    #     logging.debug("Moving cursor to the text box with passive idling mode turned off.")
    #     self.cursor.to_elem('aa', text_box, mode=None)

    #     text = "Mwahaha I changed the theme 😈"
    #     logging.debug(f"Simulating typing: '{text}'.")
    #     simulate_typing(self, text)
    #     self.dreamer.sleep(0.5)
    #     text = " now, for my next trick......."
    #     logging.debug(f"Simulating typing: '{text}'.")
    #     simulate_typing(self, text)

    #     logging.debug("Moving cursor to the send button.")
    #     self.cursor.to_elem('ab', send_button)

    #     logging.debug("Pausing for a human-like delay around 2 seconds to simulate natural delay.")
    #     self.dreamer.sleep(2)

    #     self.cursor.move_off_screen("right")
    #     self.driver.switch_to.default_content()
    #     self.cursor.insert_canvas()

    #     orientation_btn = self.wait_to_find_elem("//a[@title='Change Orientation']")
    #     logging.debug("Moving cursor to the orientation button.")
    #     self.cursor.to_elem('ae', orientation_btn)

    #     self.cursor.move_off_screen("right")
    #     self.driver.switch_to.frame(iframe)
    #     self.cursor.insert_canvas()

    #     results_box = self.wait_to_find_elem("//html")
    #     logging.debug("Moving cursor to the results box with passive idling mode turned off.")
    #     self.cursor.to_elem('ag', results_box, click=False, mode=None)

    #     logging.debug("Scrolling to the send button element.")
    #     self.cursor.scroll_to_elem('aa', send_button)

    #     logging.debug("Moving cursor to the text box with passive idling mode turned off.")
    #     self.cursor.to_elem('ah', text_box, mode=None)

    #     text = "Impressed? ;)"
    #     logging.debug(f"Simulating typing: '{text}'.")
    #     simulate_typing(self, text)

    #     logging.debug("Moving cursor to the send button.")
    #     self.cursor.to_elem('ai', send_button)

    #     self.cursor.scroll_to_top()
