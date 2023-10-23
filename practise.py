myFinalMarks={'CSF':50, 'FunPro':80, 'WT':60}

def calculate_average(final_marks):
    total=0
    for key in final_marks:
        total=total+final_marks(key)
    average=total/len(finalMarks)
    return average

print(calculate_average(myFinalMarks))



module=input("Module Name")
mark=input("Mark here")
myFinalMarks[module]=int(mark)
print(myFinalMarks)
print(calculate_average(myFinalMarks))






