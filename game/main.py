import random

play = "si"

while play == "si":
  options = ("piedra", "papel", "tijera")
  user_win = 0
  computer_win = 0
  tie = 0
  x = 0
  
  rounds = int(input("Cuantos rondas desea jugar? "))
  
  while x < rounds:
  
    print("*" * 10)
    print("ROUND", x + 1)
    print("*" * 10)
  
    user_option = input("Ingrese piedra, papel o tijera : ").lower()
    while user_option != "piedra" and user_option != "papel" and user_option !=  "tijera":
      print("Opción invalida")
      user_option = input("Por favor intentelo de nuevo. Ingrese piedra, papel o tijera : ").lower()
      
    
    computer_option = random.choice(options)
    
    print(f"Opción del computador {computer_option}")
    
    if user_option == computer_option:
      print('Empate')
      tie += 1
    elif user_option == "piedra":
      if computer_option == "tijera":
        print("Piedra le gana a tijera")
        print("Punto para el usuario")
        user_win += 1
      else:
        print("Papel le gana a piedra")
        print("Punto para el compurador")
        computer_win += 1
    elif user_option == "papel":
      if computer_option == "piedra":
        print("Papel le grana a piedra")
        print("Punto para el usuario")
        user_win += 1
      else:
        print("Tijera le gana a papel")
        print("Punto para el compurador")
        computer_win += 1
    elif user_option == "tijera":
      if computer_option == "papel":
        print("Tijera le grana a papel")
        print("Punto para el usuario")
        user_win += 1
      else:
        print("Piedra le gana a tijera")
        print("Punto para el compurador")
        computer_win += 1
      
    x += 1
    
    if x == rounds or user_win > (rounds - tie) // 2 or computer_win > (rounds - tie) // 2:
      x = rounds
      print("-" * 50)
      print("El juego a finalizado")
      if user_win == computer_win:
        print(f"Han empatado con {user_win} puntos cada uno")
      elif user_win > computer_win:
        print(f"El usuario ha ganado con {user_win} puntos")
      else:
        print(f"El compurador ha ganado con {computer_win} puntos")

      print("-" * 50)
      play = input('Quiere seguir jugando? Digite si (para continuar) o no (para finalizar): ').lower()
      while play != "si" and play != "no":
        print("Opción invalida")
        play = input('Quiere seguir jugando? Digite si (para continuar) o no (para finalizar): ').lower()
        print("+" * 50)
        