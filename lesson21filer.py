friend = []

while True :
    teman = input("siapa nama teman mu" )
    if teman .lower()== "stop":
        break
    elif teman.strip():
        friend.append(teman.strip())
if not friend:
    print("daftar teman kosong")
else :
    for teman in friend:
        print("hai,", friend )