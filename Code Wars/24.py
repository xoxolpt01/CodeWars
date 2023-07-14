def solution(text, ending):
    try:
        for i in list(ending):
            text.index(i)
        return True
    except:
        if ending != text:
            return False


print('False == ', solution("jrafnlozkcvwydgfcyhyrmn",
                           "lozkcvwydffgyhywmn"))
print("True == ", solution('sumo', "omo"))