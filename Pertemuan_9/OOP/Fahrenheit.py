class KonversiToFahrenheit:
    def __init__(self, celsius):
        self.celsius = celsius

    def konversi(self):
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit

def main():
    celsius_input = float(input("Masukkan suhu dalam Celsius: "))
    konversi_fahrenheit = KonversiToFahrenheit(celsius_input)
    hasil_fahrenheit = konversi_fahrenheit.konversi()
    print(f"{celsius_input}°C sama dengan {hasil_fahrenheit}°F")

if __name__ == "__main__":
    main()
