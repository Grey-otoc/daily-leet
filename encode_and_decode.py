def encode(strs: list[str]) -> str:
    encoded_strs = [f"{len(s)}#{s}" for s in strs]

    encoded_s = "".join(s for s in encoded_strs)

    return encoded_s


def decode(s: str) -> list[str]:
    strs = []
    i = 0

    while i < len(s):
        j = i
        length = ""
        while s[j] != "#":
            j += 1

        length = int(s[i:j])
        
        word = s[j+1 : j+1+length]
        strs.append(word)

        i = j + 1 + length

    return strs
