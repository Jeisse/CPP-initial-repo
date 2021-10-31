
while True:
    print(" Discover if you Passed or Fail on this curse, please fill in the grades below")
    pas = ["PA 1", "PA 2", "PA 3", "PA 4", "PA 5", "P"]
    allPas = []
    for x in pas:
        pas = float(input(str(x) + " grade: "))
        if x == "P":
            allPas.append(pas*0.5)
        else:
            allPas.append(pas*0.1)

    totalGrade = sum(allPas)
    if totalGrade > 40:
        print("PASS, with grade: "+str(totalGrade))
    else:
        print("FAIL")

    print("")


