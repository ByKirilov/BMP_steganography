Стеганогрфия

Программа, позволяющая скрыть текстовый документ в изображении формата BMP, и извлечь его в будущем.

Использование:
-Сокрытие текста: python Combine.py
-Извлечение текста: python Extract.py

Пакетный режим:
-Сокрытие текста: python Steganography.py combine image_path text_path key bits_to_rewrite_count
-Извлечение текста: python Steganography.py extract image_path key bits_to_rewrite_count
-Вызов справки: python Steganography.py -h

Пример запуска:
-Сокрытие текста: python Steganography.py combine ./image.bmp ./text.txt password 2
-Извлечение текста: python Steganography.py extract ./image.bmp password 2
