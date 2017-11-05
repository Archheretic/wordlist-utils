# -*- coding: utf-8 -*-
#
# Python2
#
# For a password to be valid it needs to contain minimum 8 characters and minimum: One uppercase, one lowercase and
# one number.
# The goal of this program is to turn any potential password into a working password.


from enum import Enum

inn = open("unvalidatedList.txt", "r")
out = open("validateList.txt", "w+")
MIN_PWD_LENGTH = 8


class PasswordValidity(Enum):
    Valid = 1
    OnlyDigits = 2
    OnlyLowerCase = 3
    OnlyUpperCase = 4
    MissingDigits = 5
    MissingLowerCase = 6
    MissingUpperCase = 7
#    TooShortButMissingDigits = 8
#    TooShortButAndGotDigits = 9


# This function returns a PasswordValidity enum
def password_validity(password):
    has_digits = False
    has_upper_case = False
    has_lower_case = False

    for char in password:
        if char.islower():
            has_lower_case = True
        elif char.isdigit():
            has_digits = True
        elif char.isupper():
            has_upper_case = True

    if has_digits and has_upper_case and has_lower_case:
        return PasswordValidity.Valid

    elif has_upper_case and has_lower_case and (not has_digits):
        return PasswordValidity.MissingDigits

    elif has_digits and has_lower_case and (not has_upper_case):
        return PasswordValidity.MissingUpperCase

    elif has_upper_case and has_digits and (not has_lower_case):
        return PasswordValidity.MissingLowerCase

    elif has_digits and (not has_upper_case) and (not has_lower_case):
        return PasswordValidity.OnlyDigits

    elif has_lower_case and (not has_upper_case) and (not has_digits):
        return PasswordValidity.OnlyLowerCase

    elif has_upper_case and (not has_lower_case) and (not has_digits):
        return PasswordValidity.OnlyUpperCase


def add_digits(password):
    # very messy code
    for i in range(0, 10):
        pwd = password + str(i)
        if len(pwd) >= MIN_PWD_LENGTH:
            write_to_file(pwd)
        for j in range(0, 10):
            pwd = password + str(i) + str(j)
            if len(pwd) >= MIN_PWD_LENGTH:
                write_to_file(pwd)
            for k in range(0, 10):
                pwd = password + str(i) + str(j) + str(k)
                if len(pwd) >= MIN_PWD_LENGTH:
                    write_to_file(pwd)
                for l in range(0, 10):
                    pwd = password + str(i) + str(j) + str(k) + str(l)
                    if len(pwd) >= MIN_PWD_LENGTH:
                        write_to_file(pwd)


def turn_one_char_to_lower(string):
    alpha_count = 0
    lowered = False
    new_str = []
    for x in xrange(0, len(string)):
        if string[x].isalpha() and x > 0 and not lowered:
            new_str.append(string[x].lower())
            alpha_count += 1
            lowered = True
        elif string[x].isalpha():
            alpha_count += 1
            new_str.append(string[x])
        else:
            new_str.append(string[x])
    # string needs to include minimum 2 alpha letters or its useless as a password
    if lowered and alpha_count >= 2:
        return ''.join(new_str)

    return None


def turn_one_char_to_upper(string):
    alpha_count = 0
    upped = False
    new_str = []
    for x in xrange(0, len(string)):
        if string[x].isalpha() and not upped:
            new_str.append(string[x].upper())
            upped = True
            alpha_count += 1
        elif string[x].isalpha():
            alpha_count += 1
            new_str.append(string[x])
        else:
            new_str.append(string[x])
    # string needs to include minimum 2 alpha letters or its useless as a password
    if upped and alpha_count >= 2:
        return ''.join(new_str)

    return None


def write_to_file(string):
    string = string.encode('utf-8')
    out.write(string + '\n')

# The programs entry point:
while True:
    line = inn.readline()
    if not line: break
    line = line.decode('utf-8')
    # removes \n
    line = line.rstrip()

    validity = password_validity(line)

    # This if check should not let short password get into the wordlist,
    # if its missing digits then we will allow the iteration to continue so that we can
    # add digits until the password is long enough to be valid.
    if (len(line) < MIN_PWD_LENGTH and ((validity is not PasswordValidity.MissingDigits) and
                                        (validity is not PasswordValidity.OnlyLowerCase) and
                                        (validity is not PasswordValidity.OnlyUpperCase))):
        continue

    if validity == PasswordValidity.Valid:
        write_to_file(line)

    # We don't want to use digits only passwords at all at this stage
    # elif validity == PasswordValidity.OnlyDigits:

    elif validity == PasswordValidity.OnlyLowerCase:
        line = line[0].upper() + line[1:]
        add_digits(line)

    elif validity == PasswordValidity.OnlyUpperCase:
        line = line[0:len(line)-1] + line[len(line)-1].lower()
        add_digits(line)

    elif validity == PasswordValidity.MissingDigits:
        add_digits(line)

    elif validity == PasswordValidity.MissingLowerCase:
        new_pwd = turn_one_char_to_lower(line)
        if new_pwd is not None:
            write_to_file(new_pwd)

    elif validity == PasswordValidity.MissingUpperCase:
        new_pwd = turn_one_char_to_upper(line)
        if new_pwd is not None:
            write_to_file(new_pwd)

