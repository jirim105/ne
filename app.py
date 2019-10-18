
class Kurva:
  def thot(self, jakyKozy, posilaNudes, jmeno, kolikratJebala):
    print("Thot " + jmeno + " má tyto vlastnosti:")

    if(posilaNudes == "a"):
      print("Thot " + jmeno + " " + "posílá nudes")
    elif(posilaNudes == "n"):
      print("Thot " + jmeno + " " + "neposílá nudes")
    else:
      print("Thot " + jmeno + " " + posilaNudes)

    print("Thot " + jmeno + " má kozy - " + jakyKozy)
    print("Thot jebala - " + kolikratJebala + "\n")


def main():
  kurva = Kurva()

  print("Ahoj jako, tahle věc ti prozradí informace o kurvách\n")
  print("Můžeš si vybrat z předem definovaných kurev nebo si definovat svojí")

  definovatKurvu = input("Definovat svojí? a/n\n")

  if(definovatKurvu == "a"):
    typKurvy = input("\nJaký typ kurvy bude tvoje kurva?\n 1 - Thot\n")
    jmeno = input("\nJak se bude kurva jmenovat?\n")
    posilaNudes = input("\nPosílá tvoje kurva nudes? a/n\n")
    kolikratJebala = input("\nKolikrát tvoje kurva jebala?\n")
    jakyKozy = input("\nJaký má tvoje kurva kozy?\n")

    if(typKurvy == "1"):
      kurva.thot(jakyKozy, posilaNudes, jmeno, kolikratJebala)
    else:
      print("ne")

  elif(definovatKurvu == "n"):
    print("\nO jaký kurvě by si chtěl vědět informace?\n")
    
    jakaKurva = input("\n1 - Aneta \n2 - Novotná\n3 - Pejsek\n")

    if(jakaKurva == "2"):
      kurva.thot("EXTRA", "posílá nudes a hodně", "Novotná", "to nikdo neví, ale hoooodněkrát")
    elif(jakaKurva == "1"):
      kurva.thot(":(((", "neposílá nudes naštěstí", "Aneta", "to ví štěpán")
    elif(jakaKurva == "3"):
      kurva.thot("HMMM", "HMMM", "Pejsek", "HMMM")
    else:
      print("\nSi debil")

  else:
    print("Si debil")
    pass


main()

opakovat = "a"
opakovat = input("Opakovat? a/n\n")
if (opakovat == "a"):
  main()
elif(opakovat == "n"):
  pass
else:
  print("Zab se")
