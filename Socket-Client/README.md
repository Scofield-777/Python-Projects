# Simple Python Socket Client

## Description

This project is a basic Python socket client that establishes a connection to a server, sends a message, receives a response, and then closes the connection. This can be useful for understanding basic socket programming in Python and for learning how to handle TCP connections.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/simple-python-socket-client.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd simple-python-socket-client
    ```

3. **Ensure you have Python installed:**

    - This script is compatible with Python 2. Ensure you have Python 2 installed on your machine.

## Usage

1. **Modify the IP address:**

    Edit the script to include the target IP address:

    ```python
    connection.connect(("TARGET_IP", 4444))
    ```

2. **Run the script:**

    ```bash
    python socket_client.py
    ```

3. **Expected Output:**

    Upon running, the script will connect to the specified server, send a message indicating that the connection has been established, receive a response from the server, print the received message, and then close the connection.

    Example output:

    ```text
    [+]Connection Established.
    Server Response: [Response from the server]
    ```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
