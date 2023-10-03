from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
	def add_book_to_card(self):
		assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "add to card button is not presented"
		add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
		add_button.click()

	def should_be_right_massages(self):
		self.should_be_right_book_name()
		self.should_be_right_book_price()

	def should_be_right_book_name(self):
		msg_book_name_elt = self.browser.find_element(*ProductPageLocators.MASSAGE_BOOK_NAME)
		site_book_name_elt = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
		assert msg_book_name_elt.text == site_book_name_elt.text, "Incorrect book name in the massage"

	def should_be_right_book_price(self):
		msg_book_price_elt = self.browser.find_element(*ProductPageLocators.MASSAGE_BOOK_PRICE)
		site_book_price_elt = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
		assert msg_book_price_elt.text == site_book_price_elt.text, "Incorrect book price in the massage"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
		"Success message is presented, but should not be"

	def success_message_should_disappear(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
		"Success message should disappear, but should not be"
