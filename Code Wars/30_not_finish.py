'''
Complete the solution so that it returns true
if the first argument(string) passed in ends
with the 2nd argument (also a string).

Examples:
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''

def solution(text, ending):
    if ending != text:
        return False
    try:
        for i in list(ending):
            text.index(i)
        return True
    except:
        return False


print('True == ', solution("jrafnlozkcvwydgfcyhyrmn",
                           "lozkcvwydffgyhywmn"))

'''
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)

'''