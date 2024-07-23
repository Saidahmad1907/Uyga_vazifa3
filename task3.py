class RepeatString:
    def __init__(self, input_string):
        self.input_string = input_string
    def repeat_words(self):
        words = self.input_string.split()
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                
                word_count[word] = 1
        repeated_words = [word for word, count in word_count.items() if count > 1]
        
        return repeated_words

S = "python java python php python c++ javascript python"
repeat_string_instance = RepeatString(S)
print(repeat_string_instance.repeat_words())

