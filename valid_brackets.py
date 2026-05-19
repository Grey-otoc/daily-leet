def isValid(s: str) -> bool:
    if len(s) == 1:
        return False

    matches = {")" : "(", "}" : "{", "]" : "["}
    openers = [s[0]]

    for brack in s[1:]:
        if brack in matches:
            if openers and openers[-1] == matches[brack]:
                openers.pop()
            else:
                return False
        else:
            openers.append(brack)

    return True if not openers else False

if __name__ == "__main__":
    print(isValid("([{]}])"))
