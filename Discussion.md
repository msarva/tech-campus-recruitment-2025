# Discussion

## Solutions Considered

### 1. *Single-Threaded Processing*
   - *Approach:* Read the log file line by line and extract relevant entries based on the given date.
   - *Pros:* Simple and easy to implement.
   - *Cons:* Extremely slow for large files due to sequential reading.

### 2. *Multiprocessing with File Chunks*
   - *Approach:* Split the log file into chunks and use multiprocessing to process each chunk independently.
   - *Pros:* Faster than a single-threaded approach as it utilizes multiple CPU cores.
   - *Cons:* High memory usage due to inter-process communication (multiprocessing.Queue).

### 3. **Multithreading with Buffered Reading (mmap)** (Final Choice)
   - *Approach:* Use mmap to map the file into memory and ThreadPoolExecutor for parallel processing.
   - *Pros:* Efficient file reading, avoids unnecessary memory usage, and leverages system CPU cores.
   - *Cons:* Slightly complex implementation.

## Final Solution Summary
We selected **Multithreading with Buffered Reading (mmap)** because:
- *Performance:* mmap allows fast access to file content without reading it all at once.
- *Lower Memory Usage:* Unlike multiprocessing, it avoids inter-process memory overhead.
- *Optimized CPU Utilization:* Uses ThreadPoolExecutor to efficiently parallelize log extraction.
- *Scalability:* Dynamically adjusts to the number of CPU cores.

## Steps to Run

### *Prerequisites*
- Ensure Python 3.x is installed.
- Install necessary dependencies (though all used libraries are built-in).

### *Running the Code*
1. *Clone or download the script*
   bash
   git clone <repository-link>
   cd <repository-folder>
   
2. *Run a small test* (to verify functionality)
   bash
   python extract_logs.py YYYY-MM-DD
   
   Replace YYYY-MM-DD with the desired date.

3. *Run on a full log file*
   - Ensure logs_2024.log (or any actual log file) exists in the directory.
   - Execute the command:
     bash
     python extract_logs.py YYYY-MM-DD
     

4. *Output Location*
   - Extracted logs will be saved in the output/ directory.
   - Example output file: output/output_2024-12-01.txt.

5. *Execution Time Display*
   - The script will print execution time after completing log extraction.

By following these steps, you can efficiently extract logs for any given date from a large log file. 
