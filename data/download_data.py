import subprocess
import os

# Downlaod all export files:
# makes sure all downloads happen in the data/ folder:
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

years = range(1997, 2026)
dir_files = os.listdir()
for year in years:
    url = f"https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_{year}.csv"
    current_file = f"EXP_{year}.csv"
    if current_file not in dir_files:
        subprocess.run(["wget", url])

# Make file with concatenation of all files:
if "all_exports.csv" not in dir_files:
    export_files = [file for file in dir_files if file[:3] == "EXP"]
    with open("all_exports.csv", "w", encoding="latin-1") as all_exports:
        for file in export_files:
            print(f"concatenating file {file}...")
            with open(file, "r", encoding="latin-1") as csv_file:
                for line in csv_file.readlines():
                    all_exports.write(line)
    print("Created file all_exports.csv containing all exports data!")
