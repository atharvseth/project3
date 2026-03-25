class Reverse:
    
    def __init__(self, s=""):
        self.s = s

    def reverse_words(self):
        words = self.s.split()              
        reversed_words = words[::-1]        
        return " ".join(reversed_words)

text = input("Enter a string: ")
obj = Reverse(text)


print("Reversed string:", obj.reverse_words())