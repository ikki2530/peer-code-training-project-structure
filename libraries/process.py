from libraries.common import log_message, capture_page_screenshot, browser
from libraries.mundialitis.mundialitis import Mundialitis
from config import OUTPUT_FOLDER


class Process:
    def __init__(self, credentials: dict):
        log_message("Initialization")
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_settings.popups": 0,
            "directory_upgrade": True,
            "download.default_directory": OUTPUT_FOLDER,
            "plugins.always_open_pdf_externally": True,
            "download.prompt_for_download": False
        }
        browser.open_available_browser(preferences = prefs)#browser_selection=["firefox"]
        browser.set_window_size(1920, 1080)
        browser.maximize_browser_window()
        mundialitis = Mundialitis(browser, credentials["Mundialitis"])
        mundialitis.login()
        self.mundialitis = mundialitis



    def start(self):
        log_message("Start - Register New User")
        self.mundialitis.register_new_user()
        log_message("Finish - Register New User")

    def finish(self):
        capture_page_screenshot(OUTPUT_FOLDER, "Mundialitis_Login")
        log_message("DW Process Finished")
        browser.close_browser()
