"""Standalone release-status entry point for the CREST public preview."""

import argparse


RELEASE_NOTE = (
    "The full implementation will be released upon acceptance of the paper."
)


def main():
    parser = argparse.ArgumentParser(
        description="Display the release status of the CREST public preview.",
        epilog=RELEASE_NOTE,
    )
    parser.parse_args()
    print("CREST | Aircraft trajectory prediction")
    print("Release status: public preview.")
    print(RELEASE_NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
