import zipfile
import pathlib

def make_archive(sources, dest_dir):
    """Compress selected files or an entire folder into a ZIP archive with proper naming."""
    sources = [pathlib.Path(src) for src in sources]
    
    if len(sources) == 1 and sources[0].is_dir():
        # If a single folder is selected, name the ZIP file after the folder
        zip_name = f"{sources[0].name}_compressed.zip"
    else:
        # Default name for multiple files/folders
        zip_name = "compressed.zip"
    
    dest_path = pathlib.Path(dest_dir) / zip_name
    
    with zipfile.ZipFile(dest_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for source in sources:
            if source.is_dir():
                # Add entire folder structure
                for file in source.rglob("*"):  
                    archive.write(file, arcname=file.relative_to(source.parent))
            elif source.is_file():
                archive.write(source, arcname=source.name)

def extract_archive(zip_path, dest_dir):
    """Extract the contents of a ZIP archive to the selected folder."""
    with zipfile.ZipFile(zip_path, 'r') as archive:
        archive.extractall(dest_dir)

# Test function
if __name__ == "__main__":
    make_archive(["example_folder"], "output")  # Example: Compressing a folder
    extract_archive("output/example_folder_compressed.zip", "extracted_files")
