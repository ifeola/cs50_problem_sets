import re
import sys


def main():
    # print(parse(input("HTML: ")))
    # print(parse(input("HTML: ")))
    
    # https://www.youtube.com/embed/xvFZjo5PgG0
    
    string = """<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
    print(parse(string))
        


def parse(s):
    pattern = r"https?://(?:www\.)?youtube\.com/embed/([^ \"]+)?"
    match = re.search(rf"{pattern}", s)
    url = match.group(1)
    # return f"https://youtu.be/{url}"
    return url

if __name__ == "__main__":
    main()
    
