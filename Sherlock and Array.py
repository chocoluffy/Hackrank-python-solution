# -*- coding: UTF-8 -*-

case_number = int(raw_input())
array_for_length_of_case = []
nested_array_of_cases = []
for i in range(case_number):
    array_for_length_of_case.append(int(raw_input()))
    nested_array_of_cases.append(map(int, raw_input().split()))

for case in nested_array_of_cases:
    flag = False
    prefix = []
    for i in case:
        if len(prefix) == 0:
            prefix.append(i)
        else:
            prefix.append(i + prefix[len(prefix)-1])
    for i in range(len(prefix)):
        if (i == 0 or i == len(prefix)-1):
            continue
        else:
            if prefix[i-1] == prefix[len(prefix)-1] - prefix[i]:
                flag = True
    if flag:
        print "YES"
    else:
        print "NO"

    