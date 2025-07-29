import colorama as cl
from colorama import Fore, Back, Style
cl.init(autoreset=True)

def update_daily_schedule(route, mode):
    from datetime import datetime, timedelta
    today = datetime.today()
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    new_day = (datetime.today() + timedelta(days=60)).strftime("%Y-%m-%d")

    old_file = f"{route}_{mode}_{yesterday}.txt"
    new_file = f"{route}_{mode}_{new_day}.txt"
    base_file = f"{route}_{mode}.txt"

    # Delete yesterday's file
    if os.path.exists(old_file):
        os.remove(old_file)

        f=open(base_file, "r")
        data=f.readlines()
        f.close()
        
        f=open(f"{new_file}", "w")
        for line in data:
            f.write(line)
        f.close()
    return

def delete_60_days_files(route, mode):  
    from datetime import datetime, timedelta
    today = datetime.today()
    for i in range(61):
        new_day = today + timedelta(days=i)
        new_day_str = new_day.strftime("%Y-%m-%d")
        file_name = f"{route}_{mode}_{new_day_str}.txt"
        if os.path.exists(file_name):
            os.remove(file_name)

    return

       

def daily_run():
   f=open("routes.txt","r")
   data=f.readlines()
   f.close()
   routes=[]
   for line in data:
        route=line.strip().replace("---->", "_")
        routes.append(route)      
   
   for i in routes:
       for j in ("car","train","bus","flight"):
                    update_daily_schedule(i,j)

   return


def create_60_days_files(route,mode):
    from datetime import datetime, timedelta
    today = datetime.today()
    for i in range(61):
        new_day = today + timedelta(days=i)
        new_day_str = new_day.strftime("%Y-%m-%d")
        file_name = f"{route}_{mode}_{new_day_str}.txt"

        f=open(f"{route}_{mode}.txt","r")
        data=f.readlines()
        f.close()

        f=open(file_name, "a")
        f.close

        f=open(file_name, "w")
        for line in data:
            f.write(line)
        f.close()

    return


def route_selection():
    f=open("routes.txt","r")
    data=f.readlines()
    print(Fore.CYAN + "\nAVAILABLE ROUTES:\n" + Style.RESET_ALL)
    line_number=1
    for line in data:
        print(Fore.YELLOW + f"{line_number}.{line}" + Style.RESET_ALL, end='')
        line_number+=1
    f.close()
    route=int(input(Fore.GREEN + "\nENTER YOUR CHOICE:" + Style.RESET_ALL))

    f=open("routes.txt","r")
    data=f.readlines()
    line_number=1
    for line in data:
        if line_number==route:
            file=line.strip().replace("---->", "_")     # strip()---->for removing \n from the last
            break
        line_number+=1

    f.close()
    return file
  

def generate_ticket_number():
        import random
        number=(random.randint(1000000000,9999999999))
        f=open("ticket_number.txt","r")
        data=f.readlines()
        f.close()
        probleum=0
        for line in data:
            if str(number) in line:
                number=(random.randint(1000000000,9999999999))
                probleum=1
                break
            else:
                pass

        if probleum==0:
            f=open("ticket_number.txt","a")
            f.write(f"{number}\n")
            f.close()
            return number
        else:
            return generate_ticket_number()
        
        
        

