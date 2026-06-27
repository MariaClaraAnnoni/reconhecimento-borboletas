from pathlib import Path
import subprocess
import zipfile
import shutil

DATASET = "lara311/spongebob-patrickstar-and-squidward-detection"

DATA_DIR = Path("data")
FINAL_DIR = DATA_DIR / "dataset"


def main():

    DATA_DIR.mkdir(exist_ok=True)

    # Não baixa novamente se já existir
    if FINAL_DIR.exists():
        print("Dataset já encontrado.")
        return

    print("Baixando dataset...")

    subprocess.run(
        [
            "kaggle",
            "datasets",
            "download",
            "-d",
            DATASET,
            "-p",
            str(DATA_DIR),
        ],
        check=True,
    )

    # Procura o arquivo .zip baixado
    zip_file = next(DATA_DIR.glob("*.zip"))

    print("Extraindo arquivos...")

    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(DATA_DIR)

    zip_file.unlink()

    # Renomeia a pasta extraída
    original_folder = DATA_DIR / "SpongeBob Object Detection"

    if original_folder.exists():
        shutil.move(str(original_folder), str(FINAL_DIR))

    print(f"\nDataset disponível em: {FINAL_DIR}")


if __name__ == "__main__":
    main()
