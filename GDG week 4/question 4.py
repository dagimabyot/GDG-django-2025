class Teacher:
    def work(self):
        print("Teacher is teaching students")

class Doctor:
    def work(self):
        print("Doctor is treating patients")

workers =[Teacher(), Doctor()]

for w in workers:
    w.work()
