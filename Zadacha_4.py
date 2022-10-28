with open('RLE1.txt', 'r') as file:
    original_txt = file.readline()
    txt_compr = original_txt.split()

print(original_txt)

def file_cod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond

txt_compr = file_cod(original_txt)

with open('RLE2.txt', 'w') as file:
    file.write(f'{txt_compr}')
print(txt_compr)
