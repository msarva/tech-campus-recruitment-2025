import sys
import os
import zipfile

def extract_logs(log_zip_file, date):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{date}.txt")

    with zipfile.ZipFile(log_zip_file, 'r') as z:
        log_filename = z.namelist()[0]  # Assuming only one log file inside
        with z.open(log_filename, 'r') as log_file, open(output_file, 'w', encoding='utf-8') as out_file:
            for line in log_file:
                line = line.decode('utf-8')  # Convert bytes to string
                if line.startswith(date):  # Extract logs for the specific date
                    out_file.write(line)

    print(f"Logs for {date} have been saved in {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <log_file.zip> <YYYY-MM-DD>")
        sys.exit(1)

    log_zip_file = sys.argv[1]
    date = sys.argv[2]
    extract_logs(log_zip_file, date)
