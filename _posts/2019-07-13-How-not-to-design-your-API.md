---
title: How not to design your API OR How I stopped worrying and learned to love being
  in different locations on Tinder without paying.
layout: post
sidebar_link: true
tags:
- Security
- API
- Bugs
- Tinder
- API Design
---

This is the first POST request you send when you login to your profile on Tinder's web UI.
![first_post.png](/images/tinde/first_post.png)

Notice something interesting? Yep, you are sending your **Latitude and Longitude** through tinder's obscure API.  Now as a simple yet curious person you copy the entire request in the terminal from devtools as a curl command looking roughly like this:
```
curl 'https://api.gotinder.com/v2/meta?locale=en'  ... -H 'TE: Trailers' --data '{"
lat":29.946552999999998,"lon":77.5462818,"force_fetch_resources":true}'
```

Well now you have a POST request all ready to fire at Tinder. What if we change the location a little bit? What if let's say, we get co-ordinates of **Tokyo** and put it in there. Our new curl request would look somewhat like this:
```
curl 'https://api.gotinder.com/v2/meta?locale=en'  ... -H 'TE: Trailers' --data '{"
lat":35.682838799999999,"lon":139.7594549"force_fetch_resources":true}'
```

Now we just fire it and wait for the browser and server caches to clear up. Second step? Just refresh the page or tweak any settings on the page like distance etc for tinder to set you up at the location you have beamed at it and off you go to places and people you'd have to usually pay for!

NOTE: Not including any more screenshots because privacy.

NOTE-2: I have fuzzed enough to realise that the latitude and the longitude values specifically have to be 14 and 7 decimal digits for the server to parse it correctly. 

NOTE-3: Who knows what more can be changed through simple requests without having proper checks for account privilege on the server side.