from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
	def should_be_base_page(self):
		self.should_be_empty_massage()
		self.should_be_empty()

	def should_be_empty_massage(self):
		buy_link = self.browser.find_element(*BasketPageLocators.MASSAGE_EMPTY)
		buy_link_atr = buy_link.get_attribute('href')
		if "voucher" not in buy_link_atr:
			assert True
		else:
			assert False, "No link for empty basket"

	def should_be_empty(self):
		assert self.is_not_element_present(*BasketPageLocators.ITEMS_FORM), \
		"Basket is not empty, but should be"
