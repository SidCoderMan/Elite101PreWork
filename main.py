#Preset variables and lists, needed for later parts of the code and for loops.
menu_list = ["Fancy Steak", "Fancy Chicken", "Fancy Salad", "Fancy Fruit"]
special_menu = ["Steak with Mashed Potatoes","Ice Cream Sundae","Magic Milkshake","Fancy Pancy Special"]
order = []
order_right = "n"
res_confirm = "n"
time_check = "n"
res_check = "n"
ppl_check = "n"
ppl_check_2 = "n"
confirm_check = "n"
special_check_1 = "n"
special_check_2 = "n"
special_check_3 = "n"
choice_available = "n"
#Reservation section
while res_confirm == "n":
  confirm_check = "n"
  while res_check == "n":
    player_res = input("Waiter:Would you like to make a reservation?(y/n)\n")
    if player_res != "y" and player_res != "n":
      print("Waiter:Please respond with y or n")
      continue
    elif player_res == "y":
      res_check = "y"
    else:
      res_check = "n"
      break
  
  if player_res == "y":
    while res_confirm == "n":
        while time_check == "n":
          try:
            res_time = input("Waiter: What time will you arrive?(No : )\n")
            res_time = int(res_time)
          except ValueError:
            print("Waiter:Only integers allowed in time.")
            continue
          time_check = "y"
        while ppl_check == "n":
          try:
            res_people = input("Waiter: How many people will be coming?\n")
            res_people = int(res_people)
          except ValueError:
            print("Waiter:Please only put integers for the amount of people coming.")
            continue
          ppl_check = "y"
        confirm_check = "n"  
        print("")
        while confirm_check == "n":  
          res_confirm = input(f"Waiter: Okay, you will arrive at {res_time} and {res_people} people will be coming.\nIs this right?(y/n)\n")
          if res_confirm == "y":
            print("Waiter:Good, please continue.\n")
            confirm_check = "y"
            res_people = int(res_people)
            break
          elif res_confirm == "n":
            print("Waiter:I am terribly sorry please re-order.")
            confirm_check = "a"
            res_confirm = "n"
            time_check = "n"
            ppl_check = "n"
          else:
            print("Waiter:Please respond only with y or n")
       
      
     
          
  
  #Order section
  while order_right == "n":
    if player_res == "n":
       while ppl_check_2 == "n":
          try:
            res_people = input("Waiter: How many people will be ordering?\n")
            res_people = int(res_people)
          except ValueError:
            print("Waiter:Please only put integers for the amount of people ordering.")
            continue
          ppl_check_2 = "y"
    for i in range(res_people):
      player_input = input("Waiter:What would you like to order?\n")
      menu = " or ".join(menu_list)
      
      while player_input not in menu_list:
        print("Waiter:Let me show you your options.")
        print(menu)
        player_input = input("Waiter:What would you like to order?\n")
    
      while special_check_1 == "n":
        if choice_available == "n":
          player_choice = input(f"Waiter:Ah, {player_input}, A wonderful choice! But,I also believe our specials are quite Fancy. Would you like to see them?(y/n)\n")
          if player_choice != "y" and player_choice != "n":
            print("Waiter:Please type only y or n.")
          else:
            special_check_1 = "y"
      while special_check_2 == "n":
        if player_choice == "y":
          specialmenu = " and ".join(special_menu)
          print(specialmenu)
          player_choice2 = input("Waiter:Would you like to switch to a special?(y/n)\n")
        else:
          player_choice = "n"
          player_choice2 = "n"
          break
        if player_choice2 != "y" and player_choice2 != "n":
          print("Waiter:Please type only y or n.")
          continue
        else:
          special_check_2 = "y"
          
      
      if player_choice2 == "y":
            player_input = input("Waiter: What would you like?\n")
            while player_input not in special_menu and menu_list:
              print("Waiter:I'm sorry we don't have that")
              print("Waiter:Here is what we have" + "\n" + specialmenu)
              player_input = input("Waiter: What would you like?\n")
   
      elif player_choice2 == "n":
        print("Waiter:Alright then, let's talk about your order.")
      
      else:
        print("Waiter:Please only input y or n.")
    
      #description of options section
      
      if player_input == "Fancy Steak":
        print(f"Waiter: Great choice! A {player_input} is a Fancy Steak is a wonderful cooked steak topped with some special salt and a side of salad")
      elif player_input == "Fancy Chicken":
        print(f"Waiter: Great choice! A {player_input} is a Fancy Chicken is covered with ranch and ketchup in a pattern, it is surrounded by lettuce")
      elif player_input == "Fancy Salad":
        print(f"Waiter: Great choice! A {player_input} is a Fancy Salad is covered in Ranch and has an assortment of fruits and vegetables")
      elif player_input == "Fancy Fruit":
        print(f"Waiter:Great choice! A {player_input} is a Fancy Fruit is an assortment of delicous fruits")
      elif player_input == "Steak with Mashed Potatoes":
        print(f"Waiter:Great choice! A {player_input} is a Steak with Mashed Potatoes is a Fancy Steak with a side of seasoned mashed potatoes")
      elif player_input == "Ice Cream Sundae":
        print(f"Waiter:Great choice! A {player_input} is a Ice Cream Sundae is 3 icecream scoops drizzled in Mershey's Syrup")
      elif player_input == "Magic Milkshake":
        print(f"Waiter:Great choice! A {player_input} is a Normal milkshake but with a magic flavor")
      else:
        print(f"Waiter:Great choice! A {player_input} is a Fancy Pancy Special made from Mr. Fancy Pancy himself")
      #order setup
      player_input = "".join(player_input)
      order_order = "1 "+player_input+","
      order.extend(order_order)
      print("\n")
      if i+1 < res_people:
        print("Waiter:Next order...\n\n")
      ppl_check_2 = "n"
      confirm_check = "n"
      special_check_1 = "n"
      special_check_2 = "n"
      special_check_3 = "n"
      choice_available = "n"
  
    #order confirmation
    final_order = "".join(order)
    order_right = input(f"Waiter:Is this the right order? {final_order}(y/n)\n")
    if order_right == "y":
      print("Waiter:Thank you, goodbye!")
    else:
      print("Waiter:Please order again, sorry.")