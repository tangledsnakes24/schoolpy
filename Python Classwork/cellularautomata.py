#cellular automata





rule18 = {"xxx": ".",
        "xx.": ".",
        "x.x": ".",
        "x..": "x",
        ".xx": ".",
        ".x.": ".",
        "..x": "x",
        "...": "."}
initial_string = (7 * ".") + "x" + (7 * ".")

def run_rule(rule, s):
    new_s = ""


    #find first element
    special_case_neighborhood = s[-1] + s[0] + s[1]
    new_s += rule[special_case_neighborhood]
    #find middle element
    for index in range(1, len(s) - 1):
        neighborhood = s[index - 1 : index + 2]
        new_s += rule[neighborhood]
    #find last element
    neighborhood = s[-2] + s[-1] + s[0]
    new_s += rule[neighborhood]

    return(new_s)
print(run_rule(rule18, "......x......."))
print(run_rule(rule18, ".....x.x......"))
print(run_rule(rule18, "....x...x....."))
