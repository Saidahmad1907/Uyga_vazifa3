class TupleSort:
    @staticmethod
    def sort_tuple(tuple1, tuple2):
        assert isinstance(tuple1, tuple) and isinstance(tuple2, tuple), "Inputlar tupple bo'lishi kerak"
        
        umumiy_elementlar = list(set(tuple1) & set(tuple2))
        
        return umumiy_elementlar

tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 6, 7, 8, 9)

print(TupleSort.sort_tuple(tuple1, tuple2))