def admin_start():
    admin_starting_choice=int(input(Fore.BLUE + "\n1.EDIT TIME TABLE\n2.UPDATE TIME TABLE\n3.ADD ROUTE\n4.REMOVE ROUTE\n5.LOGOUT\nENTER YOUR CHOICE:" + Style.RESET_ALL))
    if admin_starting_choice==1:
              admin_routes=route_selection()
              admin_mode=int(input(Fore.MAGENTA + "\nMODES OF TRAVELLING\n1.CAR\n2.TRAIN\n3.BUS\n4.FLIGHT\nENTER YOUR CHOICE:" + Style.RESET_ALL))
              if admin_mode==1:
                    edit_mode(admin_routes,"car")
              elif admin_mode==2:
                    edit_mode(admin_routes,"train")
              elif admin_mode==3:
                   edit_mode(admin_routes,"bus")
              elif admin_mode==4:
                   edit_mode(admin_routes,"flight")
              else:
                     print(Fore.RED + "\nINVALID CHOICE" + Style.RESET_ALL)
                     admin_start()
                     
       
    elif admin_starting_choice==2:
        admin_routes=route_selection()
        admin_mode=int(input(Fore.MAGENTA + "\nMODES OF TRAVELLING\n1.CAR\n2.TRAIN\n3.BUS\n4.FLIGHT\nENTER YOUR CHOICE:" + Style.RESET_ALL))
        update_admin_choice=int(input(Fore.CYAN + "\n1.ADD NEW\n2.REMOVE OLD\nENTER YOUR CHOICE:" + Style.RESET_ALL))



        if update_admin_choice==1:
            
         if admin_mode==1:
             
           add_mode(admin_routes,"car")
           
         elif admin_mode==2:
             
           add_mode(admin_routes,"train")
           
         elif admin_mode==3:
             
           add_mode(admin_routes,"bus")
           
         elif admin_mode==4:
             
           add_mode(admin_routes,"flight")
           
         else:
            print(Fore.RED + "\nINVALID CHOICE" + Style.RESET_ALL)
            print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
            admin_start()

        elif update_admin_choice==2:
            
          if admin_mode==1:
              
              remove_mode(admin_routes,"car")
              
          elif admin_mode==2:
              
             remove_mode(admin_routes,"train")
             
          elif admin_mode==3:
              
             remove_mode(admin_routes,"bus")
             
          elif admin_mode==4:
              
             remove_mode(admin_routes,"flight")
             
          else:
              print(Fore.RED + "\nINVALID CHOICE" + Style.RESET_ALL)
              print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
              admin_start()
              
        else:
            print(Fore.RED + "\nINVALID CHOICE" + Style.RESET_ALL)
            print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
            admin_start()
            

    elif admin_starting_choice==3:
        f=open("routes.txt","a")
        route_start=input(Fore.BLUE + "\nENTER THE STARTING POINT:" + Style.RESET_ALL)
        route_end=input(Fore.BLUE + "ENTER THE DESTINATION POINT:" + Style.RESET_ALL)
        route_start_upper=route_start.upper()
        route_end_upper=route_end.upper()
        f.write(f"{route_start_upper}---->{route_end_upper}\n")
        f.close()
        
        f1=open(f"{route_start_upper}_{route_end_upper}_car.txt","w")
        f2=open(f"{route_start_upper}_{route_end_upper}_train.txt","w")
        f3=open(f"{route_start_upper}_{route_end_upper}_bus.txt","w")
        f4=open(f"{route_start_upper}_{route_end_upper}_flight.txt","w")
        f1.write("CAR NUMBER       SOURCE TIME      DESTINATION TIME      TOTAL TIME     T.SEATS      REMAINING SEATS\n")
        f2.write("TRAIN NUMBER     SOURCE TIME      DESTINATION TIME      TOTAL TIME     T.SEATS      REMAINING SEATS\n")
        f3.write("BUS NUMBER       SOURCE TIME      DESTINATION TIME      TOTAL TIME     T.SEATS      REMAINING SEATS\n")
        f4.write("FLIGHT NUMBER    SOURCE TIME      DESTINATION TIME      TOTAL TIME     T.SEATS      REMAINING SEATS\n")
        f1.close()
        f2.close()
        f3.close()
        f4.close()

        route_60=(f"{route_start_upper}_{route_end_upper}")

        create_60_days_files(route_60,"car")
        create_60_days_files(route_60,"train")
        create_60_days_files(route_60,"bus")
        create_60_days_files(route_60,"flight")
        

        print(Fore.GREEN + "\nROUTE ADDED" + Style.RESET_ALL)
        print(Fore.YELLOW + "\n******************************************************\n" + Style.RESET_ALL)
        admin_start()

    elif admin_starting_choice==4:
        f=open("routes.txt","r")
        data=f.readlines()
        print(Fore.CYAN + "\nAVAILABLE ROUTES:\n" + Style.RESET_ALL)

        line_number=1
        
        for line in data:
            print(Fore.YELLOW + f"{line_number}.{line}" + Style.RESET_ALL, end='')
            line_number+=1
        f.close()
        route_to_remove=int(input(Fore.RED + "\nENTER THE ROUTE TO REMOVE:" + Style.RESET_ALL))
        updated_data=[]
        f=open("routes.txt","a")
        line_number=1
        for line in data:
            if line_number!=route_to_remove:
                updated_data.append(line)
            elif line_number==route_to_remove:
                route=line.strip().replace("---->", "_")
                os.remove(f"{route}_car.txt")
                os.remove(f"{route}_train.txt")
                os.remove(f"{route}_bus.txt")
                os.remove(f"{route}_flight.txt")

            line_number+=1

        delete_60_days_files(route,"car")
        delete_60_days_files(route,"train")
        delete_60_days_files(route,"bus")
        delete_60_days_files(route,"flight")

        f=open("routes.txt","w")
        f.writelines(updated_data)
        f.close()
        print(Fore.GREEN + "\nROUTE REMOVED" + Style.RESET_ALL)
        print(Fore.YELLOW + "\n******************************************************\n" + Style.RESET_ALL)
        admin_start()
        



    elif admin_starting_choice==5:
        intro()

    else:
        print(Fore.RED + "\nINVALID CHOICE" + Style.RESET_ALL)
        print(Fore.YELLOW + "\n******************************************************\n" + Style.RESET_ALL)
        admin_start()
        
        
        
        

