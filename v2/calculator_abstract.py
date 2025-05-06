# Perform up to 5 numerical operations on the starting value
# oip = input operation
# dip = input digit
# ssf = sum so far
# cosp = count of operations done so far
# osp = list of operations done so far
# dsp = list of digits input so far

import numbers
import operator

oper = {"+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv,
        "**" : operator.pow}
cosp = float(0)
osp = []
dsp = []
finish = False


# Abstract functions:

def opper(oip, dip, ssf):
    return oper[oip](ssf, dip)
    
def opptrack(cosp, osp, dsp):
    local_osp = osp.copy()
    local_dsp = dsp.copy()
    if cosp <= 4:
        return stroppsf(local_osp.pop(0), local_dsp.pop(1), local_osp, local_dsp, str(local_dsp.pop(0)))
    if cosp > 4:
        fosp = osp.pop(0)
        fdsp = dsp.pop(0)
        sdsp = dsp.pop(0)
        ufdsp = opper(fosp, float(sdsp), float(fdsp))
        dsp.reverse()
        dsp.append(str(ufdsp))
        dsp.reverse()
        return stroppsf(local_osp.pop(0), local_dsp.pop(1), local_osp, local_dsp, str(local_dsp.pop(0)))
        
def validnum(dip):
    try: float(dip)
    except ValueError:
        return False
    else:
        return True

def stroppsf(fosp, fdsp, rosp, rdsp, result):
    if rosp == []:
        result = result + " " + fosp + " " + str(fdsp)
        return result
    else:
        return stroppsf(rosp.pop(0), rdsp.pop(0), rosp, rdsp, (result + " " + fosp + " " + str(fdsp)))



# Boot:

print("Enter your starting value.")
fnum = input()
ssf = float(fnum)
dsp = [int(fnum)]
osp = []
print("Current result: " + str(ssf) + ".")



# Loop:

while finish == False:
    print("Enter the next operation and the number being used separated by a comma.")
    print("Example: +, 5")
    print("To finish calculating, enter 'fin, true'")

    inp = input()
    oip, dip = inp.split(",")

    if (oip.strip() == "fin" and dip.strip() == "true"):
        finish = True
        break

    elif (validnum(dip) and oip.strip() in ["+", "-", "*", "/", "**"]):
        ssf = opper(oip.strip(), float(dip), ssf)
        cosp = cosp + 1
        osp.append(oip.strip())
        dsp.append(float(dip))
        print("Current sum: " + str(ssf) + ".")
        print("Last 5 operations done: " + opptrack(cosp, osp, dsp))

    else:
        print("Input values invalid!")
        print("The first part be one of: +, -, *, /, **")
        print("The second part must be a valid rational number.")



# Termination:

print("Final sum: " + str(ssf))
print("Last 5 operations done: " + opptrack(cosp, osp, dsp))
