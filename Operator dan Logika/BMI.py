def calc_BMI(berat, tinggi):
    
    #rumus BMI
    BMI = berat / (tinggi**2)

    #cek nilai BMI
    print("Nilai BMI anda:",BMI)

    if (BMI <= 18.5) :
        return "Underweight"
    elif (BMI >= 18.5 and BMI < 25) :
        return "Ideal"
    elif (BMI >= 25 and BMI < 30) :
        return "Kelebihan"
    else:
        return "Anda kegemukan..."

berat = float(input("Berat badan (kg) anda:"))
tinggi = float(input("Tinggi badan (m) anda:"))

result = calc_BMI(berat, tinggi)
print("Keterangan BMI anda saat ini:", result)