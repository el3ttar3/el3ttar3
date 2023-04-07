import webbrowser

def distance(initial, end):
    if (initial == "Octoper" and end == "Nasr City") or (initial == "Nasr City" and end == "Octoper"):
        return 70.3
    elif (initial == "Octoper" and end == "El-Haram") or (initial == "El-Haram" and end == "Octoper"):
        return 11.4
    elif (initial == "Octoper" and end == "El-Tgamo3 El5ames") or (initial == "El-Tgamo3 El5ames" and end == "Octoper"):
        return 70.2
    elif (initial == "Octoper" and end == "Zamalek") or (initial == "Zamalek" and end == "Octoper"):
        return 54.0
    elif (initial == "Octoper" and end == "El-Rehab") or (initial == "El-Rehab" and end == "Octoper"):
        return 81.8
    elif (initial == "Octoper" and end == "Maadi") or (initial == "Maadi" and end == "Octoper"):
        return 52.6
    elif (initial == "Octoper" and end == "El-Sheikh Zayed") or (initial == "El-Sheikh Zayed" and end == "Octoper"):
        return 22.4
    elif (initial == "Octoper" and end == "Shobra") or (initial == "Shobra" and end == "Octoper"):
        return 44
    elif (initial == "Octoper" and end == "Masr ElGadida") or (initial == "Masr ElGadida" and end == "Octoper"):
        return 25.4
    elif (initial == "Octoper" and end == "El-Mokatam") or (initial == "El-Mokatam" and end == "Octoper"):
        return 66.1
    elif (initial == "Octoper" and end == "Giza") or (initial == "Giza" and end == "Octoper"):
        return 25.4
    elif (initial == "Nasr City" and end == "El-Haram") or (initial == "El-Haram" and end == "Nasr City"):
        return 19.8
    elif (initial == "Nasr City" and end == "El-Tgamo3 El5ames") or (initial == "El-Tgamo3 El5ames" and end == "Nasr City"):
        return 45.4
    elif (initial == "Nasr City" and end == "Zamalek") or (initial == "Zamalek" and end == "Nasr City"):
        return 14.2
    elif (initial == "Nasr City" and end == "El-Rehab") or (initial == "El-Rehab" and end == "Nasr City"):
        return 23.4
    elif (initial == "Nasr City" and end == "Maadi") or (initial == "Maadi" and end == "Nasr City"):
        return 25.4
    elif (initial == "Nasr City" and end == "El-Sheikh Zayed") or (initial == "El-Sheikh Zayed" and end == "Nasr City"):
        return 46.6
    elif (initial == "Nasr City" and end == "Shobra") or (initial == "Shobra" and end == "Nasr City"):
        return 37.4
    elif initial == "Nasr City" and end == "Masr ElGadida" or initial == "Masr ElGadida" and end == "Nasr City":
        return 10.9
    elif initial == "Nasr City" and end == "El-Mokatam" or initial == "El-Mokatam" and end == "Nasr City":
        return 8.9
    elif initial == "Nasr City" and end == "Giza" or initial == "Giza" and end == "Nasr City":
        return 18.9
    elif initial == "El-Haram" and end == "El-Tgamo3 El5ames" or initial == "El-Tgamo3 El5ames" and end == "El-Haram":
        return 43.1
    elif initial == "El-Haram" and end == "Zamalek" or initial == "Zamalek" and end == "El-Haram":
        return 19.8
    elif initial == "El-Haram" and end == "El-Rehab" or initial == "El-Rehab" and end == "El-Haram":
        return 20.6
    elif initial == "El-Haram" and end == "Maadi" or initial == "Maadi" and end == "El-Haram":
        return 15
    elif initial == "El-Haram" and end == "El-Sheikh Zayed" or initial == "El-Sheikh Zayed" and end == "El-Haram":
        return 19.8
    elif initial == "El-Haram" and end == "Shobra" or initial == "Shobra" and end == "El-Haram":
        return 15.8
    elif initial == "El-Haram" and end == "Masr ElGadida" or initial == "Masr ElGadida" and end == "El-Haram":
        return 24.9
    elif initial == "El-Haram" and end == "El-Mokatam" or initial == "El-Mokatam" and end == "El-Haram":
        return 16.7
    elif initial == "El-Haram" and end == "Giza" or initial == "Giza" and end == "El-Haram":
        return 4.1
    elif initial == "El-Tgamo3 El5ames" and end == "Zamalek" or initial == "Zamalek" and end == "El-Tgamo3 El5ames":
        return 24
    elif initial == "El-Tgamo3 El5ames" and end == "El-Rehab" or initial == "El-Rehab" and end == "El-Tgamo3 El5ames":
        return 13.8
    elif initial == "El-Tgamo3 El5ames" and end == "Maadi" or initial == "Maadi" and end == "El-Tgamo3 El5ames":
        return 23.4
    elif initial == "El-Tgamo3 El5ames" and end == "El-Sheikh Zayed" or initial == "El-Sheikh Zayed" and end == "El-Tgamo3 El5ames":
        return 56.6
    elif initial == "El-Tgamo3 El5ames" and end == "Shobra" or initial == "Shobra" and end == "El-Tgamo3 El5ames":
        return 26.3
    elif initial == "El-Tgamo3 El5ames" and end == "Masr ElGadida" or initial == "Masr ElGadida" and end == "El-Tgamo3 El5ames":
        return 25.8
    elif initial == "El-Tgamo3 El5ames" and end == "El-Mokatam" or initial == "El-Mokatam" and end == "El-Tgamo3 El5ames":
        return 15.7
    elif initial == "El-Tgamo3 El5ames" and end == "Giza" or initial == "Giza" and end == "El-Tgamo3 El5ames":
        return 27.2
    elif initial == "Zamalek" and end == "El-Rehab" or initial == "El-Rehab" and end == "Zamalek":
        return 33.2
    elif initial == "Zamalek" and end == "Maadi" or initial == "Maadi" and end == "Zamalek":
        return 15.3
    elif initial == "Zamalek" and end == "El-Sheikh Zayed" or initial == "El-Sheikh Zayed" and end == "Zamalek":
        return 31.3
    elif initial == "Zamalek" and end == "Shobra" or initial == "Shobra"and end == "Zamalek":
        return 10
    elif initial == "Zamalek" and end == "Masr ElGadida" or initial == "Masr ElGadida" and end == "Zamalek":
        return 17.3
    elif initial == "Zamalek" and end == "El-Mokatam" or initial == "El-Mokatam" and end == "Zamalek":
        return 15.3
    elif initial == "Zamalek" and end == "Giza" or initial == "Giza" and end == "Zamalek":
        return 7.8
    elif initial == "El-Rehab" and end == "Maadi" or initial == "Maadi" and end == "El-Rehab":
        return 39.6
    elif initial == "El-Rehab" and end == "El-Sheikh Zayed" or initial == "El-Sheikh Zayed" and end == "El-Rehab":
        return 71
    elif initial == "El-Rehab" and end == "Shobra" or initial == "Shobra" and end == "El-Rehab":
        return 28.7
    elif initial == "El-Rehab" and end == "Masr ElGadida" or initial == "Masr ElGadida" and end == "El-Rehab":
        return 18.9
    elif initial == "El-Rehab" and end == "El-Mokatam" or initial == "El-Mokatam" and end == "El-Rehab":
        return 27
    elif initial == "El-Rehab" and end == "Giza" or initial == "Giza" and end == "El-Rehab":
        return 40.9
    elif initial == "Maadi" and end == "El-Sheikh Zayed" or initial == "El-Sheikh Zayed" and end == "Maadi":
        return 41.1
    elif initial == "Maadi" and end == "Shobra" or initial == "Shobra" and end == "Maadi":
        return 23.4
    elif initial == "Maadi" and end == "Masr ElGadida" or initial == "Masr ElGadida" and end == "Maadi":
        return 27.1
    elif initial == "Maadi" and end == "El-Mokatam" or initial == "El-Mokatam" and end == "Maadi":
        return 17.6
    elif initial == "Maadi" and end == "Giza" or initial == "Giza" and end == "Maadi":
        return 11
    elif initial == "El-Sheikh Zayed" and end == "Shobra" or initial == "Shobra" and end == "El-Sheikh Zayed":
        return 35.8
    elif initial == "El-Sheikh Zayed" and end == "Masr ElGadida" or initial == "Masr ElGadida" and end == "El-Sheikh Zayed":
        return 45.1
    elif initial == "El-Sheikh Zayed" and end == "El-Mokatam" or initial == "El-Mokatam" and end == "El-Sheikh Zayed":
        return 48.5
    elif initial == "El-Sheikh Zayed" and end == "Giza" or initial == "Giza" and end == "El-Sheikh Zayed":
        return 36
    elif initial == "Shobra" and end == "Masr ElGadida" or initial == "Masr ElGadida" and end == "Shobra":
        return 12.5
    elif initial == "Shobra" and end == "El-Mokatam" or initial == "El-Mokatam" and end == "Shobra":
        return 18.6
    elif initial == "Shobra" and end == "Giza" or initial == "Giza" and end == "Shobra":
        return 25.8
    elif initial == "Masr ElGadida" and end == "El-Mokatam" or initial == "El-Mokatam" and end == "Masr ElGadida":
        return 19.5
    elif initial == "Masr ElGadida" and end == "Giza" or initial == "Giza" and end == "Masr ElGadida":
        return 23.1
    elif initial == "El-Mokatam" and end == "Giza" or initial == "Giza" and end == "El-Mokatam":
        return 19
