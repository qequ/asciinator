# Asciinator

Asciinator is a command-line tool that converts images and GIFs into ASCII art. It's a simple yet powerful tool for creating text-based representations of your favorite images and animations.

## Installation

Asciinator is developed in Python and can be installed via Poetry. To install Asciinator, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/asciinator.git
    ```

2. Navigate to the cloned repository:

    ```bash
    cd asciinator
    ```

3. Install using Poetry:

    ```bash
    poetry install
    ```

## Usage

After installation, Asciinator can be used directly from the command line. Here are some example commands:

    To convert a regular image to ASCII and display it in the console:

    
```bash
asciinator /path/to/image.jpg
```
To convert a regular image to ASCII and save it to a file:

```bash

asciinator /path/to/image.jpg --output output.txt
```

To convert a GIF to an ASCII animation and save it as a GIF:

```bash

asciinator /path/to/animation.gif --gif --output ascii_animation.gif
```

Use the --width argument to specify the output width of the ASCII art (default is 100 characters).

## Contributing

Contributions to Asciinator are welcome! Feel free to fork the repository, make changes, and submit pull requests. If you encounter any issues or have suggestions, please open an issue in the GitHub repository.
## License

This project is licensed under the MIT License.
## Contact

For any inquiries or suggestions, please contact Alvaro Frias Garay at alvarofriasgaray@gmail.com.