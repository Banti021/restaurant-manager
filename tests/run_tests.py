import os
import sys
import coverage
import unittest


def run_tests():
    # Start coverage
    cov = coverage.Coverage()
    cov.start()

    # Discover and run tests
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(start_dir, '..')  # Go one level up to include the tests directory

    print(f"Starting test discovery in directory: {tests_dir}")  # Debugging statement

    # Verify the tests directory exists
    if not os.path.isdir(tests_dir):
        print(f"Error: The tests directory '{tests_dir}' does not exist.")
        return 1

    # Discover tests using pattern 'test_*.py' in all subdirectories
    suite = loader.discover(tests_dir, pattern='test_*.py')
    print(f"Discovered tests: {suite.countTestCases()}")  # Debugging statement

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Stop coverage and save data
    cov.stop()
    cov.save()

    # Create report directory if it doesn't exist
    report_dir = os.path.join(start_dir, 'report')
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Report coverage
    print("\nCoverage Report:\n")
    cov.report()

    # Generate HTML coverage report in the 'report' directory
    cov.html_report(directory=os.path.join(report_dir, 'htmlcov'))
    print(f"\nHTML version: {os.path.join(report_dir, 'htmlcov', 'index.html')}")

    # Generate XML coverage report in the 'report' directory (optional, useful for CI tools)
    cov.xml_report(outfile=os.path.join(report_dir, 'coverage.xml'))
    print(f"\nXML version: {os.path.join(report_dir, 'coverage.xml')}")

    # Save coverage data file in the 'report' directory
    cov.save()
    os.rename('.coverage', os.path.join(report_dir, '.coverage'))

    # Return appropriate exit code
    return len(result.failures) + len(result.errors)


if __name__ == '__main__':
    sys.exit(run_tests())