def TripTime(distance, speed=65):
    hours = distance / speed
    minutes = (hours % 1) * 60
    return int(hours), int(minutes)

def TimeFormat(time_str):
    hour, minute = time_str.split(":")
    return int(hour), int(minute)

def TimeReform(hours, minutes):
    return f"{hours:02d}:{minutes:02d}"

def TripCostC(distance):
    Set = 0.28
    Cost = distance * Set
    return Cost

def Toxicity(dist, speed=65):
    Fuel = dist / 7
    emissions = Fuel * (0.003)
    return emissions

def H_Converter(h, m):
    Convert = (m / 60) + h
    return Convert

def play_List():
    happy = False
    energetic = False
    calm = False
    sad = False


    # ask the user a series of true or false questions to determine their mood
    happy = input("Are you feeling happy? (yes/no) ").lower() == "yes"
    if happy:
        print("Here are some happy songs to cheer you up:")
        webbrowser.open("https://www.youtube.com/watch?v=d-diB65scQU")
        webbrowser.open("https://www.youtube.com/watch?v=ru0K8uYEZWw")
        webbrowser.open("https://www.youtube.com/watch?v=4fndeDfaWCg")
        webbrowser.open("https://www.youtube.com/watch?v=y6Sxv-sUYtM")
        webbrowser.open("https://www.youtube.com/watch?v=E3Y3IMT3hic")
        return

    energetic = input("Are you feeling energetic? (yes/no) ").lower() == "yes"
    if energetic:
        print("Here are some energetic songs to get you pumped up:")
        webbrowser.open("https://www.youtube.com/watch?v=btPJPFnesV4")
        webbrowser.open("https://www.youtube.com/watch?v=3tmd-ClpJxA")
        webbrowser.open("https://www.youtube.com/watch?v=2zNSgSzhBfM")
        webbrowser.open("https://www.youtube.com/watch?v=eH3giaIzONA")
        webbrowser.open("https://www.youtube.com/watch?v=dK9C8eVpYcY")
        return

    calm = input("Are you feeling calm? (yes/no) ").lower() == "yes"
    if calm:
        print("Here are some calming songs to relax to:")
        webbrowser.open("https://www.youtube.com/watch?v=7wfYIMyS_dI")
        webbrowser.open("https://www.youtube.com/watch?v=JwYX52BP2Sk")
        webbrowser.open("https://www.youtube.com/watch?v=5ZF9ZBtG-5c")
        webbrowser.open("https://www.youtube.com/watch?v=y8AWFf7EAc4")
        webbrowser.open("https://www.youtube.com/watch?v=TwV_Uw8ZBwM")
        return

    sad = input("Are you feeling sad? (yes/no) ").lower() == "yes"
    if sad:
        print("Here are some sad songs to help you through your emotions:")
        webbrowser.open("https://www.youtube.com/watch?v=CxK7NKBc_YU")
        webbrowser.open("https://www.youtube.com/watch?v=3JWTaaS7LdU")
        webbrowser.open("https://www.youtube.com/watch?v=SmVAWKfJ4Go")
        webbrowser.open("https://www.youtube.com/watch?v=YQHsXMglC9A")
        webbrowser.open("https://www.youtube.com/watch?v=4N3N1MlvVc4")
        return
def disable(button):
            button.config(state='disable')

def enable_button(button):
            button.config(state='normal')

#def check():
    #if (len(e.get()) != 5) or (e.get()[2] != ':') or (not e.get()[:2].isdigit()) or (not e.get()[3:].isdigit()) or (not (0 <= int(e.get()[:2]) < 24)) or (not (0 <= int(e.get()[3:]) < 60)):
                #labal = tk.Label(root, text="Invalid input: time must be in the format HH:MM\n Rerun the program")
                #labal.pack()
