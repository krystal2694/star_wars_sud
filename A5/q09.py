# Krystal Wong
# A01089672
# Theoren Leveille
# A01070327
# 05/04/2019
import doctest


def base_conversion(original_base, original_number, destination_base):

    decimal_number = int(str(original_number), original_base)
    num_str = convert_to_base_n(decimal_number, destination_base)
    return num_str[::-1]


def convert_to_base_n(decimal_number, destination_base):

    quotient = decimal_number // destination_base
    remainder = decimal_number % destination_base

    if quotient == 0:
        return remainder
    else:
        return str(decimal_number % destination_base) + str(convert_to_base_n(quotient, destination_base))


def main():
    original_base = 5
    original_number = 13242
    destination_base = 9
    print(base_conversion(original_base, original_number, destination_base))


if __name__ == '__main__':
   main()
