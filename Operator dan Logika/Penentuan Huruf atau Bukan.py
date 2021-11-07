#Penentuan huruf atau bukan
print("penentuan huruf atau bukan")
print("--------------------------")
kar=input("Character = ")
huruf = (kar>='A' and kar<='Z')or(kar>='a' and kar<='z')
keterangan ="huruf" if huruf else "bukan huruf"
print(kar, "adalah", keterangan)