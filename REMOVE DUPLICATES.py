def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:

        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


values = input("Enter values:")
result = remove_duplicates(values)
print(result)
