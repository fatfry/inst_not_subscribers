from bs4 import BeautifulSoup


def find_elements_with_classes(html_content):
    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Ищем все элементы span с заданными классами
    classes = ["_ap3a", "_aaco", "_aacw", "_aacx", "_aad7", "_aade"]
    elements = soup.find_all('span', class_=lambda x: x and all(item in x.split() for item in classes))

    # Извлекаем текстовое содержимое найденных элементов
    texts = [element.get_text() for element in elements]

    return texts


# Для тестирования функции, вам нужно передать ей HTML-контент страницы как строку.
# Пример:
html_content = '''
<html>
<body>
<span class="_ap3a _aaco _aacw _aacx _aad7 _aade" dir="auto">marilatierra</span>
<span class="_ap3a _aaco _aacw _aacx _aad7 _aade" dir="auto">anotherExample</span>
<span class="_ap3a _aaco _aacw _aacx _aad7 _aade" dir="auto">sunflow_bitch</span>
</body>
</html>
'''

with open('fixtures/following.html', 'r', encoding='utf-8') as file:
    html_data = file.read()
    print(find_elements_with_classes(html_data))