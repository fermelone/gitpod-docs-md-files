#!/usr/bin/env python3

import os
import re
import requests
import time
from urllib.parse import urlparse
from pathlib import Path

def download_gitpod_docs():
    """Download all Gitpod documentation markdown files with proper folder structure."""
    
    base_dir = Path("gitpod-docs")
    base_dir.mkdir(exist_ok=True)
    
    print("Fetching llms.txt to get list of markdown files...")
    
    # Fetch the llms.txt file
    try:
        response = requests.get("https://www.gitpod.io/docs/llms.txt")
        response.raise_for_status()
        content = response.text
    except requests.RequestException as e:
        print(f"Error fetching llms.txt: {e}")
        return
    
    # Extract markdown URLs using regex - looking for the specific pattern in llms.txt
    md_pattern = r'\- \[.*?\]\((https://www\.gitpod\.io/docs/.*?\.md)\)'
    urls = re.findall(md_pattern, content)
    
    if not urls:
        # Try alternative pattern without the dash
        md_pattern = r'\[.*?\]\((https://www\.gitpod\.io/docs/.*?\.md)\)'
        urls = re.findall(md_pattern, content)
    
    if not urls:
        print("No markdown URLs found in llms.txt")
        return
    
    print(f"Found {len(urls)} markdown files to download")
    print("Starting download...\n")
    
    success_count = 0
    failed_urls = []
    
    for i, url in enumerate(urls, 1):
        try:
            # Extract relative path
            parsed_url = urlparse(url)
            relative_path = parsed_url.path.replace('/docs/', '')
            
            # Create local path
            local_path = base_dir / relative_path
            
            # Create directory structure
            local_path.parent.mkdir(parents=True, exist_ok=True)
            
            print(f"[{i}/{len(urls)}] Downloading: {relative_path}")
            
            # Download the file
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Save the file
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            print(f"  ✓ Success")
            success_count += 1
            
            # Be respectful with requests
            time.sleep(0.1)
            
        except requests.RequestException as e:
            print(f"  ✗ Failed: {e}")
            failed_urls.append(url)
        except Exception as e:
            print(f"  ✗ Error: {e}")
            failed_urls.append(url)
    
    print(f"\nDownload complete!")
    print(f"Successfully downloaded: {success_count}/{len(urls)} files")
    print(f"Files saved to: {base_dir.absolute()}/")
    
    if failed_urls:
        print(f"\nFailed downloads ({len(failed_urls)}):")
        for url in failed_urls[:5]:  # Show first 5 failures
            print(f"  - {url}")
        if len(failed_urls) > 5:
            print(f"  ... and {len(failed_urls) - 5} more")
    
    # Show directory structure
    print(f"\nDirectory structure:")
    md_files = list(base_dir.rglob("*.md"))
    for md_file in md_files[:10]:
        rel_path = md_file.relative_to(base_dir)
        print(f"  {rel_path}")
    
    if len(md_files) > 10:
        print(f"  ... and {len(md_files) - 10} more files")

if __name__ == "__main__":
    download_gitpod_docs()