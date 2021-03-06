from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

time.sleep(5)
class Test2(unittest.TestCase):
    def setUp(self):
        #options = webdriver.ChromeOptions()
        options = webdriver.FirefoxOptions()
        #options.headless = True

        options.add_argument("--headless")
        #options.add_experimental_option('w3c', False)
        #options.headless = True
        #options.add_argument('--no-sandbox')
        #options.add_argument('--disable-dev-shm-usage')
        #options.add_experimental_option("useAutomationExtension", False)
        #options.add_argument('--disable-blink-features=AutomationControlled')
        #options.add_experimental_option('excludeSwitches', ['enable-automation'])


        # self.driver =webdriver.Chrome("C:\chromedriver\chromedriver.exe") I don't work on Windows anymore
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        #self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("http://127.0.0.1:8000")

    def testSimplePath(self):
        driver= self.driver
        x01 = driver.find_element_by_name("x01")
        input_a = driver.find_element_by_name("a_node")
        input_b = driver.find_element_by_name("b_node")
        input_a.send_keys("0")
        input_b.send_keys("1")
        x01.click()
        send = driver.find_element_by_name("submit")
        send.click()
        path = driver.find_element_by_id("pth")
        #print(path.text)
        self.assertEqual(path.text, "Путь: 0 1")
        driver.quit()

    def testNoPath(self):
        driver = self.driver
        input_a = driver.find_element_by_name("a_node")
        input_b = driver.find_element_by_name("b_node")
        input_a.send_keys("0")
        input_b.send_keys("5")
        send = driver.find_element_by_name("submit")
        send.click()
        path = driver.find_element_by_id("pth")
        self.assertEqual(path.text, "Путь: Пути нет")
        driver.quit()

    def testDefault(self):
        driver = self.driver
        input_a = driver.find_element_by_name("a_node")
        input_b = driver.find_element_by_name("b_node")
        path = driver.find_element_by_id("pth")
        self.assertEqual(input_a.text, "")
        self.assertEqual(input_b.text, "")
        self.assertEqual(path.text, "Путь:")
        driver.quit()

    def testFieldMissing(self):
        driver = self.driver
        input_a = driver.find_element_by_name("a_node")
        input_a.send_keys("0")
        send = driver.find_element_by_name("submit")
        send.click()
        path = driver.find_element_by_id("pth")
        self.assertEqual(path.text, "Путь:")
        driver.quit()