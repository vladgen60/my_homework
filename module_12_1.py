import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        func_runner1 = Runner.Runner('1')
        for walk in range(10):
            func_runner1.walk()
        self.assertEqual(func_runner1.distance, 50)

    def test_run(self):
        func_runner2 = Runner.Runner('2')
        for run in range(10):
            func_runner2.run()
        self.assertEqual(func_runner2.distance, 100)


    def test_challenge(self):
        func_runner3 = Runner.Runner('3')
        func_runner4 = Runner.Runner('4')
        for walk in range(10):
            func_runner3.walk()
            func_runner4.run()
        for run in range(10):
            func_runner3.walk()
            func_runner4.run()
        self.assertNotEqual(func_runner3.distance, func_runner4.distance)

if __name__ =='__main__':
    unittest.main()