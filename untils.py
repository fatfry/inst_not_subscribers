import time

from consts import DEFAULT_TIME_SLEEP, AMOUNT_OF_UNFOLLOW, FOLLOW_BUTTON_CSS_SELECTOR, UNFOLLOW_BUTTON_CSS_SELECTOR
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def waiting_for_load_page(logging, sec=DEFAULT_TIME_SLEEP):
    logging.info(f'Ожидание загрузки страницы {sec} секунд')
    time.sleep(sec)


def login_to_inst(driver, username, password, logging):
    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys(username)
    logging.info('Введен логин')

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)
    logging.info('Введен пароль')

    # Нажатие кнопки входа
    password_input.send_keys(Keys.ENTER)
    logging.info('Нажата кнопка входа')
    waiting_for_load_page(logging)


def open_profile(driver, logging, profile_url):
    logging.info('Страница загружена')
    logging.info('Открытие профиля')
    driver.get(profile_url)
    waiting_for_load_page(logging)


def click_followers_button(driver, logging):
    followers_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'подписчиков')
    logging.info('Найдена кнопка подписчиков')
    followers_button.click()
    waiting_for_load_page(logging)


def loop_unfollow(driver, logging):
    logging.info('Запускаем цикл по отписке')
    for _ in range(AMOUNT_OF_UNFOLLOW):
        logging.info('Ищем кнопку подписки')
        follow_button = driver.find_element(By.XPATH, FOLLOW_BUTTON_CSS_SELECTOR)
        logging.info('Найдена кнопка подписки - кликаем')
        time.sleep(2)
        follow_button.click()
        waiting_for_load_page(logging)

        logging.info('Ищем кнопку отписки')
        unfollow_button = driver.find_element(By.CSS_SELECTOR, UNFOLLOW_BUTTON_CSS_SELECTOR)
        logging.info('Найдена кнопка отписки - кликаем')
        time.sleep(2)
        unfollow_button.click()
        waiting_for_load_page(logging)


def click_followers_window_to_close(driver, logging):
    button = driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Закрыть']")
    logging.info('Найдена кнопка закрытия окна подписчиков')
    button.click()
    logging.info('Клик по кнопке закрытия окна подписчиков')
    waiting_for_load_page(logging)

