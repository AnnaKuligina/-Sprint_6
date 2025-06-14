import data
from pages.important_questions_pages import MainPage
from pages.scooter_order_pages import OrderPage
from helper.help import generate_data_comment
import allure
import pytest

class TestScooterOrder:
    @allure.title("Тест заказ самоката с верхней кнопки Заказать")
    @pytest.mark.parametrize('name, surname, address, metro_st, phone', data.Data.personal_info_1)
    def test_success_order_top_button(self, driver, name, surname, address, metro_st, phone):
        main_page = MainPage(driver)
        main_page.click_top_register_button()
        order_page = OrderPage(driver)
        order_page.input_personal_information(name, surname, address, metro_st, phone)
        order_page.click_on_button_next()
        data, comment = generate_data_comment()
        order_page.input_rent_info(data, comment)
        order_page.click_on_button_order()
        order_page.click_on_button_yes()
        order_page.click_on_button_see_status()
        text = order_page.get_text_check_order()
        assert text == 'Самокат на складе', "Заказ не оформлен"

    @allure.title("Тест заказ самоката с нижней кнопки Заказать")
    @pytest.mark.parametrize('name, surname, address, metro_st, phone', data.Data.personal_info_2)
    def test_success_order_mid_button(self, driver, name, surname, address, metro_st, phone):
        main_page = MainPage(driver)
        main_page.scroll_to_mid_register_button()
        main_page.click_mid_register_button()
        order_page = OrderPage(driver)
        order_page.input_personal_information(name, surname, address, metro_st, phone)
        order_page.click_on_button_next()
        data, comment = generate_data_comment()
        order_page.input_rent_info(data, comment)
        order_page.click_on_button_order()
        order_page.click_on_button_yes()
        order_page.click_on_button_see_status()
        text = order_page.get_text_check_order()
        assert text == 'Самокат на складе', "Заказ не оформлен"