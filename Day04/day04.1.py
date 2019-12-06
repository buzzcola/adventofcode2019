(lower, upper) = (245318, 765747)

def get_digits(n):
    result = []
    while n:
        result.insert(0, n % 10)
        n //= 10
    return result

def never_decreases(digits):
    return all([digits[i] >= digits[i-1] for i in range(1, len(digits))])

def has_duplicates(digits):
    return any(digits[i] == digits[i-1] for i in range(1, len(digits)))

passwords = []
for number in range(lower, upper):
    digits = get_digits(number)
    if has_duplicates(digits) and never_decreases(digits):
        passwords.append(number)

print(len(passwords))