def user_start(user_id):
     user_starting_choice=int(input(Fore.BLUE + "\n1.BOOK TICKET\n2.PAST BOOKINGS\n3.CANCEL BOOKING\n4.LOGOUT\nENTER YOUR CHOICE:" + Style.RESET_ALL))
     if user_starting_choice==1:
            print(Fore.CYAN + "\nWELCOME TO BOOKING MODE" + Style.RESET_ALL)
            user_mode_choice=int(input(Fore.MAGENTA + "\nMODES OF TRAVELLING\n1.CAR\n2.TRAIN\n3.BUS\n4.FLIGHT\nENTER YOUR CHOICE:" + Style.RESET_ALL))
            user_route_choice=route_selection()

            if user_mode_choice==1:
                print(Fore.GREEN + "\nWELCOME TO CAR BOOKING" + Style.RESET_ALL)
                mode_book(user_route_choice,"car",user_id)

            elif user_mode_choice==2:
                print(Fore.GREEN + "\nWELCOME TO TRAIN BOOKING" + Style.RESET_ALL)
                mode_book(user_route_choice,"train",user_id)

            elif user_mode_choice==3:
                print(Fore.GREEN + "\nWELCOME TO BUS BOOKING" + Style.RESET_ALL)
                mode_book(user_route_choice,"bus",user_id)

            elif user_mode_choice==4:
                print(Fore.GREEN + "\nWELCOME TO FLIGHT BOOKING" + Style.RESET_ALL)
                mode_book(user_route_choice,"flight",user_id)
            
            else:
                print(Fore.RED + "\nINVALID CHOICE" + Style.RESET_ALL)
                print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
                user_start(user_id)
                
                

     elif user_starting_choice==2:
         print(Fore.CYAN + "\n*************PAST BOOKINGS*************" + Style.RESET_ALL)
         print(Fore.YELLOW + "\nCAR BOOKINGS:\n" + Style.RESET_ALL)
         f=open(f"{user_id}_car_bookings.txt","r")
         data=f.readlines()
         if data:
            print(Fore.BLUE + "CAR NUMBER       SOURCE TIME      DESTINATION TIME      TOTAL TIME     PASSENGER NAME           AGE      TICKET NUMBER          DATE\n" + Style.RESET_ALL)
            for line in data:
             print(Fore.WHITE + line + Style.RESET_ALL, end='')
         else:
             print(Fore.YELLOW + "\n          NO PAST CAR BOOKINGS" + Style.RESET_ALL)
         f.close()

         print(Fore.YELLOW + "\nTRAIN BOOKINGS:\n" + Style.RESET_ALL)
         f=open(f"{user_id}_train_bookings.txt","r")
         data=f.readlines()
         if data:
            print(Fore.BLUE + "TRAIN NUMBER     SOURCE TIME      DESTINATION TIME      TOTAL TIME     PASSENGER NAME           AGE      TICKET NUMBER         DATE\n" + Style.RESET_ALL)
            for line in data:
             print(Fore.WHITE + line + Style.RESET_ALL, end='')
         else:
             print(Fore.YELLOW + "\n          NO PAST TRAIN BOOKINGS" + Style.RESET_ALL)
         f.close()

         print(Fore.YELLOW + "\nBUS BOOKINGS:\n" + Style.RESET_ALL)  
         f=open(f"{user_id}_bus_bookings.txt","r")
         data=f.readlines()
         if data:
            print(Fore.BLUE + "BUS NUMBER       SOURCE TIME      DESTINATION TIME      TOTAL TIME     PASSENGER NAME           AGE      TICKET NUMBER         DATE\n" + Style.RESET_ALL)
            for line in data:
             print(Fore.WHITE + line + Style.RESET_ALL, end='')
         else:
             print(Fore.YELLOW + "\n          NO PAST BUS BOOKINGS" + Style.RESET_ALL)
         f.close()

         print(Fore.YELLOW + "\nFLIGHT BOOKINGS:\n" + Style.RESET_ALL)
         f=open(f"{user_id}_flight_bookings.txt","r")
         data=f.readlines()
         if data:
            print(Fore.BLUE + "FLIGHT NUMBER    SOURCE TIME      DESTINATION TIME      TOTAL TIME     PASSENGER NAME           AGE      TICKET NUMBER         DATE\n" + Style.RESET_ALL)
            for line in data:
             print(Fore.WHITE + line + Style.RESET_ALL, end='')
         else:
             print(Fore.YELLOW + "\n          NO PAST FLIGHT BOOKINGS" + Style.RESET_ALL)
         f.close()
         print("\n")
         print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
         
         user_start(user_id)
    
     elif user_starting_choice==3:
         print(Fore.YELLOW + "\nCAR BOOKINGS:\n" + Style.RESET_ALL)
         f=open(f"{user_id}_car_bookings.txt","r")
         data=f.readlines()

         if data:  
            print(Fore.BLUE + "CAR NUMBER       SOURCE TIME      DESTINATION TIME      TOTAL TIME     PASSENGER NAME           AGE        TICKET NUMBER        DATE\n" + Style.RESET_ALL)
            
            for lines in data:
                    print(Fore.WHITE + lines + Style.RESET_ALL, end='')
         else:
                print(Fore.YELLOW + "          NO PAST CAR BOOKINGS" + Style.RESET_ALL)

         f.close()
         
         print(Fore.YELLOW + "\nTRAIN BOOKINGS:\n" + Style.RESET_ALL)
         f=open(f"{user_id}_train_bookings.txt","r")
         data=f.readlines()

         if data:
            print(Fore.BLUE + "TRAIN NUMBER     SOURCE TIME      DESTINATION TIME      TOTAL TIME     PASSENGER NAME           AGE        TICKET NUMBER        DATE\n" + Style.RESET_ALL)
            
            for lines in data:
                    print(Fore.WHITE + lines + Style.RESET_ALL, end='')
         else:
            print(Fore.YELLOW + "          NO PAST TRAIN BOOKINGS" + Style.RESET_ALL)
         f.close()
         print(Fore.YELLOW + "\nBUS BOOKINGS:\n" + Style.RESET_ALL) 
         f=open(f"{user_id}_bus_bookings.txt","r")
         data=f.readlines()
         if data: 
            print(Fore.BLUE + "BUS NUMBER       SOURCE TIME      DESTINATION TIME      TOTAL TIME     PASSENGER NAME           AGE        TICKET NUMBER        DATE\n" + Style.RESET_ALL)
            for lines in data:
                    print(Fore.WHITE + lines + Style.RESET_ALL, end='')
         else:
            print(Fore.YELLOW + "          NO PAST BUS BOOKINGS" + Style.RESET_ALL)
         f.close()
         print(Fore.YELLOW + "\nFLIGHT BOOKINGS:\n" + Style.RESET_ALL)
         f=open(f"{user_id}_flight_bookings.txt","r")
         data=f.readlines()
         if data:
            print(Fore.BLUE + "FLIGHT NUMBER    SOURCE TIME      DESTINATION TIME      TOTAL TIME     PASSENGER NAME           AGE        TICKET NUMBER        DATE\n" + Style.RESET_ALL)  
            for lines in data:
                    print(Fore.WHITE + lines + Style.RESET_ALL, end='')
         else:
            print(Fore.YELLOW + "          NO PAST FLIGHT BOOKINGS" + Style.RESET_ALL)
         f.close() 
         print("\n")

         user_mode_choice=int(input(Fore.MAGENTA + "\nMODES OF TRAVELLING\n1.CAR\n2.TRAIN\n3.BUS\n4.FLIGHT\nENTER YOUR CHOICE:" + Style.RESET_ALL))

         if user_mode_choice==1:
             cancel_booking("car",user_id)

         elif user_mode_choice==2:
                cancel_booking("train",user_id)

         elif user_mode_choice==3:
                cancel_booking("bus",user_id)

         elif user_mode_choice==4:
                cancel_booking("flight",user_id)

         else:
                print(Fore.RED + "\nINVALID CHOICE" + Style.RESET_ALL)
                print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
                user_start(user_id)

     elif user_starting_choice==4:
            intro()

     else:
            print(Fore.RED + "\nINVALID CHOICE" + Style.RESET_ALL)
            print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
            user_start(user_id)
            
            
            

