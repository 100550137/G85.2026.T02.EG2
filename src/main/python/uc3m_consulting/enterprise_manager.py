"""Module """

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_cif(cif: str):
        """Validate CIF code."""
        letter = cif[0]
        control_caracter = ["J","A","B","C","D","E","F","G","H","I"]
        number = cif[1:8]
        add_even = int(number[1]) + int(number[3]) + int(number[5])
        add_odd = 0
        i = 0
        while i <= 6:
            odd = str(int(number[i]) * 2)
            if len(odd) == 2:
                odd = int(odd[0]) + int(odd[1])
            add_odd += int(odd)
            i += 2
        total_sum = str(add_even + add_odd)
        if total_sum[1] == "0":
            digit = 0
        else:
            digit = str(10 - int(total_sum[1]))
        if letter in ("A", "B", "E", "H") and (cif[8] != digit):
            return False
        if letter in ("K", "P", "Q", "S"):
            digit = control_caracter[int(digit)]
            if cif[8] != digit:
                return False
        return True
