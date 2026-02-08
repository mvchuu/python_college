def zlicz_bledy(sciezka_pliku):
    try:
        with open(sciezka_pliku, "r") as file:
            error_count = 0
            for line in file:
                formated_line = line.strip().split(':', 1)
                if len(formated_line) > 1 and 'ERROR' in formated_line[0]:
                    error_count += 1

            return error_count
    
    except FileNotFoundError:
        return 0

liczba_bledow = zlicz_bledy("log.txt")
print(f"Liczba bledow w log wynosi: {liczba_bledow}")
