def snake_to_pascal(string: str) -> str:
    string_array = string.split('_')
    result = []
    for word in string_array:
        result.append(word.capitalize())
    return ''.join(result)
