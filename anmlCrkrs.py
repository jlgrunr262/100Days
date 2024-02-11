def animal_crackers(text):
   
    text.lower()
    initial = text.split()
    first = initial[0][0]
    second = initial[1][0]
    if first == second:
        print(True)
    else:
        print(False)

animal_crackers('Llama Level')
animal_crackers('Crazy Kangaroo')