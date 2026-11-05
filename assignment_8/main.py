from printer import Printer
from record import Record

def main():
    printer = Printer(size=10, pagesPerMinute=18)
    records = [
        Record(jobNum=1, numPages=5),
        Record(jobNum=2, numPages=3),
        Record(jobNum=3, numPages=7),
        Record(jobNum=4, numPages=2),
        Record(jobNum=5, numPages=4),
        Record(jobNum=6, numPages=6),
        Record(jobNum=7, numPages=1),
    ]

    for record in records:
        printer.addJob(record)

    printer.printAll()

if __name__ == "__main__":
    main()