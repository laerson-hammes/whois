# https://pypi.org/project/python-whois/
import whois
import argparse


def scan_whois(domain: str) -> None:
    try:
        consult = whois.whois(domain)
        print(consult.text)
        with open(domain + ".txt", "w") as f:
            f.write(consult.text)
    except Exception as e:
        print(e)


def get_arguments() -> str:
   parser = argparse.ArgumentParser()
   parser.add_argument("-d", "--domain", dest="domain", help="Domain name")
   options = parser.parse_args()
   if not options.domain:
      domain: str = str(input("Domain name: "))
      return domain
   return options.domain


if __name__ == "__main__":
    scan_whois(domain := get_arguments())