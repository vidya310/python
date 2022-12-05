age={"efg":34,"eac":42,"ijk":20,"abc":27}
age_list=list(age.items())
age_list.sort()
print("In ascending order:",age_list)
age_list=list(age.items())
age_list.sort(reverse=True)
print("In descending order:",age_list)
dict=dict(age_list)
print("Dictionary is:",dict)
