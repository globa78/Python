# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text_my = 'Напишитеабв программу, абвудаляющую из текста слабвова, содержащие "абв".'
text_my = list(filter(lambda x: 'абв' not in x, text_my.split()))
new_text = " ".join(text_my)
print(new_text)
