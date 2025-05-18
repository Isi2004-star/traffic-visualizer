import csv
from collections import Counter
from datetime import datetime
from graphics import *

# Author: Isiri Gangamini Jayaneththi
# Date: 09/12/2024
# Student ID: 20240577

# Task A: Input Validation
def validate_date_input():
    """
    Prompts the user for a date in DD MM YYYY format, validates the input for:
    - Correct data type
    - Correct range for day, month, and year
    """
    while True:
        # Validate day
        while True:
            try:
                day = int(input('Please enter the day of the survey in the format DD: '))
                if 1 <= day <= 31:
                    break
                else:
                    print('Out of range - values must be in the range 1 and 31.')
            except ValueError:
                print('Integer required!')

        # Validate month
        while True:
            try:
                month = int(input('Please enter the month of the survey in the format MM: '))
                if 1 <= month <= 12:
                    break
                else:
                    print('Out of range - values must be in the range 1 to 12.')
            except ValueError:
                print('Integer required!')

        # Validate year
        while True:
            try:
                year = int(input('Please enter the year of the survey in the format YYYY: '))
                if 2000 <= year <= 2024:
                    break
                else:
                    print('Out of range - values must range from 2000 and 2024.')
            except ValueError:
                print('Integer required!')

        # Return the formatted date
        return f"{day:02d}{month:02d}{year}"

