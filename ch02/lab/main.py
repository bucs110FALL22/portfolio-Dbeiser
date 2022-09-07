import random
#Part A
weeks = 16
print("weeks =",weeks,type(weeks))
classes = 5
print("classes =",classes,type(classes))
tuition = 6000
print("tuition =",tuition,type(tuition),)
classes_per_week = 3
print("classes_per_week =",classes_per_week,type(classes_per_week))
cost_per_week = ((tuition / classes) / weeks)
print("cost_per_week =",cost_per_week,type(cost_per_week))
cost_per_class = (cost_per_week / classes_per_week) 
print("cost_per_class =", cost_per_class,type(cost_per_class))
print("Cost per week:", cost_per_week)
print("Cost per class:", cost_per_class, "-wow its that much?????")
#Part B
fun_list = ["bouncy ball", 2 , 18.66, 7, "toothbrush",]
random_fun = random.choice(fun_list)
print(random_fun)