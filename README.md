Host Port Scanner and HTTP Info Retriever

This program performs a port scan on a specified host to identify open ports and retrieves HTTP information from port 80 if it is open.
Dependencies

    Python 3.x
    socket and requests libraries (The socket library is included with Python)

You can install the requests library using pip:

bash

pip install requests

Usage

    Copy the code from the program and save it into a file named port_scanner.py.
    Execute the program by running the following command in your terminal:

bash

python port_scanner.py

    When prompted, enter the host name or IP address you wish to scan.

Program Overview

The program performs the following steps:

    Importing Necessary Libraries:
    The required libraries socket and requests are imported for network communication and HTTP requests.

    Defining Functions:
        get_host_by_name(host): Resolves the IP address of a specified host name.
        scan_host(host, port): Scans a specified port on a host to check if it's open.
        get_http_info(host, port): Retrieves HTTP information from a specified host and port.

    Main Execution:
        The main() function prompts the user for a host name or IP address.
        The IP address of the host is resolved using get_host_by_name().
        A loop iterates through ports 1 to 1023, scanning each one on the specified host using scan_host().
        If port 80 is open, HTTP information is retrieved using get_http_info().

Output

The program outputs the status of each port (open or closed) on the specified host. If port 80 is open, it also outputs the HTTP response status code, headers, and content from the host.
