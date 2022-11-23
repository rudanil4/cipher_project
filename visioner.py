combined_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ' \
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:-!?_;\"'
alphabet_length = len(combined_alphabet)


def VisionerEncrypting(path_in, key, path_out):
    with open(path_in, encoding='UTF8') as file, open(path_out, mode='w', encoding='UTF8') as out:
        key_count = 0
        for line in file:
            for symbol in line:
                shift = combined_alphabet.index(key[key_count % len(key)])
                if symbol == '\n':
                    out.write('\n')
                elif symbol in combined_alphabet:
                    idx = combined_alphabet.index(symbol)
                    out.write(combined_alphabet[(idx + shift) % alphabet_length])
                    key_count += 1


def VisionerDecrypting(path_in, key, path_out):
    with open(path_in, encoding='UTF8') as file, open(path_out, mode='w', encoding='UTF8') as out:
        key_count = 0
        for line in file:
            for symbol in line:
                shift = combined_alphabet.index(key[key_count % len(key)])
                if symbol == '\n':
                    out.write('\n')
                elif symbol in combined_alphabet:
                    idx = combined_alphabet.index(symbol)
                    out.write(combined_alphabet[(idx - shift) % alphabet_length])
                    key_count += 1

