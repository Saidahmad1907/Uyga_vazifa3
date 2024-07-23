class Sort:
    @staticmethod
    def sort_dict(input_dict):
        assert isinstance(input_dict, dict), "Input dict bo'lishi kerak"
        
        three_digit_numbers = [
            value for value in input_dict.values() 
            if isinstance(value, int) and 100 <= value <= 999
        ]
        
        return three_digit_numbers

example_dict = {
    'a': 123,
    'b': 45,
    'c': 678,
    'd': 910,
    'e': 345,
    'f': 'not a number',
    'g': 256
}

print(Sort.sort_dict(example_dict))

