def get_num_words(text:str):
    array_words = text.split()
    return len(array_words)

def get_num_letters(text:str):
    rtn = {}
    for char in text:
        char = char.lower()

        if rtn.get(char) == None:
            rtn[char] = 1
        else:
            rtn[char] = rtn.get(char) + 1
    
    return rtn

def sort_on(items):
    return items["num"]

def dict_to_list(items:dict):
    # return [{"char": k, "num": v} for k, v in items.items()]

    a_list = []
    for k,v in items.items():
        a_dict = {"char": k, "num": v}
        a_list.append(a_dict)

    a_list.sort(reverse=True, key=sort_on)

    for item in a_list:
        msg = f'{item["char"]}: {item["num"]}'
        print(msg)