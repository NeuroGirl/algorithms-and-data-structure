output_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab1/task10/txtf/output.txt", 'w')

def polyndrome(num_len, list_to_poly):
    if num_len == len(set(list_to_poly)):
        return sorted(list(list_to_poly))[0]
    else:
        n_let = dict()
        c_let = ''
        list_set = list(set(list_to_poly))

        for letter in sorted(list_set):
            if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                cnt = list_to_poly.count(letter)
                if cnt % 2 == 0:
                    c_let += letter * (cnt // 2)
                else:
                    n_let[letter] = cnt
            else:
                print("В введенной строке должны быть только заглавные латинские буквы")
                exit()

        result = list()
        if len(n_let) != 0:
            for letter in n_let:
                res = c_let + letter * n_let[letter] + c_let[::-1]
                if result:
                    if len(res) > len(result[0]):
                        result = list()
                    elif len(res) < len(result[0]):
                        continue
                result.append(res)
            return min(result)
        return c_let + c_let[::-1]




input_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab1/task10/txtf/input.txt")
num_len = int(input_f.readline())
file = input_f.readline()
if 1 <= num_len <= 10 ** 6:
    letters = list(file)
    result = polyndrome(num_len, letters)
    output_f.write(result)
else:
    print('Неверное количество введенных символов')

output_f.close()
input_f.close()