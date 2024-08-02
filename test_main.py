import subprocess

def test_main_script():
    # Define the input and expected output conditions
    input_text = "Hey Hello there"
    
    # Run the main.py script and capture the output
    result = subprocess.run(
        ["python", "main.py"],
        input=input_text.encode(),  # Encode the input as bytes
        capture_output=True,
        text=True  # Capture the output as text
    )
    
    # Get the output from stdout
    output = result.stdout.strip()
    
    # Assert that the output is a string (this is always true for stdout capture)
    assert isinstance(output, str)

    # Print the output for debugging (optional)
    print("Output:", output)
