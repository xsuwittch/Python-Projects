import tarfile

def decompress(compressed_file, output_file_path):

    try:
        with tarfile.open(compressed_file, 'r:gz') as tar:
            tar.extractall(output_file_path)
    except tarfile.ExtractError as e:
        print(f" Error {e} occured during extraction ")