import tarfile

def compress(backup_file, compressed_file):
    try:    
        with tarfile.open(compressed_file, mode= "w:gz") as  tar:
            tar.add(backup_file)
    except (tarfile.TarError, FileNotFoundError) as e:
        print(f"Error {e} occurred during compression")
        