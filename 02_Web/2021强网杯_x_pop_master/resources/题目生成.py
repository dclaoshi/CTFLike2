import random
import sys
import re
import os

sys.setrecursionlimit(1000000)

def get_random_str(randomlength=16):
    random_str = ''
    base_str1 = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz'
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length1 = len(base_str1) - 1
    length = len(base_str) - 1
    random_str = base_str1[random.randint(0, length1)]
    for i in range(randomlength-1):
        random_str += base_str[random.randint(0, length)]
    return random_str

def nothing_stmts(arg):
    stmts = [
        "\t\t$this->" + get_random_str(5) + ' = "' +get_random_str(5) + "\";\n",
        "\t\tif(" + str(random.randint(0,65535)) + ">" + str(random.randint(0,65535)) + "){\n\t\t\t$" + arg + " = $" + arg + ".'" + get_random_str(5) +"';\n\t\t}\n",
        "\t\tfor($i = 0; $i < " +str(random.randint(0,40))+ "; $i ++){\n\t\t\t$a" + get_random_str(5) + "= $" + arg + ";\n\t\t}\n"
    ]
    return random.choice(stmts)

def clean_stmts(arg):
    #print(arg)
    stmts = [
        "\t\tfor($i = 0; $i < " +str(random.randint(0,40))+ "; $i ++){\n\t\t\t$" + arg + "= $" + get_random_str(5) + ";\n\t\t}\n",
        "\t\t$" + arg + "='" + get_random_str(5) + "';\n"
    ]
    return random.choice(stmts)


class_list = set()
method_list = dict()
class_method = dict()

i = 0
while 1:
    if len(class_list) >= 10000 and len(method_list) >= 20000:
        break
    class_name = get_random_str(6)
    class_list.add(class_name)
    method_1 = get_random_str(6)
    method_2 = get_random_str(6)
    method_list[method_1] = class_name
    method_list[method_2] = class_name
    class_method[class_name] = [method_1, method_2]

func_map = dict()
method_list_keys = list(method_list.keys())

array = []
array2 = []

key = random.sample(method_list_keys, 1)[0]
method_list_keys.remove(key)
array.append(key)
start_func = key


for i in range(9990):
    func = array.pop(0)
    key1 = random.sample(method_list_keys, 1)[0]
    method_list_keys.remove(key1)
    if random.randint(0,1):
        key2 = random.sample(method_list_keys, 1)[0]
        method_list_keys.remove(key2)
        func_map[func] = [key1,key2]
        array.append(key1)
        array.append(key2)
    else:
        func_map[func] = [key1]
        array.append(key1)


muban = """
class {class_name}{{
    public ${var_name};
    public function {func_name1}(${random1}){{
{func_name1}_other{func_name1_call1}{func_name1_call2}
    }}
    public function {func_name2}(${random2}){{
{func_name2}_other{func_name2_call1}{func_name2_call2}
    }}
}}
"""

strs = dict()
method_args = dict()
class_var = dict()

for i in class_method.keys():
    methods = class_method[i]
    class_name = i
    var_name = get_random_str(7)
    class_var[class_name] = var_name
    random1 = get_random_str(5)
    random2 = get_random_str(5)
    func_name1 = methods[0]
    func_name2 = methods[1]
    temp_flag = 0  #用来临时标记，删除_other语句使用
    if not func_map.get(func_name1):
        func_name1_call1 = "\t\teval($" + random1 + ");\n"
        func_name1_call2 = ""
        temp_flag += 1
    elif len(func_map.get(func_name1)) == 1:
        func_name1_call1 = "\t\t$this->" + var_name + "->" + func_map[func_name1][0] + "($" + random1 +");\n"
        func_name1_call2 = ""
    elif len(func_map.get(func_name1)) == 2:
        func_name1_call1 = "\t\tif(method_exists($this->" + var_name + ", '" + func_map[func_name1][0] + "')) $this->" + var_name + "->" + func_map[func_name1][0] + "($" + random1 +");\n"
        func_name1_call2 = "\t\tif(method_exists($this->" + var_name + ", '" + func_map[func_name1][1] + "')) $this->" + var_name + "->" + func_map[func_name1][1] + "($" + random1 +");\n"
    else:
        func_name1_call1 = "\t\teval($" + random1 + ");\n"
        func_name1_call2 = ""
        temp_flag += 1

    if not func_map.get(func_name2):
        func_name2_call1 = "\t\teval($" + random2 + ");\n"
        func_name2_call2 = ""
        temp_flag += 2
    elif len(func_map.get(func_name2)) == 1:
        func_name2_call1 = "\t\t$this->" + var_name + "->" + func_map[func_name2][0] + "($" + random2 +");\n"
        func_name2_call2 = ""
    elif len(func_map.get(func_name2)) == 2:
        func_name2_call1 = "\t\tif(method_exists($this->" + var_name + ", '" + func_map[func_name2][0] + "')) $this->" + var_name + "->" + func_map[func_name2][0] + "($" + random2 +");\n"
        func_name2_call2 = "\t\tif(method_exists($this->" + var_name + ", '" + func_map[func_name2][1] + "')) $this->" + var_name + "->" + func_map[func_name2][1] + "($" + random2 +");\n"
    else:
        func_name1_call1 = "\t\teval($" + random1 + ");\n"
        func_name1_call2 = ""
        temp_flag += 2

    muban2 = muban.format(class_name=class_name, var_name=var_name, random1=random1, random2=random2, func_name1=func_name1, func_name2=func_name2, func_name1_call1=func_name1_call1, func_name1_call2=func_name1_call2, func_name2_call1=func_name2_call1, func_name2_call2=func_name2_call2)
    """
    if temp_flag == 1:
        muban2 = muban2.replace(func_name1 + "_other", "")
    elif temp_flag == 2:
        muban2 = muban2.replace(func_name2 + "_other", "")
    elif temp_flag == 3:
        muban2 = muban2.replace(func_name1 + "_other", "").replace(func_name2 + "_other", "")
    """
    strs[class_name] = muban2
    method_args[func_name1] = random1
    method_args[func_name2] = random2

