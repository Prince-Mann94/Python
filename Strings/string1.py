# a = input("Enter your name : ")
# print(f"Good afternoon {a}")

letter = '''
            Dear <|Name|>,
            You are selected!
            <|Date|>
               '''

print(letter.replace("<|Name|>" , "Prince mann").replace("<|Date|>","Join on jan 4, 2026"))