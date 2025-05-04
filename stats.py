def get_num_words(book):
  return len(book.split())

def get_num_characters(book):
  character_dict = dict()

  for char in list(book):
    if char.lower() in character_dict:
      character_dict[char.lower()] += 1
    else:
      character_dict[char.lower()] = 1

  return character_dict

def get_sorted_char_count(character_dict):
  dict_list = []

  for char, count in character_dict.items():
    dict_list.append({'char': char, 'count': count})

  def sort_on(dict):
    return dict["count"]
  
  dict_list.sort(key=sort_on,reverse=True)

  return dict_list