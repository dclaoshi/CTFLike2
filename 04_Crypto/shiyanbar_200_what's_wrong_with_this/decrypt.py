
SECRET = 'w*0;CNU[\\gwPWk}3:PWk"#&:ABu/:Hi,M'
def decrypt_string(s): 
    new_str = []
    for (index , c) in enumerate(s): 
        if index == 0:
            new_str.append(rot_chr(c, 10))
            continue
        new_str.append(rot_chr(c, ord(s[index - 1]))) 
    return ''.join(new_str)

def rot_chr(c, amount):
    return chr(((ord(c) - 33) - amount) % 94 + 33)

print decrypt_string(SECRET)