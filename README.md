403-Unlocker

403-Unlocker is a versatile tool designed to assist in bypassing poorly secured endpoints that return a 403 Forbidden status code. It leverages various techniques to enhance accessibility and uncover potential vulnerabilities in restricted endpoints.

Features

Path Fuzzing: Test various URL paths to identify accessible endpoints.

HTTP Methods Fuzzing: Try different HTTP methods (GET, POST, PUT, etc.) to bypass restrictions.

Request Headers Fuzzing: Experiment with custom headers to gain access.

URL Encoding and Double Encoding: Test for vulnerabilities using encoded URLs.

Combination Techniques: Apply multiple bypass methods simultaneously.

Ease of Use: Intuitive command-line interface for efficient operation.



Usage

To use 403-Unlocker, follow these steps:

Navigate to the tool’s directory.

Execute the following command:

./403-Unlocker [Target_URL] [Option]

Options

Option

Description

-c

Combine multiple techniques simultaneously

-p

Perform URL path fuzzing

-h

Perform request header fuzzing

-u

Fuzz the User-Agent header

--all

Execute all available techniques

--help

Display the help menu

-v

Suppress the testing progress output

Installation

Follow these steps to install 403-Unlocker:

Ensure Python 3 is installed on your machine. You can check by running:

python3 --version

Clone the repository:

git clone https://github.com/Mazenbimbo/403-Unlocker.git

Navigate to the tool’s directory:

cd 403-Unlocker

Example Usage

To test a target URL with all available techniques:

./403-Unlocker https://example.com --all

To perform URL path fuzzing only:

./403-Unlocker https://example.com -p

Contributing

Contributions are welcome! If you find a bug or have suggestions for improvement, feel free to open an issue or submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

