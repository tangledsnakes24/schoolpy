#cellular automata
def rule_string(n):
    powerof2 = 128
    s = ""
    while powerof2 >= 1:
        if n >= powerof2:
            s += "x"
            n -= powerof2

        else:
            s += "."
        powerof2 = powerof2 / 2
    return(s)

print(rule_string(1)) #...x..x.
print(rule_string(2))
print(rule_string(3))
print(rule_string(4))
print(rule_string(5))



print("__________________________________")
rule0 = {"xxx":".",
        "xx.": ".",
        "x.x": ".",
        "x..": ".",
        ".xx": ".",
        ".x.": ".",
        "..x": ".",
        "...": "."}








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

print("__________________________________")

def evolve(rule, initial_string, number_generations):
    print(initial_string)
    for gen in range(number_generations):
        initial_string = run_rule(rule, initial_string)
        print(initial_string)    
    return()
print(evolve(rule18, ".......x.......", 8))
print(evolve(rule18, (20 * ".") + "x" + (20 * "."), 40))
print("__________________________________")
