import httpx
import typer


def main(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
    }
    response = httpx.get(url, headers=headers)
    typer.echo(f"Status code: {response.status_code}")
    typer.echo(f"Content: {response.text[:100]}...")


if __name__ == "__main__":
    typer.run(main)
