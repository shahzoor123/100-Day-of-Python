def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  return b_list

x = mutate([1,2,3,5,8,13])

def sum_of_list(list_to_sum):
    y  = sum(list_to_sum)
    print(y)
    
        
def calling():
    sum_of_list(x)
    
calling()