# python3

def read_input():
    input_type = input().rstrip()
    pattern = ""
    text = ""
    if input_type == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == "F":
        file_name = "tests/06"
        with open(file_name) as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()

    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    q = 101  
    b = 256  
    len_pattern = len(pattern)
    len_text = len(text)
    pattern_hash = 0
    text_hash = 0
    occurrences = []

   
    for i in range(len_pattern):
        pattern_hash = (pattern_hash * b + ord(pattern[i])) % q
        text_hash = (text_hash * b + ord(text[i])) % q

    for i in range(len_text - len_pattern + 1):
        if pattern_hash == text_hash: 
            if text[i:i+len_pattern] == pattern:
                occurrences.append(i)

        if i < len_text - len_pattern:
            text_hash = ((text_hash - ord(text[i]) * pow(b, len_pattern - 1, q)) * b + ord(text[i + len_pattern])) % q

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))