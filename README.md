# UPDATE

This repo can now be replaced by this: https://www.gitpod.io/docs/llms-full.txt

---
## Gitpod Documentation Downloader

A Python script that downloads all Gitpod documentation markdown files from their website, maintaining the original folder structure for local access and analysis.

## Features

- Downloads all markdown files from Gitpod's documentation
- Preserves original folder structure
- Replaces existing files on each run for fresh updates
- Rate-limited requests to be respectful to the server
- Comprehensive error handling and progress reporting

## Setup

1. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script to download all Gitpod documentation:

```bash
python get-md-files.py
```

The script will:
1. Remove any existing `gitpod-docs/` folder
2. Create a fresh directory structure
3. Download all markdown files from Gitpod's documentation
4. Display progress and summary statistics

## Output

All files are saved to the `gitpod-docs/` directory with the same structure as the original documentation website.

## Requirements

- Python 3.7+
- `requests` library (see requirements.txt)

## Notes

- The script fetches the file list from `https://www.gitpod.io/docs/llms.txt`
- Downloads are rate-limited with a 0.1-second delay between requests
- Failed downloads are reported at the end of execution
