import click
import sys
import os
import typing
import cli_functions as func

#Decorator to create custom cli commands
@click.command()

#Attaches an argument to the command
@click.argument("file", nargs=-1, type=click.Path(exists=True))

#CLI options of wc tool
@click.option('-c', help = "Displays the number of bytes in the file", default = False, is_flag = True)
@click.option('-l', help = "Displays the number of lines in the file", default = False, is_flag = True)
@click.option('-w', help = "Displays the number of words in the file", default = False, is_flag = True)
@click.option('-m', help = "Displays the number of characters in the file", default = False, is_flag = True)

def main(file,c,l,w,m):
    if not file:
        file_name = " "
        file_data = sys.stdin.buffer
        bytes = func.byte_count(file_data)
        words = func.word_count(file_data)
        lines = func.line_count(file_data)
        chars = func.char_count(file_data)
    else:
        file_name =file
        bytes = func.byte_count(file)
        with open(file,'rb', encoding="utf-8") as open_file:
            file_data = open_file.read()
            words = func.word_count(file_data)
            lines = func.line_count(file_data)
            chars = func.char_count(file_data)

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