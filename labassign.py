class Process:
    def __init__(self, pid, process_name, start_time, priority):
        self.pid = pid
        self.process_name = process_name
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sort_by_pid(self):
        self.processes.sort(key=lambda x: x.pid)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda x: x.start_time)

    def sort_by_priority(self):
        priority_order = {'Low': 0, 'MID': 1, 'High': 2}
        self.processes.sort(key=lambda x: priority_order[x.priority])

    def display(self):
        print("{:<5} {:<10} {:<15} {:<8}".format("P_ID", "Process", "Start Time", "Priority"))
        print("=" * 40)
        for process in self.processes:
            print("{:<5} {:<10} {:<15} {:<8}".format(process.pid, process.process_name, process.start_time, process.priority))

def main():
    flight_table = FlightTable()

    flight_table.add_process(Process("P1", "VSCode", 100, "MID"))
    flight_table.add_process(Process("P23", "Eclipse", 234, "MID"))
    flight_table.add_process(Process("P93", "Chrome", 189, "High"))
    flight_table.add_process(Process("P42", "JDK", 9, "High"))
    flight_table.add_process(Process("P9", "CMD", 7, "High"))
    flight_table.add_process(Process("P87", "NotePad", 23, "Low"))

    while True:
        print("\nChoose sorting parameter:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            flight_table.sort_by_pid()
        elif choice == '2':
            flight_table.sort_by_start_time()
        elif choice == '3':
            flight_table.sort_by_priority()
        else:
            print("Invalid choice. Exiting...")
            break

        flight_table.display()

if __name__ == "__main__":
    main()