def cancel_booking(y,user_id):
    file_name = f"{user_id}_{y}_bookings.txt"
    f = open(file_name, "r")
    data = f.readlines()
    f.close()
    upper_case= y.upper()
    car_number_to_cancel=input(Fore.RED + f"\nENTER THE TICKET NUMBER TO CANCEL:" + Style.RESET_ALL)
    if len(car_number_to_cancel)<10:
        print(Fore.RED + "\nINVALID TICKET NUMBER" + Style.RESET_ALL)
        print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
        cancel_booking(y,user_id)
    updated_data = []
    error=0
    for line in data:
        if car_number_to_cancel not in line:
            updated_data.append(line)
        else:
            error=1
            parts=line.strip().split()
            number=parts[0]
            fb=open("routes.txt","r")
            data_routes=fb.readlines()
            fb.close()
            routes=[]
            date=parts[6]
            for route in data_routes:
                routes.append(route.strip().replace("---->", "_"))
                
                
                

            updated_data_route=[]
            
            for route in routes:
                        file_name_open=open(f"{route}_{y}_{date}.txt")
                        data=file_name_open.readlines()
                        file_name_open.close()
                        found=0
                        for line in data:
                            if number in line:
                                found=1
                                break

                        if found==1:
                            for line in data:
                                route_change=route
                                if number in line:
                                    parts=line.strip().split()
                                    seats_left=int(parts[5])
                                    parts[5]=str(seats_left+1)
                                    updated_line = f"{parts[0]:<18}{parts[1]:<18}{parts[2]:<22}{parts[3]:<16}{parts[4]:<16}{parts[5]:<10}\n"
                                    updated_data_route.append(updated_line)
                                else:
                                    updated_data_route.append(line)
                            ft=open(f"{route_change}_{y}_{date}.txt","w")
                            ft.writelines(updated_data_route)
                            ft.close()
                            
                            
                            break
                        
            updated_data_route.clear()       

    if error==0:
        print(Fore.RED + "\nNO SUCH BOOKING FOUND" + Style.RESET_ALL)
        print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
        cancel_booking(y,user_id)
    else:
     f = open(file_name, "w") 
      
     f.writelines(updated_data)  
     f.close()  
     print(Fore.GREEN + f"\n{upper_case} BOOKING CANCELLED" + Style.RESET_ALL)
     print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
     user_start(user_id)       
           

