#!/usr/bin/env python3
"""
Script to add or update "Last modified: [date]" in markdown files in _posts directory
based on the last commit date from git log.
"""

import os
import subprocess
import re
from datetime import datetime
from pathlib import Path


def get_git_last_modified(file_path):
    """Get the last modified date of a file from git log."""
    try:
        # Get the last commit date for the specific file
        result = subprocess.run([
            'git', 'log', '-1', '--format=%cd', '--date=short', file_path
        ], capture_output=True, text=True, cwd=os.path.dirname(os.path.abspath(__file__)) + '/..')
        
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        else:
            # Fall back to file system modification date if git fails
            stat = os.stat(file_path)
            return datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d')
    except Exception as e:
        print(f"Error getting git date for {file_path}: {e}")
        # Fall back to file system modification date
        stat = os.stat(file_path)
        return datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d')


def update_last_modified_in_file(file_path, last_modified_date):
    """Update or add the 'Last modified' line in a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match existing "last updated" or "Last modified" lines
    # This handles variations like:
    # (last updated: 2025-02-24 - WIP)
    # (Last modified: 2025-02-24)
    # Last modified: 2025-02-24
    last_modified_pattern = r'\(?(last updated|Last modified):\s*\d{4}-\d{2}-\d{2}[^)]*\)?'
    
    new_last_modified_line = f"(Last modified: {last_modified_date})"
    
    # Check if there's already a last modified line
    if re.search(last_modified_pattern, content, re.IGNORECASE):
        # Replace existing line
        content = re.sub(last_modified_pattern, new_last_modified_line, content, flags=re.IGNORECASE)
        print(f"Updated existing last modified date in {file_path}")
    else:
        # Add new line after the YAML front matter
        lines = content.split('\n')
        yaml_end_index = -1
        
        # Find the end of YAML front matter
        if lines[0].strip() == '---':
            for i, line in enumerate(lines[1:], 1):
                if line.strip() == '---':
                    yaml_end_index = i
                    break
        
        if yaml_end_index != -1:
            # Insert after the YAML front matter
            lines.insert(yaml_end_index + 1, new_last_modified_line)
            lines.insert(yaml_end_index + 2, '')  # Add blank line
            content = '\n'.join(lines)
            print(f"Added new last modified date in {file_path}")
        else:
            # If no YAML front matter found, add at the beginning
            content = new_last_modified_line + '\n\n' + content
            print(f"Added last modified date at beginning of {file_path}")
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    """Main function to process all markdown files in _posts directory."""
    script_dir = Path(__file__).parent
    posts_dir = script_dir.parent / '_posts'
    
    if not posts_dir.exists():
        print(f"Error: _posts directory not found at {posts_dir}")
        return
    
    # Find all markdown files in _posts directory
    markdown_files = list(posts_dir.glob('*.markdown')) + list(posts_dir.glob('*.md'))
    
    if not markdown_files:
        print("No markdown files found in _posts directory")
        return
    
    print(f"Found {len(markdown_files)} markdown files to process")
    
    for file_path in markdown_files:
        print(f"\nProcessing: {file_path.name}")
        
        # Get last modified date from git
        last_modified_date = get_git_last_modified(str(file_path))
        print(f"Last modified date from git: {last_modified_date}")
        
        # Update the file
        update_last_modified_in_file(str(file_path), last_modified_date)
    
    print(f"\nCompleted processing {len(markdown_files)} files")


if __name__ == '__main__':
    main() 