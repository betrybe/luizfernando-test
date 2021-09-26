import sys
import getopt
from inventory_report.inventory.inventory_refactor import LineReport


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "", ["inventory", "file=", "type="])
    except getopt.GetoptError:
        print("inventory_report <file> <type_report>")
        sys.exit(2)
    LineReport.line_report("path_file", "type")


if __name__ == "__main__":
    main(sys.argv[1:])
