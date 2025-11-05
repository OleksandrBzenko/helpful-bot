from datetime import datetime
'''
Додаток, який буде зберігати нотатки

This is my note, that I am taking on my laptop
- Created on 19.12.2024 20:15 ❤️

[("This is my note, that I am taking on my laptop", "19.12.2024 20:15")]
[("19.12.2024 20:15", "This is my note, that I am taking on my laptop")]

if note_data_one[1] > note_data_one[1]:
    ...

if note_data_one["creation_date"] > note_data_one["creation_date"]:
    ...

{"text": "This is my note, that I am taking on my laptop", "creation_date": "19.12.2024 20:15"}
{"creation_date": "19.12.2024 20:15", "text": "This is my note, that I am taking on my laptop"}

1) Створити словник нотаток та записати в нього інформацію
2) Написати функцію, яка буде виводити нотатку
3) Написати функцію, яка буде виводити усі нотатки
4) Написати цикл, який буде отримувати інформацію від користувача та реагувати на неї

5) Пофіксити проблему, де в нас є глобальна змінна
6) Пофіксити випадок, коли ми не передаємо аргументи print_note

'''

note_list = []
note_file = 'note.txt'


welcome_baner = r''' __    __            __                                      _______               __     
/  |  /  |          /  |                                    /       \             /  |    
$$ |  $$ |  ______  $$ |  ______    ______    ______        $$$$$$$  |  ______   _$$ |_   
$$ |__$$ | /      \ $$ | /      \  /      \  /      \       $$ |__$$ | /      \ / $$   |  
$$    $$ |/$$$$$$  |$$ |/$$$$$$  |/$$$$$$  |/$$$$$$  |      $$    $$< /$$$$$$  |$$$$$$/   
$$$$$$$$ |$$    $$ |$$ |$$ |  $$ |$$    $$ |$$ |  $$/       $$$$$$$  |$$ |  $$ |  $$ | __ 
$$ |  $$ |$$$$$$$$/ $$ |$$ |__$$ |$$$$$$$$/ $$ |            $$ |__$$ |$$ \__$$ |  $$ |/  |
$$ |  $$ |$$       |$$ |$$    $$/ $$       |$$ |            $$    $$/ $$    $$/   $$  $$/ 
$$/   $$/  $$$$$$$/ $$/ $$$$$$$/   $$$$$$$/ $$/             $$$$$$$/   $$$$$$/     $$$$/  
                        $$ |                                                              
                        $$ |                                                              
                        $$/                                                               
'''
commands = '''
1) exit - to exit the application
2) add_note - to add a new note
3) print_note [i] - to print note number i
4) print_all - to print all notes 
5) help - to print this menu
'''


def add_new_note(note_text) -> bool:
    note_creation_date = datetime.today()
    note_list.append({"text": note_text, "creation_date": note_creation_date})
    return True

def print_note(index: int):
    note = note_list[index]
    formatted_creation_date = note["creation_date"].strftime("%d.%m.%Y %H:%M")
    print(f'{note["text"]}\n- {formatted_creation_date}\n')

def print_all_notes():
    for note_index in range(len(note_list)):
        print_note(note_index)


def save_notes_to_file():
    with open(note_file, 'w', encoding='utf-8') as file:
        for note in note_list:
            file.write(f"{note['text']};{note['creation_date'].strftime('%d.%m.%Y %H:%M')}\n")


def read_notes() -> list[dict]:
    note_list = []
    with open(note_file) as file:
        for line in file:
            text, date = line.strip().split(';', 1)
            creation_date = datetime.strptime(date, "%d.%m.%Y %H:%M")
            note_list.append({"text": text, "creation_date": creation_date})
    return note_list


def init():
    global note_list
    note_list = read_notes()


    print(welcome_baner)
    print("\nWelcome to the note application!\n")
    print(commands)
    print()


def main():
    while True:
        command, *args = input("Please enter your command (enter exit to stop):").strip().split(' ')
        if command == "exit":
            print("Goodbye!")
            save_notes_to_file()
            break
        elif command == "add_note":
            text = input("Please enter note text: ")
            if add_new_note(text):
                print("\nNote added successfully!\n")
            else:
                print("\nError while adding a note!\n")
        elif command == 'help':
            print(commands)
        elif command == 'print_note':
            index = int(args[0]) - 1
            if index < 0 or index > len(note_list):
                print("Please enter valied note number")
                continue 
            print_note(index)

init()
main()
# text = input("Please enter your note: ")
# add_new_note(text, "19.12.2024 20:15")
# add_new_note(text, "19.12.2024 20:15")
# add_new_note(text, "19.12.2024 20:15")
# add_new_note(text, "19.12.2024 20:15")
# print_all_notes()




