import random
import string
import json


def get_n(p, q):
    return p * q


def get_phi_of_n(p, q):
    return (p - 1) * (q - 1)


def generate_prime_numbers():
    prime_list = []
    for n in range(2, 250):
        is_prime = True

        for num in range(2, n):
            if n % num == 0:
                is_prime = False

        if is_prime:
            prime_list.append(n)

    return prime_list


def get_p_q():
    prime_list = generate_prime_numbers()
    p = random.choice(prime_list)
    q = p
    while p == q:
        q = random.choice(prime_list)

    return p, q


def get_gcd(x, y):  # greatest common divisor
    while y:
        x, y = y, x % y
    return x


def get_encryption_key(n, phi_of_n):
    lst = [i for i in range(1, n + 1)]
    e_list = []
    for i in lst:
        if (1 < i) and (i < phi_of_n):
            gcd = get_gcd(i, n)
            gcd_phi = get_gcd(i, phi_of_n)
            if (gcd == 1) and (gcd_phi == 1):
                e_list.append(i)
    if len(e_list) == 1:
        return e_list[0]
    else:
        return e_list[random.randint(1, len(e_list) - 1)]


def get_decryption_key(e, phi_of_n):
    d_list = []
    for i in range(e * 25):
        if (e * i) % phi_of_n == 1:
            d_list.append(i)
    return d_list[random.randint(1, len(d_list) - 1)]


def text_to_digits(text):
    pool = string.ascii_letters + string.punctuation + string.digits
    text_as_digits = []
    for i in text:
        text_as_digits.append(pool.index(i))
    return text_as_digits


def encrypt(text):
    text_as_digits = text_to_digits(text)
    public_key = get_public_key()
    list = [(i ** public_key['e']) % public_key['n'] for i in text_as_digits]
    list = [str(x) for x in list]
    return "/".join(list)


def decrypt(cyphered):
    private_key = get_private_key()
    list = [int(x) for x in cyphered.split('/')]
    text_as_digits = [((i ** private_key['d']) % private_key['n']) for i in list]
    return digits_to_text(text_as_digits)


def digits_to_text(text_as_digits):
    pool = string.ascii_letters + string.punctuation + string.digits
    msg = ''
    for i in text_as_digits:
        msg += pool[i]
    return msg


def generate_keys():
    p, q = get_p_q()
    n = get_n(p, q)
    phi_func = get_phi_of_n(p, q)
    e = get_encryption_key(n, phi_func)
    d = get_decryption_key(e, phi_func)
    # to avoid key collision
    while d == e:
        d = get_decryption_key(e, phi_func)

    public_key = {'e': e, 'n': n}
    private_key = {'d': d, 'n': n}

    with open('util\\public_key.json', 'wt') as f:
        json.dump(public_key, f, indent=4)

    with open('util\\private_key.json', 'wt') as f:
        json.dump(private_key, f, indent=4)


def get_public_key():
    with open('util\\public_key.json', 'rt') as f:
        return json.load(f)


def get_private_key():
    with open('util\\private_key.json', 'rt') as f:
        return json.load(f)


if __name__ == '__main__':
    generate_keys()