from datetime import datetime, timedelta

def calculate_time_difference(source_time, destination_time):
    # Define the time format
    time_format = "%H:%M"

    # Convert string times to datetime objects
    source_time_obj = datetime.strptime(source_time, time_format)
    destination_time_obj = datetime.strptime(destination_time, time_format)

    # If destination time is earlier than source time, assume it's on the next day
    if destination_time_obj < source_time_obj:
        destination_time_obj += timedelta(days=1)

    # Calculate the time difference
    time_difference = destination_time_obj - source_time_obj

    # Extract hours, minutes, and seconds
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds // 60) % 60
    

    # Format time with leading zeros if necessary
    formatted_time = f"{hours:02}:{minutes:02}"
    return formatted_time






def mode_book(y,z,user_id):
    date=input("\nENTER THE TRAVELLING DATE(YYYY-MM-DD):")
    
    file_name = f"{y}_{z}_{date}.txt"
    if not os.path.exists(file_name):
        print(Fore.RED + "\nNO SUCH DATE AVAILABLE" + Style.RESET_ALL)
        print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
        mode_book(y,z,user_id)


    f = open(file_name, "r")
    data = f.readlines()
    f.close()
    print(Fore.CYAN + "\nCURRENT SCHEDULE:\n" + Style.RESET_ALL)
    for line in data:
        print(Fore.WHITE + line + Style.RESET_ALL, end='')
    booking_file_name=f"{user_id}_{z}_bookings.txt"
    fb=open(booking_file_name,"a")
    upper_case= z.upper()
    car_number_to_book_small=input(Fore.BLUE + f"\nENTER THE {upper_case} NUMBER TO BOOK:" + Style.RESET_ALL)
    car_number_to_book=car_number_to_book_small.upper()
    number_of_passengers=int(input(Fore.BLUE + "\nENTER THE NUMBER OF PASSENGERS:" + Style.RESET_ALL))
    passenger_name=[]
    age=[]
    ticket_number=[]
    for i in range(number_of_passengers):
        a=input(Fore.BLUE + f"\nENTER THE NAME OF PASSENGER {i+1}:" + Style.RESET_ALL)
        passenger_name.append(a)
        b=int(input(Fore.BLUE + f"ENTER THE AGE OF PASSENGER {i+1} :" + Style.RESET_ALL))
        age.append(b)
        ticket_number.append(generate_ticket_number())



    updated_data = []

    for line in data:
        if car_number_to_book in line and not line.startswith(upper_case):
                parts=line.strip().split()
                seats_left=int(parts[5])

                if seats_left>=number_of_passengers:
                    parts[5]=str(seats_left-number_of_passengers)
                    updated_line = f"{parts[0]:<18}{parts[1]:<18}{parts[2]:<22}{parts[3]:<16}{parts[4]:<16}{parts[5]:<10}\n"
                    updated_data.append(updated_line)
                else:
                    print(Fore.RED + "\nNOT ENOUGH SEATS AVAILABLE" + Style.RESET_ALL)
                    mode_book(y,z,user_id)
        else:
            updated_data.append(line)
        
    f= open(file_name, "w")
    f.writelines(updated_data)
    f.close()
    
    
    
    
    
    error=0
    for line in data:
        if car_number_to_book in line:
          for i in range(number_of_passengers):
            parts_new=line.strip().split()
            new_line=parts_new[0:4]
            new_line.append(parts_new[4])
            new_line.append(parts_new[5])
            new_line.append(passenger_name[i].upper())
            new_line.append(str(age[i]))
            new_line.append(str(ticket_number[i]))
            fb.write(f"{new_line[0]:<18} {new_line[1]:<18} {new_line[2]:<18} {new_line[3]:<16} {new_line[6][:15]:<22} {new_line[7]:<10} {new_line[8]:<15} {date}\n")
            error=1
    ticket_number.clear()
    if error==0:
        print(Fore.RED + f"\nNO SUCH {upper_case} NUMBER FOUND" + Style.RESET_ALL)
        fb.close()
        print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
        mode_book(y,z,user_id)
    else:
     print(Fore.GREEN + "\nTICKET BOOKED" + Style.RESET_ALL)
     print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
     fb.close()
     user_start(user_id)
     
     
     
     
     
     

