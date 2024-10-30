from logic04 import Family

# Создаем экземпляр класса Family
my_family = Family(['Mother', 'Father', 'Brother', 'I'], [173, 178, 160, 182])

# Получаем и выводим высоту члена семьи 'Father'
father_height = my_family.get_member_height('Father')
print('Рост отца:', father_height)

# Вычисляем и выводим общую сумму всех высот в семье
total_height = my_family.get_total_height()
print('Общий рост семьи:', total_height)