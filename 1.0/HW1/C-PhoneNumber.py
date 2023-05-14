def number_resolve(number: str):
    result = number.replace('-', '').replace('(', '').replace(')', '')
    if result.startswith("+7"):
        return result[2:]
    elif result.startswith("8"):
        return result[1:]
    else:
        return "495" + result


new_num = input()
all_nums = [input() for _ in range(3)]
print('\n'.join("YES" if number_resolve(new_num) == number_resolve(num) else "NO" for num in all_nums))