def add_mode(y,z):
    file_name = f"{y}_{z}.txt"
    
    f = open(file_name, "a")
    upper_case= z.upper()
    
    
    car_number_SMALL = input(Fore.BLUE + f"\nENTER THE {upper_case} NUMBER: " + Style.RESET_ALL)
    car_number=car_number_SMALL.upper()
    car_time = input(Fore.BLUE + "\nENTER THE SOURCE TIME(HH:MM): " + Style.RESET_ALL)
    car_destination = input(Fore.BLUE + "\nENTER THE DESTINATION TIME(HH:MM): " + Style.RESET_ALL)
    total_seats = int(input(Fore.BLUE + "\nENTER THE TOTAL SEATS: " + Style.RESET_ALL))
    vacant_seats=total_seats
    time_difference=calculate_time_difference(car_time,car_destination)
    
    # f.write(car_number,"     ",car_time,"     ",car_destination)       (this is wrong)
    f.write(f"{car_number}              {car_time}              {car_destination}                {time_difference}          {total_seats:<3}             {vacant_seats:<3}\n")
    f.close() 

    create_60_days_files(y,z)
    
    print(Fore.GREEN + f"\n{upper_case} DETAILS UPDATED" + Style.RESET_ALL)
    print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
    admin_start()
    
    
    
    

