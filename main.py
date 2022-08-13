from random import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


class santosh:

    url = "http://www.tutorialsninja.com/demo/"
    driver = webdriver.Firefox()

    def open_web_page(self):

        self.driver.get(self.url)
        self.driver.maximize_window()

    
    def open_phones(self):

        self.open_web_page()

        time.sleep(1)
        
        """ Click on Phones from the status bar """
        phone_tab = self.driver.find_element(by=By.XPATH,value='//a[text()="Phones & PDAs"]')
        phone_tab.click()
        time.sleep(2)

        """ assertion to check phones page"""
        x = self.driver.title
        assert x == "Phones & PDAs"
        time.sleep(1)

        """ Clicking on the iphone product """
        iphone = self.driver.find_element(by=By.XPATH,value='//a[text()="iPhone"]')
        iphone.click()
        time.sleep(2)

        y = self.driver.title
        assert y == "Phone & PDAs"

        """ Click on the 1st pic of the product """
        first_pic = self.driver.find_element(by=By.XPATH,value='//ul[@class="thumbnails"]/li[1]')
        first_pic.click()
        time.sleep(2)

        """ Click on the next button of the product pic """
        next_pic_button = self.driver.find_element(by=By.XPATH,value='//button[@class="mfp-arrow mfp-arrow-right mfp-prevent-close"]')
        for i in range(0,5):
            next_pic_button.click()
            time.sleep(1)
        
        """ Taking a screenshot of the product """
        self.driver.save_screenshot('Screenshot_' + str(random.randint(0,100)) + '.png')
        time.sleep(2)

        """ close the product pic """
        close_pic = self.driver.find_element(by=By.XPATH,value='//button[@title="Close (Esc)"]')
        close_pic.click()
        time.sleep(2)

        """ Quantity change to 2 """
        quantity_phone = self.driver.find_element(by=By.ID,value='input-quantity')
        quantity_phone.click()
        quantity_phone.clear()
        time.sleep(2)

        quantity_phone.send_keys("2")
        time.sleep(2)

        """ Click on add to cart """
        add_to_cart = self.driver.find_element(by=By.ID,value='button-cart')
        add_to_cart.click()
        time.sleep(2)

    
    def open_laptops(self):

        time.sleep(1)

        """ Click on the Laptop Section from the top bar """
        laptop_bar = self.driver.find_element(by=By.XPATH,value='//a[text()="Laptops & Notebooks"]')
        
        """ Perform Hovering to all laptops """
        act = ActionChains(self.driver)
        act.move_to_element(laptop_bar).perform()

        show_laptop = self.driver.find_element(by=By.XPATH,value='//a[text()="Show All Laptops & Notebooks"]')
        show_laptop.click()
        time.sleep(2)

        """ Assertion laptop page title """
        x = self.driver.title
        assert x == "Laptops & Notebooks"
        time.sleep(1)

        """ Click on the HP Laptop Product """
        laptop_product = self.driver.find_element(by=By.XPATH,value='//a[text()="HP LP3065"]')
        laptop_product.click()
        time.sleep(2)

        add_to_cart = self.driver.find_element(by=By.ID,value='button-cart')
        
        """ Scroll the screen till add to chart option """
        add_to_cart.location_once_scrolled_into_view
        time.sleep(2)

        """ Clicking on the calender """
        calender_button = self.driver.find_element(by=By.XPATH,value='//i[@class="fa fa-calendar"]')
        calender_button.click()
        time.sleep(2)

        """ Clicking on the month and year """
        month_year = self.driver.find_element(by=By.XPATH,value='//th[@class="picker-switch"]')
        next_button_calender = self.driver.find_element(by=By.XPATH,value='//th[@class="next"]')

        while month_year.text != "December 2022":
            next_button_calender.click()

        time.sleep(2)

        """ Click on the date """
        calender_date = self.driver.find_element(by=By.XPATH,value='//td[text()="31"]')
        calender_date.click()
        time.sleep(2)

        """ Add to cart the product """
        add_to_cart.click()
        time.sleep(2)


    def click_on_cart(self):

        self.open_web_page()
        time.sleep(3)
        self.open_phones()
        time.sleep(3)
        self.open_laptops()

        time.sleep(1)

        """ Click on cart """
        cart = self.driver.find_element(by=By.ID,value='cart-total')
        cart.click()
        time.sleep(1)

        """ Click on CheckOut """
        check_out = self.driver.find_element(by=By.XPATH,value='//p[@class="text-right"]/a[2]')
        check_out.click()
        time.sleep(1)

        """ click on Guest login """
        guest_radio = self.driver.find_element(by=By.XPATH,value='//input[@value="guest"]')
        guest_radio.click()
        time.sleep(1)

        """Assertion for checkout page """
        y = self.driver.title
        assert y == "Checkout"
        time.sleep(1)

        """ continue at step 1 """
        continue_1 = self.driver.find_element(by=By.ID,value='button-account')
        continue_1.click()
        time.sleep(1)

        """ step 2 """

        first_name = self.driver.find_element(by=By.ID,value='input-payment-firstname')
        first_name.clear()
        time.sleep(1)
        first_name.send_keys("test first name")
        time.sleep(1)

        last_name = self.driver.find_element(by=By.ID,value='input-payment-lastname')
        last_name.clear()
        time.sleep(1)
        last_name.send_keys("test last name")
        time.sleep(1)

        e_mail = self.driver.find_element(by=By.ID,value='input-payment-email')
        e_mail.clear()
        time.sleep(1)
        e_mail.send_keys("test@test.com")
        time.sleep(1)

        telephone = self.driver.find_element(by=By.ID,value='input-payment-telephone')
        telephone.clear()
        time.sleep(1)
        telephone.send_keys("4598712364")
        time.sleep(1)

        address_1 = self.driver.find_element(by=By.ID,value='input-payment-address-1')
        address_1.clear()
        time.sleep(1)
        address_1.send_keys("address test")
        time.sleep(1)

        city = self.driver.find_element(by=By.ID,value='input-payment-city')
        city.clear()
        time.sleep(1)
        city.send_keys("vizag")
        time.sleep(1)

        post_code = self.driver.find_element(by=By.ID,value='input-payment-postcode')
        post_code.clear()
        time.sleep(1)
        post_code.send_keys("530004")
        time.sleep(1)

        country = self.driver.find_element(by=By.ID,value='input-payment-country')
        drop_down = Select(country)
        drop_down.select_by_visible_text("India")
        time.sleep(1)

        region_state = self.driver.find_element(by=By.ID,value='input-payment-zone')
        drop_down_1 = Select(region_state)
        drop_down_1.select_by_value('1476')
        time.sleep(1)

        continue_2 = self.driver.find_element(by=By.ID,value='button-guest')
        continue_2.click()
        time.sleep(1)

        """ Delivery method continue """
        continue_3 = self.driver.find_element(by=By.ID,value='button-shipping-method')
        continue_3.click()
        time.sleep(1)

        """ Payment method """
        check_box = self.driver.find_element(by=By.XPATH,value='//input[@name="agree"]')
        check_box.click()
        time.sleep(1)

        continue_4 = self.driver.find_element(by=By.ID,value='button-payment-method')
        continue_4.click()
        time.sleep(1)

        """ To print the price from the cart """
        final_price = self.driver.find_element(by=By.XPATH,value='//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')
        print("*"*50)
        print(final_price.text)
        print("*"*50)
        time.sleep(1)

        """ Confirm order """
        confirm_order = self.driver.find_element(by=By.ID,value='button-confirm')
        confirm_order.click()
        time.sleep(1)

        """ Print successful order """
        message_print = self.driver.find_element(by=By.XPATH,value='//div[@id="content"]/h1')
        print("*"*50)
        print(message_print.text)
        print("*"*50)
        time.sleep(1)

        """ Final continue to main page """
        continue_5 = self.driver.find_element(by=By.XPATH,value='//div[@class="pull-right"]')
        continue_5.click()


s = santosh()

s.open_phones()


