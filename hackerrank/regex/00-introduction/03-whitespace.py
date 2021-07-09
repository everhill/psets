#
# Matching Whitespace & Non-Whitespace Character
#
# \s matches any whitespace character
#
# \S matches any non-whitespace character
#
# https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character/problem
#

Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
