input_jarijari = float(input("Masukkan Jari-Jari Lingkaran:"))

circle_area = lambda r: 3.14 * r * r

result = circle_area(input_jarijari)

print(f"Luas Lingkaran dengan jari-jari: {input_jarijari} adalah {result}")