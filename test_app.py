
import unittest
import app


class TestStudentApp(unittest.TestCase):

    def setUp(self):
        app.students.clear()

    def test_add_student(self):
        result = app.add_student(1, "Ravi", 85)
        self.assertEqual(result["name"], "Ravi")

    def test_get_student(self):
        app.add_student(2, "Sita", 90)
        result = app.get_student(2)
        self.assertEqual(result["marks"], 90)

    def test_duplicate_student(self):
        app.add_student(3, "Ravi", 70)
        with self.assertRaises(ValueError):
            app.add_student(3, "Sita", 80)

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            app.add_student(4, "Ravi", 120)

    def test_calculate_grade(self):
        self.assertEqual(app.calculate_grade(95), "A")
        self.assertEqual(app.calculate_grade(80), "B")
        self.assertEqual(app.calculate_grade(60), "C")
        self.assertEqual(app.calculate_grade(30), "F")


if __name__ == "__main__":
    unittest.main()
