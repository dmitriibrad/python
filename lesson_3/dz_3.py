names = "Иван", "Мария", "Петр", "Илья", "Сергей"
name_letter = []
letters = {}


def thesaurus(name_employ):
    def letter_function(name):
        return name.startswith(my_names)

    for i in name_employ:
        name_letter.append(name_employ[name_employ.index(i)][:1])
        my_names = name_employ[name_employ.index(i)][:1]
        name_staff_test = list(filter(letter_function, name_employ))
        letters[my_names] = name_staff_test
    return letters


print(thesaurus(names))
