from src.dev_guide import DevGuide

def test_dev_guide_creation():
    dev_guide = DevGuide('Test Guide', 'This is a test guide')
    assert dev_guide.name == 'Test Guide'
    assert dev_guide.description == 'This is a test guide'

def test_dev_guide_to_json():
    dev_guide = DevGuide('Test Guide', 'This is a test guide')
    json_string = dev_guide.to_json()
    assert json_string == '{"name": "Test Guide", "description": "This is a test guide"}'

def test_main():
    # This test is a bit tricky because it involves running the main function
    # We'll just test that it doesn't throw any errors
    import sys
    import io
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    import argparse
    sys.argv = ['dev_guide', '--name', 'Test Guide', '--description', 'This is a test guide']
    from src.dev_guide import main
    main()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() != ''
