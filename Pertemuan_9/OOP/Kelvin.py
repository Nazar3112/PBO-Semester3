class KonversiToKelvin:
    def __init__(self, celsius):
        self.celsius = celsius

    def konversi(self):
        kelvin = self.celsius + 273.15
        return kelvin

def main():
    celsius_input = float(input("Masukkan suhu dalam Celsius: "))
    konversi_kelvin = KonversiToKelvin(celsius_input)
    hasil_kelvin = konversi_kelvin.konversi()
    print(f"{celsius_input}°C sama dengan {hasil_kelvin}K")

if __name__ == "__main__":
    main()
