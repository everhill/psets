#
# Matching Digits & Non-Digit Characters
#
# The expression \d matches any digit [0 - 9]
#
# The expression \D matches any character that is not a digit
#
# https://www.hackerrank.com/challenges/matching-digits-non-digit-character/problem
#

Regex_Pattern = r"\d{2}\D\d{2}\D\d{4}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
