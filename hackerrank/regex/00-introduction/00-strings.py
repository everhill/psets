#
# Matching Specific String
#
# We can match a specific string by making our search pattern that string.
#
# https://www.hackerrank.com/challenges/matching-specific-string/problem
#

Reegex_Pattern = r'hackerrank'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
