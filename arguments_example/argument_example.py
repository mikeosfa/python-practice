import argparse

def main(sample_string):
    if len(sample_string) >0:
        print(sample_string)
    else:
        print ("No string passed")
         



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Print a supplied string"
    )

    parser.add_argument(
        "message",
        help="The message to print"
    )

    args = parser.parse_args()

    main(args.message)