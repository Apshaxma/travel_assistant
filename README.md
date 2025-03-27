
# Travel Assistant

## Overview

The AI Travel Planner is a Streamlit-based web application that generates personalized travel itineraries using Google's Gemini 2.0 Flash model. Users can input their travel preferences, and the AI will create a detailed itinerary, including recommendations for activities, restaurants, and transport options.

## Features

- Select budget type (Low, Moderate, Luxury)
- Input destination and travel dates
- Specify number of travel days
- Define purpose of travel (e.g., adventure, relaxation)
- Add personal preferences (food, activities, etc.)
- AI-generated day-wise itinerary

## Installation

### Prerequisites

Ensure you have Python installed (>= 3.7). Then, install the required dependencies:

```sh
pip install streamlit google-generativeai
```

## Usage

1. Clone or download the repository.
2. Replace `YOUR_GEMINI_API_KEY` in the script with your actual Google Gemini API key.
3. Run the Streamlit app:

```sh
streamlit run your_script.py
```

4. Enter your travel details in the UI and click "Generate Itinerary."

## API Configuration

This application uses Google's `google-generativeai` package to access the Gemini API. Make sure to obtain an API key from Google AI Studio and set it up in the script.

## License

This project is open-source. Feel free to modify and enhance it as needed!

## Contributions

Contributions are welcome! Fork the repository, make changes, and submit a pull request.

