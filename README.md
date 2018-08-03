# seaweed-cli

### Surfline API
Surfline's API is undocumented and unauthenticated, it took some reverse engineering to figure out how it works.
The main Surfline API is here: `http://api.surfline.com/v1/forecasts/<spot_id>` where `spot_id` is a four digit id corresponding to the surf spot

It's difficult to find a spot's `spot_id`, there is no endpoint for retrieving them or any way to search for them. I wasn't willing to dig through HTML on
surfline.com to find the id for every single spot, so I found another option.

There is a way 

There are four 