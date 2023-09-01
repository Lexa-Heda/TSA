from mpmath import mp

# Setze die Genauigkeit (Anzahl der Dezimalstellen)
mp.dps = 50  # Zum Beispiel auf 50 Dezimalstellen

# Erstelle mpmath-Objekte
x = mp.mpf('3.141592653589793238462643383279')
y = mp.mpf('1.414213562373095048801688724209')

# Führe Berechnungen mit den mpmath-Objekten durch
ergebnis = x * y

print(str(ergebnis))