# Weather App

A simple Flask-based web application that displays current weather information for any city using the OpenWeatherMap API.

## Features

- Search weather by city name
- Display current temperature, weather description, humidity, pressure, and wind speed
- Responsive web interface
- Weather icons from OpenWeatherMap
- Error handling for invalid cities and API errors

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- An OpenWeatherMap API key (free tier available at https://openweathermap.org/api)

## Installation

1. Navigate to the project directory:
   ```bash
   cd weather_app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your OpenWeatherMap API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Enter a city name in the search box to view its weather information.

## Project Structure

```
weather_app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css       # CSS styling
└── templates/
    └── index.html      # HTML template
```

## Dependencies

- **Flask** - Web framework
- **requests** - HTTP library for API calls
- **python-dotenv** - Environment variable management

See `requirements.txt` for version details.

## API Information

This application uses the OpenWeatherMap API:
- **Endpoint**: https://api.openweathermap.org/data/2.5/weather
- **Documentation**: https://openweathermap.org/current

## License

This project is open source and available under the MIT License.
