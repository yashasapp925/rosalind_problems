n = 32
k = 3

current_gen = 1
past1 = 1
past2 = 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
for i in range (0, n - 2):
    current_gen = past1 + k * past2
    past2 = past1
    past1 = current_gen
print(current_gen)
