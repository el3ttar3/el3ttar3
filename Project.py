import tkinter as tk
import webbrowser
from Functions import*
root = tk.Tk()

class TransportationGUI:

    def choose_car(self):
        # Make the page disappear when click on a button
        self.No.pack_forget()
        self.Yes.pack_forget()
        self.Que.pack_forget()
        self.label.pack_forget()
        self.car_button.pack_forget()
        self.bus_button.pack_forget()
        self.taxi_button.pack_forget()
        # Add a text to the screen
        Car = tk.Label(root, text="Choose your start destination: ", pady=10)
        Car.pack()
        # Create a list of options
        optionsCar = ["Octoper", "Nasr City", "El-Haram", "El-Tgamo3 El5ames", "Zamalek", "El-Rehab", "Maadi", "El-Sheikh Zayed", "Shobra", "Masr ElGadida", "El-Mokatam", "Giza"]

        # Create a StringVar object to hold the selected option
        selected_option = tk.StringVar()

        # Create a dropdown menu
        dropdown = tk.OptionMenu(root, selected_option, *optionsCar)
        dropdown.pack(padx=30)

        Car1 = tk.Label(root, text="Choose your final destination: ", pady=10)
        Car1.pack()
        optionsCar1 = ["Octoper", "Nasr City", "El-Haram", "El-Tgamo3 El5ames", "Zamalek", "El-Rehab", "Maadi", "El-Sheikh Zayed", "Shobra", "Masr ElGadida", "El-Mokatam", "Giza"]

        # Create a StringVar object to hold the selected option
        selected_option1 = tk.StringVar()

        # Create a dropdown menu
        dropdown1 = tk.OptionMenu(root, selected_option1, *optionsCar1)
        dropdown1.pack(padx=30)
        Lab = tk.Label(root, text="Enter departure time in HH:MM")
        Lab.pack(pady=10)
        e = tk.Entry(root)
        e.pack()

        def CalcCar():

            if (len(e.get()) != 5) or (e.get()[2] != ':') or (not e.get()[:2].isdigit()) or (not e.get()[3:].isdigit()) or (not (0 <= int(e.get()[:2]) < 24)) or (not (0 <= int(e.get()[3:]) < 60)):
                labal = tk.Label(root, text="Invalid input: time must be in the format HH:MM\n Rerun the program")
                labal.pack()
            else:
                if selected_option1.get() == selected_option.get():
                    Fals = tk.Label(root, text="Wrong data, the destinations are the same, Rerun the program")
                    Fals.pack()
                else:
                    KM = distance(selected_option.get(), selected_option1.get())
                    Start_Time_Car = e.get()
                    Format = TimeFormat(Start_Time_Car) #return tuble (x, y)
                    Convert = H_Converter(Format[0], Format[1])
                    Time = TripTime(KM, 65)
                    Convert_Time = H_Converter(Time[0], Time[1])
                    Arrive_Time = Convert + Convert_Time
                    minutes = (Arrive_Time % 1) * 60
                    Hours = ((Arrive_Time * 60) - minutes) / 60
                    ArrReformat = TimeReform(int(Hours), int(minutes))
                    Cost = int(TripCostC(KM))
                    Toxic = Toxicity(KM, 65)
                    Label_Calc = tk.Label(root, text=f"The trip time is {Time[0]} hours and {Time[1]} minutes\n The cost of consumed fuel is {Cost} pounds\n The arrival time is {ArrReformat}\nThe amount of carbon dioxide emission\n that harm the enviroment is %4.2f "%Toxic)
                    Label_Calc.pack()

        btnCar = tk.Button(root, text="Submit", command=CalcCar, pady=5)
        btnCar.pack()


    def choose_bus(self):
        self.No.pack_forget()
        self.Yes.pack_forget()
        self.Que.pack_forget()
        self.label.pack_forget()
        self.car_button.pack_forget()
        self.bus_button.pack_forget()
        self.taxi_button.pack_forget()

        lbel = tk.Label(root, text="*NOTE* The trip cost for any destination is 10 pounds")
        lbel.pack(pady=10)
        Bus = tk.Label(root, text="Choose your start destination: ", pady=10)
        Bus.pack()
        # Create a list of options
        optionsBus = ["Octoper", "Nasr City", "El-Haram", "El-Tgamo3 El5ames", "Zamalek", "El-Rehab", "Maadi", "El-Sheikh Zayed", "Shobra", "Masr ElGadida", "El-Mokatam", "Giza"]

        # Create a StringVar object to hold the selected option
        selected_optionBus = tk.StringVar()

        # Create a dropdown menu
        dropdownBus = tk.OptionMenu(root, selected_optionBus, *optionsBus)
        dropdownBus.pack(padx=30)

        Bus1 = tk.Label(root, text="Choose your final destination: ", pady=10)
        Bus1.pack()
        optionsBus1 = ["Octoper", "Nasr City", "El-Haram", "El-Tgamo3 El5ames", "Zamalek", "El-Rehab", "Maadi", "El-Sheikh Zayed", "Shobra", "Masr ElGadida", "El-Mokatam", "Giza"]

        # Create a StringVar object to hold the selected option
        selected_optionBus1 = tk.StringVar()

        # Create a dropdown menu
        dropdownBus1 = tk.OptionMenu(root, selected_optionBus1, *optionsBus1)
        dropdownBus1.pack(padx=30)
        LabB = tk.Label(root, text="Enter departure time in HH:MM")
        LabB.pack(pady=10)
        eBus = tk.Entry(root)
        eBus.pack()



        def calcBus():
            SBus1 = selected_optionBus.get()
            SBus2 = selected_optionBus1.get()

            if SBus1 == SBus2:
                FalsBus = tk.Label(root, text="Wrong data, the destinations are the same\nPlease rerun the program")
                FalsBus.pack()
            else:
                KMBus = distance(selected_optionBus.get(), selected_optionBus1.get())
                Start_Time_Bus = eBus.get()
                FormatBus = TimeFormat(Start_Time_Bus)
                ConvertBus = H_Converter(FormatBus[0], FormatBus[1])
                trip_time = TripTime(KMBus, 65)
                Convert_Time_Bus = H_Converter(trip_time[0], trip_time[1])
                Arrive_Time_Bus = ConvertBus + Convert_Time_Bus
                minutesBus = (Arrive_Time_Bus % 1) * 60
                HoursBus = ((Arrive_Time_Bus * 60) - minutesBus) / 60
                Arr_Reformat_Bus = TimeReform(int(HoursBus), int(minutesBus))
                Toxic_Bus = (Toxicity(KMBus, 65)) + 0.2
                Label_Calc_Bus = tk.Label(root, text=f"The trip time is {trip_time[0]} hours and {trip_time[1]} minutes\n The arrival time is {Arr_Reformat_Bus}\nThe amount of carbon dioxide emission\n that harm the enviroment is %4.2f "%Toxic_Bus)
                Label_Calc_Bus.pack()


        btnBus = tk.Button(root, text="Submit", command=calcBus, pady=5)
        btnBus.pack()


    def choose_taxi(self):

        # Make the page disappear when click on a button
        self.No.pack_forget()
        self.Yes.pack_forget()
        self.Que.pack_forget()
        self.label.pack_forget()
        self.car_button.pack_forget()
        self.bus_button.pack_forget()
        self.taxi_button.pack_forget()
        # Add a text to the screen
        Taxi = tk.Label(root, text="Choose your start destination: ", pady=10)
        Taxi.pack()
        # Create a list of options
        optionsTaxi = ["Octoper", "Nasr City", "El-Haram", "El-Tgamo3 El5ames", "Zamalek", "El-Rehab", "Maadi", "El-Sheikh Zayed", "Shobra", "Masr ElGadida", "El-Mokatam", "Giza"]

        # Create a StringVar object to hold the selected option
        selected_optionTaxi = tk.StringVar()

        # Create a dropdown menu
        dropdownTaxi = tk.OptionMenu(root, selected_optionTaxi, *optionsTaxi)
        dropdownTaxi.pack(padx=30)

        Taxi1 = tk.Label(root, text="Choose your final destination: ", pady=10)
        Taxi1.pack()
        optionsTaxi1 = ["Octoper", "Nasr City", "El-Haram", "El-Tgamo3 El5ames", "Zamalek", "El-Rehab", "Maadi", "El-Sheikh Zayed", "Shobra", "Masr ElGadida", "El-Mokatam", "Giza"]

        # Create a StringVar object to hold the selected option
        selected_optionTaxi1 = tk.StringVar()

        # Create a dropdown menu
        dropdownTaxi1 = tk.OptionMenu(root, selected_optionTaxi1, *optionsTaxi1)
        dropdownTaxi1.pack(padx=30)
        LabTaxi = tk.Label(root, text="Enter departure time in HH:MM")
        LabTaxi.pack(pady=10)
        eTaxi = tk.Entry(root)
        eTaxi.pack()

        def calcTaxi():
            ST1 = selected_optionTaxi.get()
            ST2 = selected_optionTaxi1.get()
            e2 = eTaxi.get()
            if (len(eTaxi.get()) != 5) or (eTaxi.get()[2] != ':') or (not eTaxi.get()[:2].isdigit()) or (not eTaxi.get()[3:].isdigit()) or (not (0 <= int(eTaxi.get()[:2]) < 24)) or (not (0 <= int(eTaxi.get()[3:]) < 60)):
                labelTaxi = tk.Label(root, text="Invalid input: time must be in the format HH:MM\n Rerun the program")
                labelTaxi.pack()
            else:
                if ST1 == ST2:
                    FalsTaxi = tk.Label(root, text="Wrong data, the destinations are the same, Rerun the program")
                    FalsTaxi.pack()
                else:
                    KMTaxi = distance(selected_optionTaxi.get(), selected_optionTaxi1.get())
                    Start_Time_Taxi = eTaxi.get()
                    Format_Taxi = TimeFormat(Start_Time_Taxi)
                    Convert_Taxi = H_Converter(Format_Taxi[0], Format_Taxi[1])
                    Time_Taxi = TripTime(KMTaxi, 65)
                    Convert_Time_Taxi = H_Converter(Time_Taxi[0], Time_Taxi[1])
                    Arrive_Time_Taxi = Convert_Taxi + Convert_Time_Taxi
                    minutesTaxi = (Arrive_Time_Taxi % 1) * 60
                    HoursTaxi = ((Arrive_Time_Taxi * 60) - minutesTaxi) / 60
                    ArrReformatTaxi = TimeReform(int(HoursTaxi), int(minutesTaxi))
                    Cost_Taxi = int((TripCostC(KMTaxi)) + 20)
                    Toxic_Taxi = Toxicity(KMTaxi, 65)
                    Label_Calc_Taxi = tk.Label(root, text=f"The trip time is {Time_Taxi[0]} hours and {Time_Taxi[1]} minutes\n The trip cost is {Cost_Taxi} pounds\n The arrival time is {ArrReformatTaxi}\nThe amount of carbon dioxide emission\n that harm the enviroment is %4.2f "%Toxic_Taxi)
                    Label_Calc_Taxi.pack()



        btnCar = tk.Button(root, text="Submit", command=calcTaxi, pady=5)
        btnCar.pack()


    def __init__(self, master):
        # make the title
        self.master = master
        master.title("Lucida")
        master.geometry("400x400")

        def disable(button):
            button.config(state='disable')

        def enable_button(button):
            button.config(state='normal')




        # Make the buttons of car and bus and taxi
        self.Que = tk.Label(root, text="Do you have a car?")
        self.Que.pack()
        self.car_button = tk.Button(master, text="Car", command=self.choose_car, padx=10, pady=3)
        self.Yes = tk.Button(root, text="Yes", command=lambda: enable_button(self.car_button))
        self.No = tk.Button(root, text="No", command=lambda: disable(self.car_button))
        self.Yes.pack()
        self.No.pack()
        self.label = tk.Label(master, text="Choose your transportation mode:")
        self.label.pack(pady=15)
        self.car_button.pack(padx=20, pady=6)

        self.bus_button = tk.Button(master, text="Bus", command=self.choose_bus, padx=10, pady=3)
        self.bus_button.pack(padx=20, pady=6)

        self.taxi_button = tk.Button(master, text="Taxi", command=self.choose_taxi, padx=10, pady=3)
        self.taxi_button.pack(padx=20, pady=6)


my_gui = TransportationGUI(root)
root.mainloop()
