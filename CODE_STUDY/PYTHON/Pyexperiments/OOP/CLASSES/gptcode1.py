class Job:
    def work(self):
        print("Working...")

class Person:
    def __init__(self, job):
        self.job = job

    def do_work(self):
        self.job.work()

my_job = Job()
john = Person(my_job)
john.do_work()  # Output: Working...
