from django.db import models
import datetime

class Semester(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(default=datetime.datetime.now().year)
    semester = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.year}-{'Spring' if self.semester == 1 else 'Fall'}"
    def create_semester(cls, year, semester):
        semester = cls(year=year, semester=semester)
        semester.save()
        return semester

    def update_semester(self, year, semester):
        self.year = year
        self.semester = semester
        self.save()

    def delete_semester(self):
        self.delete()

    def get_semester(cls, year, semester):
        return cls.objects.get(year=year, semester=semester)

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    # lecturer = models.ManyToManyField('Lecturer',related_name='courses')
    semesters = models.ManyToManyField(Semester, blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
    def create(cls, code, name):
        course = cls(code=code, name=name)
        course.save()
        return course

    def update(self, code=None, name=None):
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        self.save()

    def delete(self):
        super().delete()            
            
    def getCourse(cls, course_id):
        try:
           course_obj= cls.objects.get(id=course_id)
        except cls.DoesNotExist:
            return None
        return course_obj


class Class(models.Model):
    number = models.IntegerField(default=1)
    id = models.AutoField(primary_key=True)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey('Lecturer', on_delete=models.CASCADE)
    def create(cls, number, semester, course, lecturer):
        class_obj = cls(number=number, semester=semester, course=course, lecturer=lecturer)
        class_obj.save()
        return class_obj

    def delete(cls, class_id):
        try:
            class_obj = cls.objects.get(id=class_id)
        except cls.DoesNotExist:
            return False
        class_obj.delete()
        return True

    def update(self, number=None, semester=None, course=None, lecturer=None):
        if number is not None:
            self.number = number
        if semester is not None:
            self.semester = semester
        if course is not None:
            self.course = course
        if lecturer is not None:
            self.lecturer = lecturer
        self.save()

    def get_class(cls, class_id):
        try:
            class_obj = cls.objects.get(id=class_id)
        except cls.DoesNotExist:
            return None
        return class_obj


class Lecturer(models.Model):
    staffId = models.IntegerField(default=0)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    classes = models.ManyToManyField(Class,related_name='lecturers')
    course = models.ManyToManyField(Course,related_name='courses')
   
    def create_lecturer(staff_id, first_name, last_name, email):
      lecturer = Lecturer.objects.create(staffId=staff_id, firstname=first_name, lastname=last_name, email=email)
      return lecturer
    
    def delete_lecturer(self):
      self.delete()

    def update_lecturer(self, staff_id=None, first_name=None, last_name=None, email=None):
        if staff_id:
            self.staffId = staff_id
        if first_name:
            self.firstname = first_name
        if last_name:
            self.lastname = last_name
        if email:
            self.email = email
        self.save()
    def get_lecturer(cls, staff_id):
        try:
            lecturer = cls.objects.get(id=staff_id)
        except cls.DoesNotExist:
            return None
        return lecturer


class Student(models.Model):
    studentID = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    DOB = models.DateField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def create_student(cls, studentID, first_name, last_name, email, DOB):
        student = cls(studentID=studentID, first_name=first_name, last_name=last_name, email=email, DOB=DOB)
        student.save()
        return student

    def update_student(self, studentID, first_name, last_name, email, DOB):
        self.studentID = studentID
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.DOB = DOB
        self.save()

    def delete_student(self):
        self.delete()

    def get_student(cls, studentID):
        try:
           student= cls.objects.get(studentID=studentID)
        except cls.DoesNotExist:
            return None
        return student


class StudentEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    studentId = models.IntegerField(default=0)
    classId = models.IntegerField(default=0)
    grade = models.CharField(max_length=100)
    enrollTime = models.DateField(auto_created=True)
    gradeTime = models.DateField()

    def create(cls, student, enrolled_class, studentId, classId, grade, enrollTime, gradeTime):
        enrollment = cls(student=student, enrolled_class=enrolled_class, studentId=studentId, classId=classId, grade=grade, enrollTime=enrollTime, gradeTime=gradeTime)
        enrollment.save()
        return enrollment

    def delete(self):
        self.delete()

    def update(self, student=None, enrolled_class=None, studentId=None, classId=None, grade=None, enrollTime=None, gradeTime=None):
        if student is not None:
            self.student = student
        if enrolled_class is not None:
            self.enrolled_class = enrolled_class
        if studentId is not None:
            self.studentId = studentId
        if classId is not None:
            self.classId = classId
        if grade is not None:
            self.grade = grade
        if enrollTime is not None:
            self.enrollTime = enrollTime
        if gradeTime is not None:
            self.gradeTime = gradeTime
        self.save()

    def get_enrollment(cls, enrollment_id):
        try:
            enrollment = cls.objects.get(id=enrollment_id)
        except cls.DoesNotExist:
            return None
        return enrollment
