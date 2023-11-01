list = {
    'ID': 13, 
    'name': 'Ivan',
    'surname': 'Lasitsa',
    'group': 'ІПЗс-23-2',
    'course': 1,
    'books': [],
    'statistic': []
}

while True:
    print("Меню:")
    print("1 - Показати карту читача")
    print("2 - Взяти книгу")
    print("3 - Повернути книгу")
    print("0 - Вихід")
    x = input("вбири ")
    match x:
        case "0":
            print("Програма завершена.")
            break
        case "1":
            print(list)
        case "2":
            book = input("Введіть назву книги, яку бажаєте взяти: ")
            list['books'].append(book)
            print(list)
        case "3":
            if list['books'] != []:
                print(list['books'])
                book = input("Введіть назву книги, яку бажаєте повернути: ")
                list['books'].remove(book)
                list['statistic'].append(book)
                print(list)
            else:
                print("У вас немає книг у боргу.")
                
        
        
        