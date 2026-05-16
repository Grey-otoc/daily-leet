def checkInclusion(s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
        return False

    s1_table = {chr(i): 0 for i in range(97, 123)}
    s2_table = {chr(i): 0 for i in range(97, 123)}

    for i in range(len(s1)):
        s1_table[s1[i]] += 1
        s2_table[s2[i]] += 1

    if s1_table == s2_table:
        return True

    for r in range(len(s1), len(s2)):   
        s2_table[s2[r]] += 1
        s2_table[s2[r - len(s1)]] -= 1

        if s1_table == s2_table:
            return True

    return False

if __name__ == "__main__":
    print(checkInclusion("adc", "dcda"))
