def word_count(file_contents):
    split_content = file_contents.split()
    return split_content

def character_count(word_count):
    character_dict = {}
    for word in word_count.lower():
        if word not in character_dict:
            character_dict[word] = 1
        else:
            character_dict[word] += 1

    return character_dict
        
def sorted_dict_list(character_dict):
    sorted_list = []
    for char in character_dict:
        if char.isalpha() == True:
            char_dict = {"char": char, "num": character_dict[char]}
            sorted_list.append(char_dict)
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    #print (sorted_list)
    return sorted_list
