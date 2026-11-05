from time import sleep
from queue import Queue 
from record import Record


class Printer:
    def __init__(self, size: int, pagesPerMinute: int):
        self.queue = Queue(size)
        self.delay = 60 / pagesPerMinute

    def addJob(self, job: Record):
        self.queue.enqueue(job)

    def printAll(self):
        while not self.queue.isEmpty():
            record = self.queue.dequeue()
            print(f"Printing job {record.jobNum} with {record.numPages} pages")
            for page in range(1, record.numPages + 1):
                print(f"page: {page}/{record.numPages}")
                sleep(self.delay)
