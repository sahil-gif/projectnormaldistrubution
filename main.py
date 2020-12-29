import pandas as pd
import statistics
import csv
df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()
height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)
height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)
height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)
height_std_deviation = statistics.stdev(height_list)
weight_std_deviation = statistics.stdev(weight_list)
std = statistics.stdev(height-weight)
print()
print()
print()
