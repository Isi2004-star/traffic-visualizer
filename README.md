## Traffic Visualizer

This Python-based Traffic Visualizer project processes and analyzes vehicle traffic data from CSV files. 
It provides detailed statistical insights and displays a histogram of vehicle frequency per hour using a graphical interface.

## Features

Total and categorized vehicle counts (trucks, electric, two-wheelers, etc.)

Histogram of vehicle frequency per hour (with GUI)

Weather-based filtering (e.g., rainy hours)

Junction-based insights (e.g., Elm Avenue/Rabbit Road, Hanley Highway/Westway)

Results saved to a text file for reporting

## Technologies Used

Python (Core logic and GUI)

graphics.py (for histogram visualization)

csv and collections modules

## How It Works

User inputs a survey date (validated in DD MM YYYY format).

The corresponding CSV file is read and analyzed.

Key metrics like overspeeding, junction-specific counts, and vehicle categories are extracted.

A graphical histogram of hourly vehicle frequency is displayed.

Results are saved in a results.txt file.

## Author

Isiri Gangamini Jayaneththi
Student ID: 20240577
Date: 09/12/2024

## Getting Started

Ensure you have Python installed.

Install graphics.py (part of the Zelle graphics library).

Place your traffic CSV files with names like traffic_dataDDMMYYYY.csv.

Run the script using python traffic_visualizer.py.

## File Structure

traffic_visualizer.py – Main program logic

results.txt – Output file for textual summaries

traffic_dataDDMMYYYY.csv – Input data files (one per date)

## Want to Explore More?

If you're interested in exploring the complete codebase or contributing to the project, 
feel free to check out the source files or reach out. Suggestions and improvements are always welcome!

