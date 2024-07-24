def intinput(prompt):
    while True:
        raw = input(prompt)
        try:
            return int(raw)
        except ValueError:
            print("Please enter a number")