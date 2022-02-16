from libraries.common import act_on_element, capture_page_screenshot
from config import OUTPUT_FOLDER


class Mundialitis():

    def __init__(self, rpa_selenium_instance, credentials: dict):
        self.browser = rpa_selenium_instance
        self.mundialitis_url = credentials["url"]
        self.mundialitis_login = credentials["login"]
        self.mundialitis_password = credentials["password"]

    def login(self):
        """
        Login to Mundialitis with Bitwarden credentials.
        """
        try:
            self.browser.go_to(self.mundialitis_url)
            self.input_credentials()
            self.submit_form()
        except Exception as e:
            capture_page_screenshot(OUTPUT_FOLDER, "Exception_Mundialitis_Login")
            raise Exception("Login to Mundialitis failed")


    def input_credentials(self):
        """
        Function that writes the credentials in the login form.
        """
        self.browser.click_element('//a[text()="LOGIN"]')
        self.browser.input_text_when_element_is_visible('//input[@id="logusername"]', self.mundialitis_login)
        self.browser.input_text_when_element_is_visible('//input[@id="logpassword"]', self.mundialitis_password)
        return

    def submit_form(self):
        """
        Function that submits the login form and waits for the main page to load.
        """
        self.browser.click_element('//button[@name="login"]')
        act_on_element('//div[@id="main"]', "find_element")
        return

    def register_new_user(self):
        """
        Function that registers a new user.
        """
        new_user = "RPATRAINING2"
        self.browser.go_to(self.mundialitis_url)
        self.browser.input_text_when_element_is_visible('//input[@id="rusername"]', new_user)
        self.browser.input_text_when_element_is_visible('//input[@id="rpassword"]', new_user)
        self.browser.input_text_when_element_is_visible('//input[@id="rpassword2"]', new_user)
        act_on_element('//button[@name="register" and @type="submit"]', "click_element")
        self.browser.input_text_when_element_is_visible('//input[@id="rfirstname"]', "RPA2")
        self.browser.input_text_when_element_is_visible('//input[@id="rlastname"]', "TRAINING2")
        self.browser.input_text_when_element_is_visible('//input[@id="remail"]', "rpa2@training.com")
        self.browser.input_text_when_element_is_visible('//input[@id="raddress"]', "RPA TRAINING ADDRESS 2")
        act_on_element('//select[@id="rcountry"]', "click_element")
        act_on_element('//select[@id="rcountry"]/option[@value="Perú"]', "click_element")
        self.browser.input_text_when_element_is_visible('//input[@id="rmoney"]', "1500")
        act_on_element('//button[@name="cmpregister" and @type="submit"]', "click_element")
        act_on_element('//div[@id="main"]', "find_element")
        


