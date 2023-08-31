# Simple HTTP Client

This Python script is a basic HTTP client that sends GET requests to a specified URL and processes the responses. It is designed to help you interact with HTTP endpoints and handle JSON responses effectively.

## Prerequisites

Before you can use this script, ensure you have the following prerequisites installed:

- Python
- Requests library (`requests`)
- Pandas library (`pandas`)

## Usage with Docker

Follow these steps to use the `simple_http_client` script:

1. **Clone the Repository:**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/DvdCp/python-http-client.git
   ```

2. **Navigate to the Project Directory:**

   Change to the project directory:

   ```bash
   cd python-http-client
   ```

3. **Build image with Docker**

   Run:

   ```bash
   docker build . --tag python-http-client
   ```

4. **Run the container:**

   Run

   ```bash
   docker run -ti --name python-http-client --network myNet python-http-client
   ```

   This will start a Docker container with an interative terminal (`-ti` flag) and use `myNet` as network

5. **Input and Output:**

   - Enter a string when prompted. The script will construct a URL with the provided string and send a GET request.
   - If the request is successful (status code 200), the script will display the JSON response in a tabular format using Pandas.
   - If the request fails, it will print the status code and any JSON error message.
   - The script will add a new line after every response for readability.

6. **Exit the Script:**

   To exit the script, enter `-1` when prompted.

7. **Conclusion:**

   You have successfully used the `simple_http_client` script to interact with HTTP endpoints and process JSON responses. Customize the script and its usage to fit your specific needs.

## Customization

You can customize the script by:

- Modifying the URL construction logic to target different endpoints.
- Adjusting the error handling and response processing as required.
- Incorporating this script into your own projects or workflows.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, please open an issue or submit a pull request.

---

**Note:** Replace `your-username` and `your-repo` with your actual GitHub username and repository name. Customize the project details and instructions as needed.