# Task B: Processed Outcomes
def process_csv_data(file_path):
    """
    Processes the CSV data for the selected date and extracts:
    - Total vehicles
    - Total trucks
    - Total electric vehicles
    - Two-wheeled vehicles, and other requested metrics
    """
    # Initialize counters and data structures
    total_vehicles = 0
    total_trucks = 0
    total_electric_vehicles = 0
    total_two_wheeled_vehicles = 0
    total_busses_ElmAvenue_heading_north = 0
    total_vehicles_straight = 0
    total_vehicles_over_speed_limit = 0
    total_vehicles_through_ElmAvenue_RabbitRoad = 0
    total_vehicles_through_HanleyHighway_Westway = 0
    total_scooters_ElmAvenue_RabbitRoad = 0
    peak_hour_vehicles = Counter()
    rain_hours = set()
    bike_counts = Counter()

    traffic_data = {}

    try:
        # Open and read the CSV file
        with open(file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            
            # Validate headers
            expected_headers = [
                "JunctionName", "Date", "timeOfDay", "travel_Direction_in",
                "travel_Direction_out", "Weather_Conditions", "JunctionSpeedLimit",
                "VehicleSpeed", "VehicleType", "elctricHybrid"
            ]

            missing_headers = [header for header in expected_headers if header not in reader.fieldnames]
            if missing_headers:
                print(f"Missing headers: {', '.join(missing_headers)}")
                return
            
            # Extract and clean row data
            for row in reader:
                try:
                    # Extract and clean row data
                    junction = row['JunctionName'].strip().lower()
                    time_of_day = row['timeOfDay'].strip()
                    travel_direction_in = row['travel_Direction_in'].strip().upper()
                    travel_direction_out = row['travel_Direction_out'].strip().upper()
                    weather_conditions = row['Weather_Conditions'].strip().lower()
                    junction_speed_limit = float(row['JunctionSpeedLimit']) if row['JunctionSpeedLimit'] else 0
                    vehicle_speed = float(row['VehicleSpeed']) if row['VehicleSpeed'] else 0
                    vehicle_type = row['VehicleType'].strip().lower()
                    electric_hybrid = row['elctricHybrid'].strip().upper() == 'TRUE' if row['elctricHybrid'] else False
                    hour = int(time_of_day.split(':')[0])
                    
                    # Update counters based on conditions
                    total_vehicles += 1
                    if junction not in traffic_data:
                        traffic_data[junction] = Counter()
                    traffic_data[junction][hour] += 1

                    if vehicle_type == 'truck':
                        total_trucks += 1
                    if electric_hybrid:
                        total_electric_vehicles += 1
                    if vehicle_type in ['bicycle', 'motorcycle', 'scooter']:
                        total_two_wheeled_vehicles += 1
                    if vehicle_type == 'bicycle':
                        bike_counts[hour] += 1
                    if vehicle_type == 'scooter' and junction == 'elm avenue/rabbit road':
                        total_scooters_ElmAvenue_RabbitRoad += 1

                    if vehicle_speed > junction_speed_limit:
                        total_vehicles_over_speed_limit += 1

                    if junction == 'elm avenue/rabbit road':
                        total_vehicles_through_ElmAvenue_RabbitRoad += 1

                    if junction == 'hanley highway/westway':
                        total_vehicles_through_HanleyHighway_Westway += 1
                        peak_hour_vehicles[hour] += 1

                    if vehicle_type == 'buss' and junction == 'elm avenue/rabbit road' and travel_direction_in == 'N':
                        total_busses_ElmAvenue_heading_north += 1

                    if travel_direction_in == travel_direction_out:
                        total_vehicles_straight += 1

                    if 'rain' in weather_conditions:
                        rain_hours.add(hour)
                except ValueError:
                    continue
           
        # Calculate additional metrics
        percentage_of_trucks = round((total_trucks / total_vehicles) * 100) if total_vehicles else 0
        avg_bikes_per_hour = round(sum(bike_counts.values()) / len(bike_counts)) if bike_counts else 0
        max_vehicles = max(peak_hour_vehicles.values(), default=0)
        peak_hours = [hour for hour, count in peak_hour_vehicles.items() if count == max_vehicles]
        
        # Create output summary
        outcomes = f"""***************************
Data file selected: {file_path}
***************************
The total number of vehicles recorded for this date is {total_vehicles}
The total number of trucks recorded for this date is {total_trucks}
The total number of electric vehicles for this date is {total_electric_vehicles}
The total number of two-wheeled vehicles for this date is {total_two_wheeled_vehicles}
The total number of busses leaving Elm Avenue/Rabbit Road heading North is {total_busses_ElmAvenue_heading_north}
The total number of vehicles through both junctions not turning left or right is {total_vehicles_straight}
The percentage of total vehicles recorded that are trucks for this date is {percentage_of_trucks}%
The average number of bikes per hour for this date is {avg_bikes_per_hour}
The total number of vehicles recorded as over the speed limit for this date is {total_vehicles_over_speed_limit}
The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {total_vehicles_through_ElmAvenue_RabbitRoad}
The total number of vehicles recorded through Hanley Highway/Westway junction is {total_vehicles_through_HanleyHighway_Westway}
{int((total_scooters_ElmAvenue_RabbitRoad / total_vehicles_through_ElmAvenue_RabbitRoad) * 100)}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.
The highest number of vehicles in an hour on Hanley Highway/Westway is {max_vehicles}
The most vehicles through Hanley Highway/Westway were recorded between {peak_hours[0]}:00 and {int(peak_hours[0]) + 1}:00
The number of hours of rain for this date is {len(rain_hours)}
"""
        print(outcomes)
        save_results_to_file(outcomes)
        return traffic_data

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return {}

# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    try:
        # Open the file in append mode
        with open(file_name, 'a') as file:
             # Write the outcomes to the file
            file.write(outcomes)
    except Exception as e:
        # Handle any errors during the file write process
        print(f"Error writing to file: {e}")

# Task D: Histogram Visualization
class HistogramApp:
    def __init__(self, traffic_data, date):
        self.traffic_data = traffic_data
        # Format the date for display
        self.date = datetime.strptime(date, "%d%m%Y").strftime("%d/%m/%Y")
        # Create a graphical window for the histogram
        self.win = GraphWin(f"Histogram of Vehicle Frequency per Hour ({self.date})", 1500, 600)
        self.win.setBackground("white")

    def draw_histogram(self):
        bar_width = 16
        group_spacing = 10
        x_start = 30
        y_start = 500
        max_height = 300
        
        # Find the maximum count for scaling the histogram bars
        max_count = max(max(data.values()) for data in self.traffic_data.values())
        scale = max_height / max_count
        
        # Add a title to the histogram
        title = Text(Point(600, 20), f"Histogram of Vehicle Frequency per Hour ({self.date})")
        title.setSize(18)
        title.setStyle("bold")
        title.draw(self.win)
        
        # Get junction names and set bar colors
        junctions = list(self.traffic_data.keys())
        colors = ["green", "orange"]
        for hour in range(24):
            group_x_start = x_start + hour * (len(junctions) * (bar_width + 5) + group_spacing)
            for i, junction in enumerate(junctions):
                # Get the count for the current hour and junction
                count = self.traffic_data[junction].get(hour, 0)
                bar_height = count * scale
                x = group_x_start + i * bar_width
                
                # Get the count for the current hour and junction
                bar = Rectangle(Point(x, y_start - bar_height), Point(x + bar_width, y_start))
                bar.setFill(colors[i])
                bar.draw(self.win)
                
                # Add a label above the bar if count > 0
                if count > 0:
                    label = Text(Point(x + bar_width / 2, y_start - bar_height - 10), str(count))
                    label.setSize(8)
                    label.draw(self.win)
            
             # Add an hour label below the bars
            hour_label_x = group_x_start + (len(junctions) * (bar_width + 5)) / 2 - bar_width / 2
            hour_label = Text(Point(hour_label_x, y_start + 15), str(hour).zfill(2))
            hour_label.setSize(8)
            hour_label.draw(self.win)
            
        # Add a legend label
        legend_label = Text(Point(600, y_start + 40), "Hours 00:00 to 24:00")
        legend_label.setSize(10)
        legend_label.setStyle("bold")
        legend_label.draw(self.win)
        
        # Draw the legend
        self.draw_legend(junctions, colors)

    def draw_legend(self, junctions, colors):
        legend_start_x = 1000
        legend_start_y = 30
        legend_spacing = 25

        for i, junction in enumerate(junctions):
            # Draw the color box for each junction
            rect = Rectangle(Point(legend_start_x, legend_start_y + i * legend_spacing),
                             Point(legend_start_x + 15, legend_start_y + i * legend_spacing + 15))
            rect.setFill(colors[i])
            rect.draw(self.win)
            
            # Add the junction name next to the color box
            legend_text = Text(Point(legend_start_x + 100, legend_start_y + i * legend_spacing + 7.5), junction.title())
            legend_text.setSize(10)
            legend_text.draw(self.win)

    def run(self):
        self.draw_histogram()
        # Wait for a mouse click to close the window
        self.win.getMouse()
        self.win.close()

# Task E: MultiCSVProcessor
class MultiCSVProcessor:
    def __init__(self):
        self.current_data = None
        self.traffic_data = None
        self.date_input = None

    def load_csv_file(self):
        # Validate the date input from the user
        self.date_input = validate_date_input()
        # Construct the file path using the validated date
        file_path = f"C:/Users/ISIRI/Music/Music/course work sd/traffic_data{self.date_input}.csv"
        # Process the CSV data
        self.traffic_data = process_csv_data(file_path)

    def clear_previous_data(self):
        self.current_data = None
        self.traffic_data = None
        
    def handle_user_interaction(self):
        while True:
             # Load the data file
            self.load_csv_file()

            if self.traffic_data:
                # Run the histogram application with the loaded data
                app = HistogramApp(self.traffic_data, self.date_input)
                app.run()
            
            # Ask the user if they want to process another file
            user_input = input("Do you want to select a data file for a different date? (Y/N): ").strip().lower()
            if user_input == 'n':
                print("Exiting the program. Thank you!")
                break
            elif user_input != 'y':
                print("Invalid input. Please enter 'Y' to continue or 'N' to quit.")

# Main Execution
if __name__ == "__main__":
    # Create an instance of the processor
    processor = MultiCSVProcessor()
    # Clear any remaining data before exiting
    processor.clear_previous_data()
    # Start user interaction
    processor.handle_user_interaction()
    
    

