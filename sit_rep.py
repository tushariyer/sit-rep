import sit_rep_server as server
import sit_rep_client as client


def get_input(text):
    return input(text)


def main():
    # User Prompts
    client_or_server = get_input("Is this a Sit-Rep Client or Server? (c/s)\n")

    if client_or_server == "c":
        client.main()
    elif client_or_server == "s":
        server.main()
    else:
        raise Exception('Invalid Response. Enter c for Client or s for Server')


if __name__ == '__main__':
    main()
