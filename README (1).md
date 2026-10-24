# Weather Dashboard

A small Python terminal app that looks up the current temperature for a city or town using Open-Meteo.

## How it works

- Takes a place name from the user.
- Looks up its latitude and longitude.
- Uses those coordinates to request the current temperature.
- Prints the temperature and its unit.

```text
The temperature in Bath is 11.8°C
```

Example output only; results depend on the location and weather.

## Run it

You need Python 3 and an internet connection. With the script saved as `main.py`, run these commands from the project folder:

```bash
python -m pip install requests
python main.py
```

## What I learned

This was my first project using APIs. I built it with AI guidance to move beyond basic input and output programs.

I practised sending requests, converting JSON into Python data, and reading nested dictionaries and lists. The hardest part was understanding which keys to use and the difference between a response object and the data inside it. I needed help with those parts and am still practising them.

## Still to do

The app uses the first matching location and doesn't handle invalid places or failed requests yet. Next, I'd like to add error handling and more weather details.

Weather data provided by [Open-Meteo](https://open-meteo.com/).
