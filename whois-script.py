import whois # type: ignore
import argparse


class Whois(object):
    def __init__(self, /) -> None:
        self.scan_whois(self.get_arguments())
        

    def scan_whois(self, domain: str, /) -> None:
        try:
            consult = whois.whois(domain)
            print(consult.text)
            with open(domain + ".txt", "w") as f:
                f.write(consult.text)
        except Exception as e:
            raise Exception(e)


    def get_arguments(self, /) -> str:
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--domain", dest="domain", help="Domain name")
        options = parser.parse_args()
        if not options.domain:
            options.domain = str(input("Domain name: "))
        return options.domain


if __name__ == "__main__":
    w = Whois()