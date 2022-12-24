s=int(input("Enter a the Values in the List :"))
list=[ ]
for i in range(0,s):
  element =int(input("Enter the Value :"))
  list.append(element)
print("Circulating the list")
for i in range(0,s):
  element_deleted=list.pop(0)
  list.append(element_deleted)
  print(" The Circulated list after",i+1,"rotation",list)
