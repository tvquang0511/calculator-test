import os
import zipfile

def create_zip(source_dir, output_zip):
    exclude_dirs = {'node_modules', '.git', 'playwright-report', 'test-results', '.vscode', '__pycache__'}
    exclude_files = {output_zip, 'Nhom02.zip'}
    
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # Exclude unwanted directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                if file.startswith('~$') or file in exclude_files or file.endswith('.pyc'):
                    continue
                file_path = os.path.join(root, file)
                # Compute relative path inside the zip (prefixed with Nhom02/ for clean unzipping)
                rel_path = os.path.relpath(file_path, source_dir)
                archive_name = os.path.join('Nhom02', rel_path)
                zipf.write(file_path, archive_name)
                print(f"Added: {archive_name}")

if __name__ == '__main__':
    src = os.path.abspath('.')
    out = os.path.abspath('Nhom02.zip')
    create_zip(src, out)
    print(f"\nSUCCESS: Created {out} ({os.path.getsize(out)} bytes)")
