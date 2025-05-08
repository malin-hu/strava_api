# READ ME

This repo contains code for sending API requests to Strava and creating  visualizations with your running data using Python.

Follow these steps once before running any code:

1. Follow [Strava's instructions](https://developers.strava.com/docs/getting-started/#account) to create an API application.

2. Create a file in your working directory called strava_tokens.json.  Paste the following into the file, replacing the client_id, client_secret, access_token, and refresh_token fields with your own information.  expires_at can be set to any arbitrary number at this point.

```
{
  "client_id": "YOUR_CLIENT_ID_HERE",
  "client_secret": "YOUR_CLIENT_SECRET_HERE",
  "access_token": "YOUR_ACCESS_TOKEN_HERE",
  "refresh_token": "YOUR_REFRESH_TOKEN_HERE",
  "expires_at": 9999999999 // Unix timestamp
}
``` 

Access tokens expire after six hours.  strava_auth.py contains functions that will refresh your access token, if necessary.

Once this set-up is complete, you can start executing code in strava.ipynb.  It begins by fetching your activity data.  This will be saved in a file called strava_activities.json. It will then fetch pace- and heart rate-zone data for each activity.  These zones will be saved in a file called strava_zones.json.  Given Strava API's rate limits, it may take a few days to import your own data.

Here are some fun graphs that you can make that, inexplicatly, you cannot make through Strava itself:

- weekly totals for distance, moving time, elevation gain, and relative effort for a given year (super basic stuff but, again, not possible through Strava)
- weekly total time, split into Strava's pace and heart rate zones (so you can _ex post_ realize that you got injured because you increased both mileage *and* intensity, like an idiot)
- cumulative mileage by year (it's like racing your past self)
- scatterplots so that you can, for instance, see how your average heart rate correlates with average pace or how pace varies with distance (so much bunching!)
- one particular scatterplot that graphs average pace against average heart rate by year (this one really captures how your aerobic fitness has changed over time)
- time series of pace, distance, heart rate, and relative effort

figs.pdf contains examples of these graphs, created using my own running data.