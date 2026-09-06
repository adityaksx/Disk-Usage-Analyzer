# Disk Usage Analyzer

A lightweight Python-based disk usage analyzer that scans a folder recursively and generates a visual HTML report showing files and folders sorted by size, with percentage usage bars and expandable folder contents.

## Features

- Recursively scans folders and subfolders.
- Calculates file and folder sizes.
- Sorts items by size in descending order.
- Displays file and folder percentages relative to the scanned directory.
- Generates an interactive HTML report.
- Expand/collapse folders in the generated report.
- Uses only Python's standard library.

## Requirements

- Python 3.8 or newer
- No external Python packages are required.

## Usage

Run the Python script:

```bash
python main.py
```

Enter the folder path when prompted:

```text
Enter folder path to analyze: /path/to/folder
```

The program scans the selected directory and creates:

```text
disk_report.html
```

Open `disk_report.html` in a web browser to view the report.

## Output

The generated report includes:

- File and folder names
- Size in B, KB, MB, GB, or TB
- Percentage of total scanned size
- Visual size bars
- Expandable folder trees

## Project Structure

```text
.
├── main.py
├── disk_report.html    # Generated after running the program
├── requirements.txt
└── README.md
```

## How It Works

1. The program asks for a directory path.
2. It recursively scans the directory using `os.scandir()`.
3. File sizes are collected using filesystem metadata.
4. Folder sizes are calculated recursively.
5. Results are sorted from largest to smallest.
6. The data is converted into an HTML report.
7. The report is saved as `disk_report.html`.

## Limitations

- Access errors are silently skipped.
- The scan can take time for large directories.
- The generated report is static; rescanning is required to update it.
- Folder size is calculated from files and subfolders that the program can access.

## License

This project is open source. See the repository license file for the applicable license.