def edit_mode(y,z):
    file_name = f"{y}_{z}.txt"
    
    
    f = open(file_name, "r")  
    data = f.readlines()  
    f.close()  
    
    print(Fore.CYAN + "\nCURRENT SCHEDULE:\n" + Style.RESET_ALL)
    for line in data:
        print(Fore.WHITE + line + Style.RESET_ALL, end='')
    upper_case= z.upper()
    
    car_number_to_edit_small = input(Fore.BLUE + f"\nENTER THE {upper_case} NUMBER TO EDIT: " + Style.RESET_ALL)
    car_number_to_edit=car_number_to_edit_small.upper()
    error=0
    updated_data = []
    for line in data:
        if car_number_to_edit in line:
            error=1
            parts=line.strip().split()
            source_time = input(Fore.BLUE + "\nENTER THE NEW SOURCE TIME: " + Style.RESET_ALL)
            destination_time = input(Fore.BLUE + "\nENTER THE NEW DESTINATION TIME: " + Style.RESET_ALL)
            time_difference=calculate_time_difference(source_time,destination_time)

            updated_data.append(f"{car_number_to_edit}              {source_time}              {destination_time}                {time_difference}          {parts[4]:<3}             {parts[5]:<3}\n")
        else:
            updated_data.append(line)
    if error==0:
        print(Fore.RED + f"\nNO SUCH {upper_case} NUMBER FOUND" + Style.RESET_ALL)
        edit_mode(y,z)
    else:    
     f = open(file_name, "w")  
     f.writelines(updated_data)  
     f.close() 
     create_60_days_files(y,z)
     print(Fore.GREEN + "\nSCHEDULE UPDATED" + Style.RESET_ALL)
     print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
     admin_start()
     

def remove_mode(y,z):
    file_name = f"{y}_{z}.txt"
    
    
    f = open(file_name, "r")  
    data = f.readlines()  
    f.close()  
    
    print(Fore.CYAN + "\nCURRENT SCHEDULE:\n" + Style.RESET_ALL)
    for line in data:
        print(Fore.WHITE + line + Style.RESET_ALL, end='')
    upper_case= z.upper()
    
    car_number_to_remove_small = input(Fore.RED + f"\nENTER THE {upper_case} NUMBER TO REMOVE: " + Style.RESET_ALL)
    car_number_to_remove=car_number_to_remove_small.upper()
    updated_data = []
    error=0
    for line in data:
        if car_number_to_remove not in line:
            updated_data.append(line)
        else:
            error=1
    if error==0:
        print(Fore.RED + f"\nNO SUCH {upper_case} NUMBER FOUND" + Style.RESET_ALL)
        print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
        remove_mode(y,z)
    else:
     f = open(file_name, "w")  
     f.writelines(updated_data)  
     f.close()  

     create_60_days_files(y,z)

     print(Fore.GREEN + f"\n{upper_case} REMOVED" + Style.RESET_ALL)
     print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
     admin_start()
     
     
     
     

