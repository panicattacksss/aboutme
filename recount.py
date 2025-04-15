import re

input_file = "index.html"
output_file = "index_converted.html"

# Читаем HTML
with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# Функция перевода px в %
def px_to_percent(match):
    px_value = int(match.group(1))
    prop = match.group(2)  # Свойство (width, height и т.д.)

    if prop in ["width", "left", "right", "margin", "padding"]:
        base = 1920  # Относительно ширины экрана
    elif prop in ["height", "top", "bottom"]:
        base = 1080  # Относительно высоты экрана
    else:
        return match.group(0)  # Не менять

    percent_value = round((px_value / base) * 100, 2)
    return f"{prop}: {percent_value}%"

# Регулярка для поиска `width: 100px;`, `margin: 50px;` и т.д.
pattern = re.compile(r"(\b(?:width|height|margin|padding|top|left|right|bottom)\b):\s*(\d+)px")

# Заменяем пиксели на проценты
new_content = pattern.sub(px_to_percent, content)

# Записываем результат в новый файл
with open(output_file, "w", encoding="utf-8") as file:
    file.write(new_content)

print(f"Файл с изменениями сохранен как {output_file}")
