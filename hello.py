import click
import tarfile
import zipfile
import os

def tar_folder(folder_path, output_path):
    with tarfile.open(output_path, 'w:gz') as tar:
        tar.add(folder_path, arcname=os.path.basename(folder_path))

def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

@click.group()
def cli():
    pass

@click.command()
@click.option("--folder", default="my_folder", help="Your folder name or path")
@click.option("--output", default="output.tar", help="The output TAR file name")
def compress_tar(folder, output):
    tar_folder(folder, output)
    click.echo(f'Folder compressed to {output}')

@click.command()
@click.option("--folder", default="my_folder", help="Your folder name or path")
@click.option("--output", default="output.zip", help="The output ZIP file name")
def compress_zip(folder, output):
    zip_folder(folder, output)
    click.echo(f'Folder compressed to {output}')

cli.add_command(compress_tar)
cli.add_command(compress_zip)

if __name__ == '__main__':
    cli()

