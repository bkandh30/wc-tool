import click
import sys

def byte_count(file_content:str) -> int:
    """
    Returns the number of bytes
    Args:
        file: File object
    Returns:
        int: Number of bytes in the file
    """
    return len(file_content.encode('utf-8'))

def line_count(file_content:str) -> int:
    """
    Returns the number of lines
    Args:
        file: File object
    Returns:
        int: Number of lines in the file
    """
    return file_content.count('\n')

def word_count(file_content:str) -> int:
    """
    Returns the number of words
    Args:
        file: File object
    Returns:
        int: Number of words in the file
    """
    words = file_content.split()
    return len(words)

def char_count(file_content:str) -> int:
    """
    Returns the number of characters
    Args:
        file: File object
    Returns:
        int: Number of characters in the file
    """
    return len(file_content)

@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True))
@click.option('-c', help="Displays the number of bytes in the file", is_flag=True)
@click.option('-l', help="Displays the number of lines in the file", is_flag=True)
@click.option('-w', help="Displays the number of words in the file", is_flag=True)
@click.option('-m', help="Displays the number of characters in the file", is_flag=True)
def main(files, c, l, w, m):
    # Empty list to collect file data
    file_data = []
    
    # Check if any files were provided as arguments
    if not files:
        # If no files, use standard input
        file_data.append((sys.stdin.read(), "<stdin>"))
    else:
        # Open the files and it's contents
        for file_path in files:
            with open(file_path, 'r', encoding="utf-8") as file:
                file_data.append((file.read(), file_path))
    
    # Process every file's data
    for content, file_name in file_data:
        bytes = byte_count(content)
        words = word_count(content)
        lines = line_count(content)
        chars = char_count(content)
        
        # Display the results based on command line options
        if c:
            click.echo(f"{bytes} {file_name}")
        elif l:
            click.echo(f"{lines} {file_name}")
        elif w:
            click.echo(f"{words} {file_name}")
        elif m:
            click.echo(f"{chars} {file_name}")
        else:
            click.echo(f"{bytes} {lines} {words} {chars} {file_name}")

if __name__ == '__main__':
    main()