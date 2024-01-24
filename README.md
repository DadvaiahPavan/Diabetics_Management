# Diabetes Management Project

This project aims to assist individuals with diabetes in managing their diet by leveraging Google's Gemini Pro Vision API. The system analyzes input images of various food items, identifies the type of food, and determines its glycemic index. Based on this information, it provides recommendations on whether the detected food is suitable for individuals with diabetes and specifies the recommended quantity for consumption.

## Overview

The Diabetes Management system utilizes the following technologies:

- **Google's Gemini Pro Vision API:** The generative model is employed to analyze and interpret images of food items, providing valuable insights into their identity and glycemic index.

- **Gradio Library:** The user interface is created using Gradio, making it easy to upload food images, interact with the model, and receive recommendations.

## Installation

1. Install the required Python packages:

    ```bash
    pip install google-generativeai==0.3.1 gradio
    ```

2. Set up your Gemini API key by replacing `"YOUR_GEMINI_API_KEY"` in the code.

3. Run the `app.py` script:

    ```bash
    python app.py
    ```

## Usage

1. Open the provided Colab notebook or run the Python script locally.

2. Follow the prompts in the Gradio interface to upload an image of the food you want to analyze.

3. Receive recommendations on whether the detected food is suitable for individuals with diabetes and get specified quantities for consumption.

## Troubleshooting

- If you encounter issues with antivirus software flagging Gradio-related files, consider adding exclusions or temporarily disabling real-time scanning.

## Contributions

Contributions to this project are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

