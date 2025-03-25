import random

# Funkcja do obliczania współczynników różnicowych
def oblicz_roznice(x, y):
    n = len(x)
    roznice = [[0 for _ in range(n)] for _ in range(n)]
    
    # Uzupełniamy pierwszą kolumnę różnicami
    for i in range(n):
        roznice[i][0] = y[i]
    
    # Obliczamy pozostałe różnice
    for j in range(1, n):
        for i in range(n-j):
            roznice[i][j] = (roznice[i+1][j-1] - roznice[i][j-1]) / (x[i+j] - x[i])
    
    return roznice

# Funkcja do interpolacji Newtona
def interpolacja_newtona(x, y, x_punkt):
    n = len(x)
    roznice = oblicz_roznice(x, y)
    wynik = roznice[0][0]
    
    for i in range(1, n):
        temp = roznice[0][i]
        for j in range(i):
            temp *= (x_punkt - x[j])
        wynik += temp
    
    return wynik

# Funkcja do wypełnienia tabeli x i y ręcznie lub automatycznie
def wypelnij_tabele():
    wybor = input("Czy chcesz ręcznie wprowadzić dane? (tak/nie): ").strip().lower()
    
    if wybor == "tak":
        n = int(input("Podaj liczbę węzłów (n): "))
        x = []
        y = []
        for i in range(n):
            x_val = float(input(f"Podaj x_{i+1}: "))
            y_val = float(input(f"Podaj y_{i+1}: "))
            x.append(x_val)
            y.append(y_val)
    else:
        n = int(input("Podaj liczbę węzłów (n): "))
        x = [random.uniform(0, 15) for _ in range(n)]
        y = [random.uniform(0, 15) for _ in range(n)]
        print(f"Generowane węzły x: {x}")
        print(f"Generowane węzły y: {y}")
    
    return x, y

# Program główny
def main():
    x, y = wypelnij_tabele()
    x_punkt = float(input("Podaj wartość x, dla której chcesz obliczyć interpolację: "))
    
    wynik = interpolacja_newtona(x, y, x_punkt)
    print(f"Interpolowana wartość w punkcie x = {x_punkt}: {wynik}")

if __name__ == "__main__":
    main()
