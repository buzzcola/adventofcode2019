(lower, upper) = (245318, 765747)

def get_digits(n):
    result = []
    while n:
        result.insert(0, n % 10)
        n //= 10
    return result

def never_decreases(digits):
    return all([digits[i] >= digits[i-1] for i in range(1, len(digits))])

def has_strict_pair(digits):
    return any(
        digits[i] == digits[i-1]
        and (i == 1 or digits[i-2] != digits[i])        
        and (i == 5 or digits[i+1] != digits[i])
        for i in range(1, len(digits)))

passwords = []
for number in range(lower, upper):
    digits = get_digits(number)
    if has_strict_pair(digits) and never_decreases(digits):
        passwords.append(number)

print(len(passwords))