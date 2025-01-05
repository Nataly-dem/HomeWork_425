import pytest
from classTeacher import Teacher


@pytest.fixture
def teacher():
    Teacher.teacher_dict.clear()
    teacher = Teacher('test_name', 'test_education', 'test_experience')
    return teacher

