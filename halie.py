n=int(input())
infos = []
for _ in range (n):
      student_info=input()
      info = student_info.split("#")
      infos.append(info)
      
for info in infos:
      print(*info)



