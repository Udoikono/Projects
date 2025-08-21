import hashlib
import sys
import requests


def check_password(password):
    # Hash the password using SHA-1
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_char, last = hashed_password[:5], hashed_password[5:]

    # Contact the API with the first 5 characters of the hash
    url = f'https://api.pwnedpasswords.com/range/{first_char}'
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f'API Error: {response.status_code}')

    # Parse the response to find a match
    hashes = (line.split(':') for line in response.text.splitlines())
    found = False
    for h, count in hashes:
        if h == last:
            print(f'⚠️ Your password "{password}" has been breached {count} times. Consider changing it.')
            found = True
            break

    if not found:
        print(f'✅ Your password "{password}" has NOT been found in known breaches. Carry on!')


def main(args):
    for password in args:
        check_password(password)


if __name__ == "__main__":
    # Exclude the script name itself from the arguments
    main(sys.argv[1:])
