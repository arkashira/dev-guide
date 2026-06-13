import argparse
import json
from dataclasses import dataclass

@dataclass
class DevGuide:
    name: str
    description: str

    def to_json(self):
        return json.dumps(self.__dict__)

def main():
    parser = argparse.ArgumentParser(description='Dev Guide Platform', prog='dev_guide')
    parser.add_argument('--name', help='Name of the dev guide')
    parser.add_argument('--description', help='Description of the dev guide')
    args = parser.parse_args()
    if args.name and args.description:
        dev_guide = DevGuide(args.name, args.description)
        print(dev_guide.to_json())
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
