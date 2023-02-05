t=input("write a sentence : ").strip()

c=0 
space=True
for i in t:
  if i==" ":
     if space==True:
       c=c+1
       space=False
  else:
      space=True  


print(f"space: {c}")
