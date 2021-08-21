from prettytable import PrettyTable  # подключаем библиотеку pretty table через Settings-Python Interpreter

x = PrettyTable()
# Первая колонка  с шапкой и данными.
x.add_column("КОД", [r'\a', r'\b', r'\n', r'\t', r'\\', r'\"', r"\'"])
# Вторая колонка с шапкой и данными.
x.add_column("Описание", ['Bell (alert)', 'Backspace', 'New line', 'Horizontal tab', "Backslah \\",
                          'Double quotation mark \"',
                          " Single quotation mark \'"])
print(x)  # Печатаем таблицу
