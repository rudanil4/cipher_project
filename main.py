from ceaser import CeaserEncrypting, CeaserDecrypting, CeaserHack
from visioner import VisionerEncrypting, VisionerDecrypting
from vernam import VernamEncrypting, VernamDecrypting

def function_call():
    print("Введите путь к исходному файлу")
    path = str(input())
    print("Введите название результата")
    path_out = str(input())
    print('Если хотите зашифровать текст введите: encrypt, если хотите расшифровать текст введите: decrypt')
    answer = str(input())
    correct_answer = True
    if answer == 'encrypt':
        print('Выберите предпочитаемый метод шифрования: ceaser, visioner, vernam')
        answer = str(input())
        if answer == 'ceaser':
            print("Введити сдвиг")
            shift = int(input())
            CeaserEncrypting(path, shift, path_out)
        elif answer == 'visioner':
            print("Введити ключ")
            key = input()
            VisionerEncrypting(path, key, path_out)
        elif answer == 'vernam':
            print("Введите название файла, куда будет помещен ключ")
            path_key = input()
            VernamEncrypting(path, path_out, path_key)
        else:
            correct_answer = False
    elif answer == 'decrypt':
        print('Выберите метод шифрования: ceaser, visioner, vernam')
        answer = str(input())
        if answer == 'ceaser':
            print('Расшифровать или взломать: 1 или 2')
            answer = int(input())
            if answer == 1:
                print("Введити ключ")
                shift = int(input())
                CeaserDecrypting(path, shift, path_out)
            if answer == 2:
                CeaserHack(path, path_out)
        elif answer == 'visioner':
            print("Введити ключ")
            key = input()
            VisionerDecrypting(path, key, path_out)
        elif answer == 'vernam':
            print('Введите путь по которому находится ключ')
            path_key = input()
            VernamDecrypting(path, path_out, path_key)
        else:
            correct_answer = False
    else:
        correct_answer = False
    if not correct_answer:
        print('Неправильная команда, пожалуйста начните с начала')
        function_call()


function_call()

