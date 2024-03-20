import datetime
import time
import random

class SchoolTimeManagementSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store student details
        self.teachers = {}  # Dictionary to store teacher details
        self.classes = {}   # Dictionary to store class details
        self.exams = {}     # Dictionary to store exam details

    def add_student(self, student_id, name):
        self.students[student_id] = {'name': name, 'attendance': False}

    def add_teacher(self, teacher_id, name):
        self.teachers[teacher_id] = {'name': name}

    def add_class(self, class_id, subject, teacher_id, venue, start_time):
        self.classes[class_id] = {'subject': subject, 'teacher_id': teacher_id, 'venue': venue, 'start_time': start_time}

    def add_exam(self, exam_id, subject, date, venue):
        self.exams[exam_id] = {'subject': subject, 'date': date, 'venue': venue}

    def mark_attendance(self, student_id):
        if student_id in self.students:
            self.students[student_id]['attendance'] = True
            print(f"Attendance marked for student {self.students[student_id]['name']}")

    def get_venue(self, class_id):
        if class_id in self.classes:
            return self.classes[class_id]['venue']
        else:
            return None

    def alert(self, message):
        print("Alert:", message)

    def simulate_class_start_alert(self, class_id):
        if class_id in self.classes:
            start_time = self.classes[class_id]['start_time']
            alert_time = start_time - datetime.timedelta(minutes=5)
            current_time = datetime.datetime.now()
            while current_time < alert_time:
                time.sleep(1)
                current_time = datetime.datetime.now()
            self.alert(f"Class {class_id} will start in 5 minutes at {self.classes[class_id]['venue']}")

    def simulate_exam_alert(self, exam_id):
        if exam_id in self.exams:
            exam_date = self.exams[exam_id]['date']
            alert_time = exam_date - datetime.timedelta(minutes=5)
            current_time = datetime.datetime.now()
            while current_time < alert_time:
                time.sleep(1)
                current_time = datetime.datetime.now()
            self.alert(f"Exam {exam_id} will start in 5 minutes at {self.exams[exam_id]['venue']}")

    def simulate_gps_tracker(self, student_id, latitude, longitude):
        # Simulate GPS tracker by randomly generating location within school premises
        school_latitude = 12.3456  # Replace with actual school latitude
        school_longitude = 78.9101  # Replace with actual school longitude
        distance = ((latitude - school_latitude) ** 2 + (longitude - school_longitude) ** 2) ** 0.5
        if distance < 0.01:  # Assuming 0.01 is within school premises
            self.mark_attendance(student_id)
        else:
            print("You are not within the school premises!")

# Example usage
if __name__ == "__main__":
    school_system = SchoolTimeManagementSystem()

    # Add students
    school_system.add_student(1, "lawi Fadhili")
    school_system.add_student(2, "Cynthia Mwende")

    # Add teachers
    school_system.add_teacher(101, "Mr. lewis")
    school_system.add_teacher(102, "Ms. Judy")

    # Add classes
    class_start_time = datetime.datetime.now() + datetime.timedelta(minutes=2)
    school_system.add_class(201, "Software Engineering", 101, "Room 101", class_start_time)

    # Add exams
    exam_date = datetime.datetime.now() + datetime.timedelta(days=1)
    school_system.add_exam(301, "Database Programming", exam_date, "Exam Hall")

    # Simulate alerts
    school_system.simulate_class_start_alert(201)
    school_system.simulate_exam_alert(301)

    # Simulate GPS tracker
    student_id = 1
    latitude = 12.3456  # Replace with actual latitude
    longitude = 78.9101  # Replace with actual longitude
    school_system.simulate_gps_tracker(student_id, latitude, longitude)
