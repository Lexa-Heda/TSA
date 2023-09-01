from decimal import Decimal, getcontext

# Setze die Genauigkeit des decimal-Moduls (Anzahl der Dezimalstellen)
getcontext().prec = 30  # Zum Beispiel auf 30 Dezimalstellen

# Erstelle Decimal-Objekte
x = Decimal('3.141592653589793238462643383279')
y = Decimal('1.414213562373095048801688724209')

# Führe Berechnungen mit den Decimal-Objekten durch
ergebnis = x * y

print(ergebnis)