from abc import abstractmethod, ABC
class Person(ABC):
    def __init__(self, name,yob):
        self._name = name
        self._yob = yob

    @abstractmethod
    def display(self):
        '''
            When parent class have abstract methods, child class must be implement this method
        '''
        pass

class Student(Person):
    """
        Class Student: 
            >> st1 = Student("Student 1", 1996, 28)
    """
    def __init__(self, name, yob, grade):
        super().__init__(name,yob)
        self.__grade = grade

    def display(self):
        print(f'{Student.__name__} - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}')

class Teacher(Person):
    """
        Teacher Class:
            tc2 = Teacher("Teacher 2", 1995, "Physical")
            
    """
    def __init__(self, name,yob, subject):
        super().__init__(name,yob)
        self.__subject = subject

    def display(self):
        print(f'{Teacher.__name__} - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}')

class Doctor(Person):
    """
        Docker Class: 
            dt1 = Doctor("Doctor 1", 1980, "General")
    """
    def __init__(self, name, yob, special):
        super().__init__(name, yob)
        self.__special = special

    def display(self):
        print(f'{Doctor.__name__} - Name: {self._name} - YoB: {self._yob} - specialist: {self.__special}')


class Ward():
    """
        Ward class consist Person, Teacher, Doctor
    
    """
    def __init__(self, name):
        self.__name = name
        self.__list_person = []

    def add_person(self, _person):
        if isinstance(_person, Person) and _person not in self.__list_person:
            self.__list_person.append(_person)

        else:
            message = "Person invalid! (Maybe not person or person already exists in list person)"
            print(message)

    def remove_person(self, _person):
        self.__list_person.remove(_person)

    def describe(self):
        print(f"Ward name: {self.__name}")
        for person in self.__list_person:
            person.display()

    def count_doctor(self):
        list_teacher = [x for x in self.__list_person if isinstance(x, Doctor)]
        print(f'Number of Docter in Ward: {len(list_teacher)}')
        return len(list_teacher)

    def sort_age(self):
        '''Sorting with Longevity inrcreasing '''
        copy= self.__list_person.copy()
        copy.sort(key=lambda x: x._yob, reverse = True)
        return copy

    def compute_average_teacher_age(self):
        sum_age = 0
        list_teacher = [x for x in self.__list_person if isinstance(x, Teacher)]
        sum_age += sum([x._yob for x in list_teacher])
        if sum_age == 0:
            print("Have no teacher in ward")
        else:
            print(f'Average age of teacher is {sum_age/len(list_teacher)}')
        return sum_age / len(list_teacher)
    

if __name__ == "__main__":
    # Testing 
    dt = Doctor("kt", 1299, "khoa")
    dt.display()

    st1 = Student("Student 1", 1996, "28")
    st1.display()

    tc1 = Teacher("Teacher 1", 1990, "Math")
    tc1.display()

    # Adding object into class
    st1 = Student("Student 1", 1996, 28)
    tc1 = Teacher("Teacher 1", 1990, "Math")
    tc2 = Teacher("Teacher 2", 1995, "Physical")
    dt1 = Doctor("Doctor 1", 1980, "General")
    dt2 = Doctor("Doctor 2", 1985, "Endocrinologists")

    ward = Ward("ward 1")

    ward.add_person(st1)
    ward.add_person(tc1)
    ward.add_person(tc2)
    ward.add_person(dt1)
    ward.add_person(dt2)

    ward.describe()

    # Count number of Doctor
    ward.count_doctor()

    # Sort Age 
    a = ward.sort_age()
    for i in a:
        i.display()

    # Compute Average age
    ward.compute_average_teacher_age()

