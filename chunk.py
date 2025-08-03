def read_data() -> str:
    with open("data.md", "r", encoding="utf-8") as f:
        return f.read()

def get_chunks() -> list[str]:
    content: str = read_data()
    chunks: list[str] = content.split('\n\n')

    result: list = []
    header: str = ""
    for c in chunks:
        if c.startswith("#"):
            header += f"{c}\n"
        else:
            result.append(f"{header}{c}")
            header = ""

    return result

if __name__ == "__main__":
    chunks: list[str] = get_chunks()
    for c in chunks:
        print(c)
        print("--------------")