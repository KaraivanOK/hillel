from prettytable import PrettyTable # подключаем библиотеку pretty table через Settings-Python Interpreter
x = PrettyTable()
x.add_column("КОД", [r'\a', r'\b', r'\n', r'\t', r'\\',  r'\"', r"\'"]) # Первая колонка  с шапкой и данными.
x.add_column("Описание", ['Bell (alert)', 'Backspace', 'New line', 'Horizontal tab', "Backslah \\",
'Double quotation mark \"', " Single quotation mark \'"]) #Вторая колонка с шапукой и данными.
print(x)  # Печатаем таблицу