flag = 0
flag2 = 0 #用来留后门
flag3 = 0
i = 0
result_list = []
result_list2 = []

def dfs(method):
    global func_map, flag, strs, method_list, flag2, flag3, i, result_list, result_list2
    i += 1
    result_list.append(method)
    class_name = method_list[method]
    if i >= 1000 and flag3 == 0 and flag == 0:
        flag2 = 1
        flag3 = 1
    if not func_map.get(method):
        if flag2 == 1:
            strs[class_name] = strs[class_name].replace(method + "_other", nothing_stmts(method_args[method]))
            result_list2 = result_list.copy()
            flag2 = 0
        elif flag == 0:
            strs[class_name] = strs[class_name].replace(method + "_other", clean_stmts(method_args[method]))
        else :
            strs[class_name] = strs[class_name].replace(method + "_other", nothing_stmts(method_args[method]))
        #print(i)
        result_list.pop()
        return
    if len(func_map[method]) == 1:
        if flag2 == 1:
            strs[class_name] = strs[class_name].replace(method + "_other", nothing_stmts(method_args[method]))
            dfs(func_map[method][0])
        elif flag == 1:
            strs[class_name] = strs[class_name].replace(method + "_other", nothing_stmts(method_args[method]))
            dfs(func_map[method][0])
        else:
            if random.randint(0, 15) == 14 and i > 40:
                flag = 1
                strs[class_name] = strs[class_name].replace(method + "_other", clean_stmts(method_args[method]))
                dfs(func_map[method][0])
                flag = 0
            else:
                strs[class_name] = strs[class_name].replace(method + "_other", nothing_stmts(method_args[method]))
                dfs(func_map[method][0])

    elif len(func_map[method]) == 2:
        if flag2 == 1:
            strs[class_name] = strs[class_name].replace(method + "_other", nothing_stmts(method_args[method]))
            dfs(func_map[method][0])
            dfs(func_map[method][1])
        elif flag == 1:
            strs[class_name] = strs[class_name].replace(method + "_other", nothing_stmts(method_args[method]))
            dfs(func_map[method][0])
            dfs(func_map[method][1])
        else:
            if random.randint(0, 15) == 14  and i > 40:
                flag = 1
                strs[class_name] = strs[class_name].replace(method + "_other", clean_stmts(method_args[method]))
                dfs(func_map[method][0])
                dfs(func_map[method][1])
                flag = 0
            else:
                strs[class_name] = strs[class_name].replace(method + "_other", nothing_stmts(method_args[method]))
                dfs(func_map[method][0])
                dfs(func_map[method][1])
    result_list.pop()

dfs(start_func)

with open(r"/root/class.php" ,"w+") as f:
    f.write("<?php\n")
    for class_name in strs.keys():
        string = strs[class_name]
        if "_other" in string:
            string = re.sub(".{6}_other", "", string)
        f.write(string + "\n")


pop = "*****"
for func in result_list2:
    pop = pop.replace("*****", 'O:6:"' + method_list[func] + '":1:{s:7:"' + class_var[method_list[func]] + '";*****}')
pop = pop.replace("*****", "N;")

index_muban = """
<?php
include "class.php";
//class.php.txt
highlight_file(__FILE__);
$a = $_GET['pop'];
$b = $_GET['argv'];
$class = unserialize($a);
$class->{start_func}($b);
"""
index_content = index_muban.format(start_func=start_func)

with open(r"/root/index.php" ,"w+") as f:
    f.write(index_content)

with open("/root/pop", "w") as f:
    f.write(pop)