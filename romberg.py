# Menggunakan scipy.integrate untuk memudahkan perhitungan
from scipy import integrate

# Fungsi yang akan diintegrasikan adalah x^3
def f(x):
    return x ** 3

# Metode Trapezoidal
def trapezoidal(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2*(f(a + i * h))
    s *= h/2
    return s

# Mengambil input untuk nilai a, b, dan n
a = int(input("Masukkan batas bawah: "))
b = int(input("Masukkan batas atas: "))
n = int(input("Masukkan jumlah interval: "))
print("")

# Menghitung nilai integral dengan metode Trapezoidal
result_trapezoidal = trapezoidal(a, b, n)

# Menghitung nilai integral dengan metode Integrasi Romberg, menggunakan scipy.integrate.romberg()
result_romberg = integrate.romberg(lambda x: f(x), a, b, show=True)

# hasil sebenarnya dari integral x^3 dari a sampai b
result = integrate.quad(lambda x: f(x), a, b)[0]
true_result = float(''.join(str(result)))

# Menampilkan hasil perhitungan
print("\nMetode Integrasi Analitik:", true_result)
print("Metode Integrasi Trapezoidal:", result_trapezoidal)
print("Metode Integrasi Romberg:", result_romberg)

# Menghitung nilai error
Trelative_error = (abs(true_result - result_trapezoidal) / abs(true_result))*100.0
Rrelative_error = (abs(true_result - result_romberg) / abs(true_result))*100.0

# menampilkan relative error
print("Trapezoidal Er :", round(Trelative_error, 3), "%")
print("Romberg Er :", round(Rrelative_error, 3), "%")