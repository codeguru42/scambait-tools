import httpx
import typer

def main(url: str):
    response = httpx.get(url)
    typer.echo(f'Status code: {response.status_code}')
    typer.echo(f'Content: {response.text[:100]}...')

if __name__ == '__main__':
    typer.run(main)