class FlightTable:
    def _init_(self):
        self.data = []

    def add_entry(self, p_id, process, start_time, priority):
        self.data.append({'P_ID': p_id, 'Process': process, 'Start Time': start_time, 'Priority': priority})

    def bubble_sort(self, key):
        n = len(self.data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.data[j][key] > self.data[j + 1][key]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

    def print_table(self):
        print("{:<5} {:<10} {:<15} {:<10}".format("P_ID", "Process", "Start Time", "Priority"))
        print("="*40)
        for entry in self.data:
            print("{:<5} {:<10} {:<15} {:<10}".format(entry['P_ID'], entry['Process'], entry['Start Time'], entry['Priority']))

flight_table = FlightTable()
flight_table.add_entry("P1", "VSCode", 100, "MID")
flight_table.add_entry("P23", "Eclipse", 234, "MID")
flight_table.add_entry("P93", "Chrome", 189, "High")
flight_table.add_entry("P42", "JDK", 9, "High")
flight_table.add_entry("P9", "CMD", 7, "High")
flight_table.add_entry("P87", "NotePad", 23, "Low")

while True:
    print("\nSorting Options:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    print("4. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        flight_table.bubble_sort('P_ID')
    elif choice == 2:
        flight_table.bubble_sort('Start Time')
    elif choice == 3:
        flight_table.bubble_sort('Priority')
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please enter a valid option.")

    flight_table.print_table()

