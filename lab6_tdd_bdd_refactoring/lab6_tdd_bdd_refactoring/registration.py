MAX_HOURS = 18


class RegistrationError(Exception):
    """Raised when a course registration action violates a rule."""


class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.courses = {}

    @property
    def total_hours(self):
        return sum(self.courses.values())

    def register(self, code, hours):
        if code in self.courses:
            raise RegistrationError(f"{code} is already registered")
        if not isinstance(hours, int) or hours <= 0:
            raise RegistrationError("credit hours must be a positive integer")
        if self.total_hours + hours > MAX_HOURS:
            raise RegistrationError("credit-hour limit is 18")
        self.courses[code] = hours

    def drop(self, code):
        if code not in self.courses:
            raise RegistrationError(f"{code} is not registered")
        del self.courses[code]
