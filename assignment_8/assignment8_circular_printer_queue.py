"""Programming Assignment 8: Circular printer queue with priority jobs.

Run this file with Python 3. The application accepts jobs interactively and
then simulates printing them at the selected pages-per-minute rate.
"""

from dataclasses import dataclass
from time import sleep
from typing import List, Optional


STANDARD = "standard"
PRIORITY = "priority"
MIN_PAGES = 1
MAX_PAGES = 100


@dataclass(frozen=True)
class Record:
    """One print job stored in the queue.

    The assignment's required fields are jobNum and numPages. The priority
    field is the additional data item used for the extra-credit feature.
    """

    jobNum: int
    numPages: int
    priority: str = STANDARD


class Queue:
    """Fixed-size circular queue for printer records.

    Empty-state positions are virtual: front is the next slot to fill and
    back is the slot immediately before front. At startup front is 0 and
    back is size - 1, so the first enqueue uses table index 0. After a
    dequeue, the table slot is left untouched; a later enqueue overwrites it.
    """

    def __init__(self, size: int):
        if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
            raise ValueError("Queue size must be a positive integer.")

        self.size = size
        self.count = 0
        self.front = 0
        self.back = size - 1
        self.table: List[Optional[Record]] = [None] * size

    def isEmpty(self) -> bool:
        """Return True when the queue contains no records."""
        return self.count == 0

    def isFull(self) -> bool:
        """Return True when every queue location is occupied."""
        return self.count == self.size

    def enqueue(self, record: Record) -> None:
        """Add a record, validating the printer's page limit.

        Standard jobs go to the back. A priority job shifts the waiting jobs
        one slot toward the back and occupies the front. Since a job being
        printed has already been dequeued, this puts a priority job directly
        after the job in service.
        """
        if not isinstance(record, Record):
            raise TypeError("enqueue expects a Record.")
        if isinstance(record.jobNum, bool) or not isinstance(record.jobNum, int):
            raise ValueError("Job number must be an integer.")
        if (isinstance(record.numPages, bool)
                or not isinstance(record.numPages, int)
                or not MIN_PAGES <= record.numPages <= MAX_PAGES):
            raise ValueError("A print job must have between 1 and 100 pages.")
        if not isinstance(record.priority, str):
            raise ValueError("Priority must be 'standard' or 'priority'.")

        job_priority = record.priority.strip().lower()
        if job_priority not in (STANDARD, PRIORITY):
            raise ValueError("Priority must be 'standard' or 'priority'.")
        if self.isFull():
            raise OverflowError("The queue is full; this job was not added.")

        if job_priority == PRIORITY and not self.isEmpty():
            # Shift from back toward the free slot. Going backward prevents
            # each source record from being overwritten before it is copied.
            for offset in range(self.count, 0, -1):
                source = (self.front + offset - 1) % self.size
                destination = (self.front + offset) % self.size
                self.table[destination] = self.table[source]

            self.table[self.front] = record
            self.back = (self.front + self.count) % self.size
            self.count += 1
        else:
            # This also handles a priority job added to an empty queue.
            self.back = (self.back + 1) % self.size
            self.table[self.back] = record
            self.count += 1
            if self.count == 1:
                self.front = self.back

    def dequeue(self) -> Record:
        """Remove and return the front record, without shifting the table."""
        if self.isEmpty():
            raise IndexError("Cannot dequeue from an empty queue.")

        record = self.table[self.front]
        # A nonempty queue always has a Record at front.
        assert record is not None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        # When count reaches zero, front and back are again virtual adjacent
        # positions, with the next enqueue reusing the location just served.
        return record

    def records_in_order(self) -> List[Record]:
        """Return a snapshot of accessible records from front to back."""
        records: List[Record] = []
        for offset in range(self.count):
            record = self.table[(self.front + offset) % self.size]
            if record is not None:
                records.append(record)
        return records


class Printer:
    """Print queued jobs using a delay based on pages per minute."""

    def __init__(self, queue: Queue, pages_per_minute: int = 18):
        if (isinstance(pages_per_minute, bool)
                or not isinstance(pages_per_minute, int)
                or pages_per_minute <= 0):
            raise ValueError("Pages per minute must be a positive integer.")
        self.queue = queue
        self.pages_per_minute = pages_per_minute

    def print_all(self) -> None:
        """Continue printing until the queue is empty."""
        seconds_per_page = 60.0 / self.pages_per_minute

        while not self.queue.isEmpty():
            job = self.queue.dequeue()
            print(f"\nPrinting job {job.jobNum} ({job.numPages} pages).")

            for page in range(1, job.numPages + 1):
                print(
                    f"Job {job.jobNum}: page {page}/{job.numPages}",
                    end="\r",
                    flush=True,
                )
                sleep(seconds_per_page)

            print(f"Job {job.jobNum} complete.{' ' * 12}")

        print("All print jobs are complete.")


def prompt_integer(prompt: str, default: int, minimum: int,
                   maximum: Optional[int] = None) -> int:
    """Read an integer, using default when the user presses Enter."""
    while True:
        answer = input(f"{prompt} [{default}]: ").strip()
        if not answer:
            return default
        try:
            value = int(answer)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if value < minimum or (maximum is not None and value > maximum):
            if maximum is None:
                print(f"Enter a value of at least {minimum}.")
            else:
                print(f"Enter a value from {minimum} to {maximum}.")
            continue
        return value


def prompt_job_number() -> Optional[int]:
    """Read a job number, or return None when the user is ready to print."""
    while True:
        answer = input("Job number (press Enter to start printing): ").strip()
        if not answer:
            return None
        try:
            return int(answer)
        except ValueError:
            print("Job number must be a whole number.")


def prompt_priority() -> str:
    """Read the job's priority type."""
    while True:
        answer = input("Type S for standard or P for priority [S]: ").strip().lower()
        if answer in ("", "s", STANDARD):
            return STANDARD
        if answer in ("p", PRIORITY):
            return PRIORITY
        print("Enter S for standard or P for priority.")


def run_application() -> None:
    """Collect print jobs interactively, then run the printer simulation."""
    print("Circular Printer Queue")
    capacity = prompt_integer("Queue capacity", default=8, minimum=1)
    speed = prompt_integer(
        "Printer speed in pages per minute", default=18, minimum=1
    )
    queue = Queue(capacity)

    print("\nEnter print jobs. Press Enter at the job-number prompt to begin printing.")
    print(f"Each job must contain between {MIN_PAGES} and {MAX_PAGES} pages.")

    while not queue.isFull():
        job_number = prompt_job_number()
        if job_number is None:
            break

        pages = prompt_integer("Number of pages", default=1,
                               minimum=MIN_PAGES, maximum=MAX_PAGES)
        priority = prompt_priority()
        try:
            queue.enqueue(Record(job_number, pages, priority))
        except (TypeError, ValueError, OverflowError) as error:
            print(f"Job was not added: {error}")
            continue
        print(f"Job {job_number} added as {priority}.")

    if queue.isEmpty():
        print("No print jobs were submitted.")
        return

    if queue.isFull():
        print("The queue is full. Printing the accepted jobs now.")

    print("\nJobs waiting in print order:")
    for job in queue.records_in_order():
        print(f"  Job {job.jobNum}: {job.numPages} pages ({job.priority})")

    Printer(queue, pages_per_minute=speed).print_all()


if __name__ == "__main__":
    run_application()
