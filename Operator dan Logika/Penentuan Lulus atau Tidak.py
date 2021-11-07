#Penentuan lulus atau tidak
print("Penentuan lulus atau tidak")
print("--------------------------")
nilai=int(input("nilai="))
lulus = (nilai >= 60)
hasil="LULUS BOS" if lulus else "TIDAK LULUS"
print(hasil)