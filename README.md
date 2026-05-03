# 🚦 Traffic Data Analyser & Visualizer

A Python-based traffic survey data analysis tool that processes real-world junction traffic data from CSV files, generates detailed statistical reports, and produces a graphical histogram of vehicle frequency per hour.

> **Author:** Isiri Gangamini Jayaneththi | **Student ID:** 20240577 | **Date:** 09/12/2024

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [How to Run](#how-to-run)
- [Program Walkthrough](#program-walkthrough)
- [Sample Output](#sample-output)
- [Technologies Used](#technologies-used)

---

## Overview

This coursework project analyses traffic survey data collected at two junctions:

- **Elm Avenue / Rabbit Road**
- **Hanley Highway / Westway**

The program reads daily CSV traffic records, validates user date input, processes multiple traffic metrics, saves results to a text file, and renders an interactive histogram showing vehicle frequency per hour for each junction.

---

## Features

### ✅ Task A — Input Validation
- Prompts the user to enter a survey date (DD MM YYYY format)
- Validates day (1–31), month (1–12), and year (2000–2024)
- Handles incorrect data types and out-of-range values with clear error messages
- Loops until a valid date is entered

### ✅ Task B — CSV Data Processing
Extracts and calculates the following metrics from the selected date's CSV file:

| Metric | Description |
|--------|-------------|
| Total vehicles | All vehicles recorded at both junctions |
| Total trucks | Count of truck-type vehicles |
| Electric/Hybrid vehicles | Vehicles flagged as electric or hybrid |
| Two-wheeled vehicles | Bicycles, motorcycles, and scooters combined |
| Buses heading North (Elm Ave) | Buses at Elm Avenue/Rabbit Road travelling north |
| Vehicles not turning | Vehicles with matching in/out direction (going straight) |
| Truck percentage | Trucks as a percentage of total vehicles |
| Average bikes per hour | Mean bicycle count across active hours |
| Over speed limit | Vehicles exceeding the junction speed limit |
| Junction totals | Vehicle counts per junction |
| Scooter percentage (Elm Ave) | Scooters as % of Elm Avenue/Rabbit Road traffic |
| Peak hour (Hanley Highway) | Hour with most vehicles at Hanley Highway/Westway |
| Rain hours | Number of hours with rainy weather conditions |

### ✅ Task C — Save Results to File
- Appends all statistical output to `results.txt`
- Supports multiple runs — each new date's results are added without overwriting

### ✅ Task D — Histogram Visualisation
- Renders a **graphical histogram** using `graphics.py` (Tkinter-based)
- Shows vehicle count per hour (00:00–24:00) for both junctions side by side
- **Green bars** = Elm Avenue / Rabbit Road
- **Orange bars** = Hanley Highway / Westway
- Includes bar value labels, hour axis labels, and a colour legend
- Click anywhere on the window to close it

### ✅ Task E — Multi-File Processor
- After viewing results, prompts the user to analyse another date
- Clears previous session data between runs
- Enter `Y` to load a new date or `N` to exit

---

## Project Structure

```
traffic-visualizer/
│
├── w2120048.py                    # Main program — all tasks (A–E)
├── graphics.py                    # Graphics library (Zelle, open-source)
├── pseudocode.txt                 # Pseudocode for program logic
├── results.txt                    # Auto-generated output file (appended per run)
│
├── traffic_data15062024.csv       # Survey data — 15 June 2024
├── traffic_data16062024.csv       # Survey data — 16 June 2024
├── traffic_data21062024.csv       # Survey data — 21 June 2024
│
└── Test Case (task D and E).pdf   # Test case documentation
```

---

## Dataset

Each CSV file contains traffic records with the following columns:

| Column | Description |
|--------|-------------|
| `JunctionName` | Junction identifier (Elm Avenue/Rabbit Road or Hanley Highway/Westway) |
| `Date` | Date of the survey (DD/MM/YYYY) |
| `timeOfDay` | Time the vehicle was recorded (HH:MM:SS) |
| `travel_Direction_in` | Direction vehicle entered the junction (N/S/E/W) |
| `travel_Direction_out` | Direction vehicle exited the junction (N/S/E/W) |
| `Weather_Conditions` | Weather at time of recording (e.g., Overcast, Rain, Clear) |
| `JunctionSpeedLimit` | Speed limit at the junction (mph) |
| `VehicleSpeed` | Recorded vehicle speed (mph) |
| `VehicleType` | Type of vehicle (Truck, Car, Bicycle, Motorcycle, Scooter, Buss) |
| `elctricHybrid` | Whether the vehicle is electric/hybrid (TRUE/FALSE) |

**Available dates:** 15/06/2024, 16/06/2024, 21/06/2024

---

## How to Run

### Prerequisites
- Python 3.x installed
- Tkinter available (comes built-in with most Python installations)
- All files in the **same directory**

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Isi2004-star/traffic-visualizer.git
   cd traffic-visualizer
   ```

2. Run the main program:
   ```bash
   python w2120048.py
   ```

3. When prompted, enter a valid survey date:
   ```
   Please enter the day of the survey in the format DD: 15
   Please enter the month of the survey in the format MM: 06
   Please enter the year of the survey in the format YYYY: 2024
   ```

4. View the statistical summary printed in the terminal

5. A **histogram window** will open — click it to close

6. Choose whether to analyse another date (`Y`) or exit (`N`)

> ⚠️ The CSV data files must be named in the format `traffic_dataDDMMYYYY.csv` and placed in the same folder as the script.

---

## Sample Output

```
***************************
Data file selected: traffic_data15062024.csv
***************************
The total number of vehicles recorded for this date is 1452
The total number of trucks recorded for this date is 214
The total number of electric vehicles for this date is 386
The total number of two-wheeled vehicles for this date is 320
The total number of busses leaving Elm Avenue/Rabbit Road heading North is 43
The total number of vehicles through both junctions not turning left or right is 789
The percentage of total vehicles recorded that are trucks for this date is 15%
The average number of bikes per hour for this date is 6
The total number of vehicles recorded as over the speed limit for this date is 127
The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is 734
The total number of vehicles recorded through Hanley Highway/Westway junction is 718
...
```

Results are also saved and appended to `results.txt` after each run.

---

## Technologies Used

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-informational?style=flat)

- **Python 3** — Core language
- **csv module** — CSV file parsing
- **collections.Counter** — Frequency counting
- **datetime** — Date parsing and formatting
- **graphics.py** — Tkinter-based graphics library by John Zelle



