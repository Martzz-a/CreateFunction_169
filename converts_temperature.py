def converts_temperature(value, unit):
    if unit.upper() == 'C':
        print(f"Konversi suhu dari Celcius: {value}°C, ke Fahrenheit: {value*9/5+32}°F")
    elif unit.upper() == 'F':
        print(f"Konversi suhu dari Fahrenheit: {value}°F, ke Celcius: {(value-32)*5/9}°C")
    else:
        print("Tidak ada unit")

input_value = float(input("Masukkan Nilai Suhu:"))
input_unit = input("Masukkan Unit Suhu(C/F):")