def intro():
    daily_run()
    print(Fore.CYAN + "\nWELCOME TO SAFAR" + Style.RESET_ALL)
    starting_choice=int(input((Fore.BLUE + "\n1.USER\n2.ADMIN\nENTER YOUR CHOICE:" + Style.RESET_ALL)))
    if starting_choice==1:
        print(Fore.GREEN + "\nWELCOME TO USER MODE" + Style.RESET_ALL)
        print(Fore.BLUE + "\nARE YOU A NEW USER?" + Style.RESET_ALL)
        new_user=int(input(Fore.BLUE + "\n1.YES\n2.NO\nENTER YOUR CHOICE:" + Style.RESET_ALL))
    
        if new_user==1:
            add_account()
        elif new_user==2:
           user_id=input(Fore.BLUE + "\nPLEASE ENTER YOUR USER NAME:" + Style.RESET_ALL)
           user_password=(input(Fore.BLUE + "\nPLEASE ENTER YOUR PASSWORD:" + Style.RESET_ALL))
           f=open("account.txt","r")
           data=f.readlines()
           f.close()
           check=0
           for line in data:
                  if user_id in line:
                    check=1
                    if user_password in line:
                        line = line.strip()
                        key, value = line.split('---->', 1)
                        key = key.strip()
                        value = value.strip()
                        if user_password==value:
                            print(Fore.GREEN + "\nWELCOME USER" + Style.RESET_ALL)
                            user_start(user_id)
                        else:       
                            print(Fore.RED + "\nWRONG PASSWORD" + Style.RESET_ALL)
                            intro()
                    else:
                        print(Fore.RED + "\nWRONG PASSWORD" + Style.RESET_ALL)
                        intro()
                        
                        
                        
           if check==0:
              print(Fore.RED + "\nNO SUCH USER NAME EXIST" + Style.RESET_ALL)
              intro()
                      
                              
    if starting_choice==2:
       print(Fore.GREEN + "\nWELCOME TO ADMIN MODE" + Style.RESET_ALL)
       admin_password=int(input(Fore.BLUE + "\nPLEASE ENTER YOUR PASSWORD:" + Style.RESET_ALL))
       if admin_password==5678:
           
           admin_start()
           
       else:
        print(Fore.RED + "\nWRONG PASSWORD" + Style.RESET_ALL)
        intro()
        
        
import os
import pygetwindow as gw
import time
import cv2

# Open the command prompt in a bigger size
os.system('mode con: cols=180 lines=50')

# Small delay to allow the window to open
time.sleep(1)  

# Get and maximize the window
try:
    window = gw.getWindowsWithTitle("C:\\Windows\\py.exe")[0]
    window.maximize()
except IndexError:
    print(Fore.RED + "Window not found. Try running the script again." + Style.RESET_ALL)

def display_image(image_path, window_name):
    image = cv2.imread(image_path)
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, image)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Display the first image
image_path1 = r"C:\Users\Shyam Sharma\Downloads\final_logo.webp"
display_image(image_path1, "Safar Logo")

# Wait for a key press and close the first window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Display the second image
image_path2 = r"C:\Users\Shyam Sharma\Downloads\logo_name.webp"
display_image(image_path2, "Logo Name")

# Wait for a key press and close the second window
cv2.waitKey(0)
cv2.destroyAllWindows()

import os
import pygetwindow as gw
import time

# Open the command prompt in a bigger size
os.system('mode con: cols=180 lines=50')

# Small delay to allow the window to open
time.sleep(1)  

# Get and maximize the window
try:
    window = gw.getWindowsWithTitle("C:\\Windows\\py.exe")[0]  # Adjust this based on the window title
    window.maximize()
except IndexError:
    print("Window not found. Try running the script again.")
        
        
        

def add_account():
    f=open("account.txt","a")
    f.close()

    f=open("account.txt","r")  
    data=f.readlines()
    f.close()

    user_name=input(Fore.BLUE + "\nENTER YOUR USER NAME:" + Style.RESET_ALL)

    for line in data:
        if user_name in line:
            print(Fore.RED + "\nTHE USER NAME IS ALREADY REGISTERED" + Style.RESET_ALL)
            print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
            add_account()

        else:
            f=open("account.txt","a")
            user_password=(input(Fore.BLUE + "ENTER YOUR PASSWORD:" + Style.RESET_ALL))
            f.write(f"{user_name}---->{user_password}\n")

            f.close()
            
            f=open(f"{user_name}_car_bookings.txt","a")
            f.close()
            f=open(f"{user_name}_train_bookings.txt","a")
            f.close()
            f=open(f"{user_name}_bus_bookings.txt","a")
            f.close()
            f=open(f"{user_name}_flight_bookings.txt","a")
            f.close()

            print(Fore.GREEN + "\nACCOUNT CREATED SUCCESSFULLY" + Style.RESET_ALL)
            print(Fore.YELLOW + "\n***********************************************************\n" + Style.RESET_ALL)
            intro()




intro()



#DO CAR NUMBER FORMAT LIKE CR___
