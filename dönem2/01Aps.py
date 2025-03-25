def cube(num):  # Bir fonksiyon tanımlıyoruz, parametre olarak num alıyor
    return num * num * num  # num'un küpünü döndürüyor

result = cube(4)  # cube fonksiyonuna 4 değerini gönderiyoruz ve sonucu alıyoruz
print(result)  # Sonucu ekrana yazdırıyoruz


class TemperatureConverter:  # Sıcaklık dönüşümleri için bir sınıf oluşturduk
    @staticmethod
    def celsiusToFahrenheit(celsius):  # Celsius'tan Fahrenheit'a çeviren metod
        return (9.0 / 5) * celsius + 32  # Formülü uyguluyoruz

    @staticmethod
    def fahrenheitToCelsius(fahrenheit):  # Fahrenheit'tan Celsius'a çeviren metod
        return (5.0 / 9) * (fahrenheit - 32)  # Formülü uyguluyoruz

# Test programı
print("Celsius -> Fahrenheit | Fahrenheit -> Celsius")
print(f"40.0 -> {TemperatureConverter.celsiusToFahrenheit(40.0):.2f} | 120.0 -> {TemperatureConverter.fahrenheitToCelsius(120.0):.2f}")


def max(a, b):  # max isimli fonksiyon, iki parametre alıyor
    if a > b:  # Eğer a, b'den büyükse
        return a  # a'yı döndür
    else:
        return b  # Aksi halde b'yi döndür

# Test
print(max(7, 12))  # 12 bekleniyor
print(max(20, 5))  # 20 bekleniyor
print(max(-3, -7))  # -3 bekleniyor

