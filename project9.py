class IntegerToRoman:
    def __init__(self, number):
        self.number = number

    def convert(self):
        num = self.number

        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman = ""

        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman += syb[i]
                num -= val[i]
            i += 1

        return roman
    
number = int(input("Enter an integer: "))

obj = IntegerToRoman(number)

print("Roman numeral:", obj.convert())