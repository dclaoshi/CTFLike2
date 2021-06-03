
result = []
str = "jeihjiiklwjnk{ljj{kflghhj{ilk{k{kij{ihlgkfkhkwhhjgly"
for s in str:
    s_int = ord(s)
    if s_int > 100 and s_int <= 149:
        result.append(chr(s_int - 53))
    elif s_int <= 11:
        pass
    else:
        pass

result_str = "".join(result)
print result_str
