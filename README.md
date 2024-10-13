# YouTube Simple Downloader

A straightforward GUI application that allows users to download YouTube videos using Python and the `pytube` library.

## Features

- User-friendly interface to paste a YouTube video link.
- Downloads the video in its default quality.
- Displays a message upon successful download.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)
- `pytube` library

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.x installed on your machine.
3. Install the `pytube` library if you haven't already:

   ```bash
   pip install pytube
   ```

4. Run the script using the command:

   ```bash
   python youtube_simple_downloader.py
   ```

## Usage

1. Launch the application.
2. Paste the YouTube video link into the designated input field.
3. Click the "DOWNLOAD" button to start the download process.
4. Upon successful download, a "DOWNLOADED" message will appear.

## Example

- **Paste Link Here**: `https://www.youtube.com/watch?v=example_video_id`
- After clicking "DOWNLOAD", the video will be saved in the current directory.

## Code Overview

The main functionality of the application is handled by the `Downloader` function, which:

- Retrieves the user-provided link.
- Uses the `pytube` library to download the video.
- Updates the GUI to indicate that the download is complete.

## Error Handling

Currently, the application does not include advanced error handling. If a non-YouTube link or an invalid URL is provided, the application may raise an error. Future improvements could include adding error messages for a better user experience.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions or improvements.

## Acknowledgements

- Thanks to the Python and `pytube` communities for providing resources and documentation.
