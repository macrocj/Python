#Author: JC
#Date: 8/12/2018
#Version: 1.0

def get_valid_ip_adddress(s):
    def is_valid_part(s):
        # "00', "000'', '01'. ect. are not valid, but'0' is valid.
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)

    result, parts = [] ,[None]*4
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if is_valid_part(parts[0]):
            for j in range(1, min(len(s) - i, 4)):
                parts[1] = s[i:i+j]
                if is_valid_part(parts[1]):
                    for k in range(1, min(len(s) - i - j, 4)):
                        parts[2], parts[3] = s[i + j: i+j+k], s[i+j+k:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            result.append('.'.join(parts))
    return result

print(get_valid_ip_adddress('19000'))

def selftry(s):
    def valid(s):
        # Ture or False return True
        return len(s)==1 or (s[0] != '0'  and int(s) <= 255)
    result, parts = [], [None]*4
    for i in range(1,min(4,len(s))):
        parts[0] = s[:i]
        if valid(parts[0]):
            for j in range(1, min(len(s)-1,4)):
                parts[1] = s[i:i+j]
                if valid(parts[1]):
                    for k in range(1, min(len(s)-1,4)):
                        parts[2], parts[3] = s[i+j: i+j+k], s[i+j+k:]
                        if valid(parts[2]) and valid(parts[3]):
                            result.append('.'.join(parts))
    return result
print(selftry('19000'))
#####
# selftry need to edit on list length
# each loop need to substract the previous length of list


