import subprocess
import pandas as pd

taskname = "babylm"
download_dir = "../env"

subprocess.run(["wget", "-q", "https://github.com/babylm/babylm.github.io/raw/main/babylm_data.zip"], cwd=download_dir, stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL) 
subprocess.run(["unzip", "-n", f"babylm_data.zip"], cwd=download_dir,  stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL)
subprocess.run(["rm", f"babylm_data.zip"], cwd=download_dir)
subprocess.run(["rm", "-rf", f"babylm_data/babylm_100M"], cwd=download_dir)
subprocess.run(["rm", "-rf", f"__MACOSX"], cwd=download_dir)