
def esAnagrama(p1: str, p2: str):
    if len(p1) != len(p2):
        return False

    p2 = list(p2.lower())
    for i in p1.lower():
        if i in p2:
            index = p2.index(i)
            p2.pop(index)
            continue
        else:
            return False
    return True


print(esAnagrama("Dracula", "Alucard"))
