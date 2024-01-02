import argparse
from multiomics_network_explorer.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Project combining interaction tables, summaries, and exported graph views.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
