def cube(num):  # Bir fonksiyon tanımlıyoruz, parametre olarak num alıyor
    return num * num * num  # num'un küpünü döndürüyor

result = cube(4)  # cube fonksiyonuna 4 değerini gönderiyoruz ve sonucu alıyoruz
print(result)  # Sonucu ekrana yazdırıyoruz


def celsiusToFahrenheit(celsius):  # Celsius'tan Fahrenheit'a çeviren fonksiyon
    return (9.0 / 5) * celsius + 32  # Formülü uyguluyoruz

def fahrenheitToCelsius(fahrenheit):  # Fahrenheit'tan Celsius'a çeviren fonksiyon
    return (5.0 / 9) * (fahrenheit - 32)  # Formülü uyguluyoruz

# Test edelim
print("40°C ->", celsiusToFahrenheit(40), "°F")  # 40 Celsius'u Fahrenheit'a çevir
print("120°F ->", fahrenheitToCelsius(120), "°C")  # 120 Fahrenheit'ı Celsius'a çevir


def max(a, b):  # max isimli fonksiyon, iki parametre alıyor
    if a > b:  # Eğer a, b'den büyükse
        return a  # a'yı döndür
    else:
        return b  # Aksi halde b'yi döndür

# Test
print(max(7, 12))  # 12 bekleniyor
print(max(20, 5))  # 20 bekleniyor
print(max(-3, -7))  # -3 bekleniyor

