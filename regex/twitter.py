# `import re` is importing the `re` module in Python. The `re` module provides support for regular
# expressions, which are a powerful tool for pattern matching and string manipulation. By importing
# the `re` module, we can use its functions and classes to work with regular expressions in our code.
import re

def format_url(url):
    # The line `username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)` is using the `re.sub()`
    # function from the `re` module in Python to remove the prefix `https://`, `http://`, or `www.` and
    # the string `twitter.com/` from the `url` variable. It replaces the matched pattern with an empty
    # string, effectively extracting the username from the Twitter URL.
    #return re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

    # The line `if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url,
    # re.IGNORECASE):` is using the `re.search()` function from the `re` module in Python to search
    # for a pattern in the `url` variable.
    if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
        # `return matches.group(2)` is returning the second group of the matched pattern from the
        # `re.search()` function.
        return matches.group(1)


def main():
    """
    The main function prompts the user for a URL, strips any leading or trailing whitespace, and then
    prints the formatted URL.
    """
    url = input("URL: ").strip()
    print(f"username: {format_url(url)}")

if __name__ == "__main__":
    main()