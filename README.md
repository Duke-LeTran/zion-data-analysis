# zion-data-analysis

Upon my research in preparation for our Top-Down, single-day 16-mile trek through the Zion Narrows, I found that the U.S. Geological Survey (USGS) publishes their data publicly in tab-delimited csv format. To test my knowledge of python, the [pandas](https://pandas.pydata.org/), and [seaborn](https://seaborn.pydata.org/), I decided to do some exploratory analysis.

Below you will find the water flow measured in Cubic Feet per Second (CFS) plotted by month. The first set of graphs are the median water flow, and the second set of graphs are the 95 percentile water flow. The first set of graphs describe median water flow behavior by months, and the latter set of graphs describe possible erratic water flow behavior by months. As a general reference, 50 CFS indicates relatively easy hiking; 100 CFS indicates difficult and dangerous conditions; 120 CFS or higher indicates that the National Park Service (NPS) will no longer issue permits.

We see that though past historical data is can be a wonderful predictor, there will always be outlier events. For example, based on the median water flow graphs, we see that July & August are by far the safest times to visit the Narrows of Zion. However, by concidental happenstance, we see that in this past July 2018 a [flash flood occured](https://www.usnews.com/news/best-states/utah/articles/2018-07-19/trails-closed-due-to-flash-floods-at-zion-national-park), forcing the National Park Service (NPS) to close mutiple trails, including the most famous Angel's Landing. Though the recent flash flood this past summer was likely a statistical outlier, it goes with out saying that one should always respect the power of mother nature. Always be prepared for worst.

See exploratory data analysis below. Maps are generated via [Caltopo](https://caltopo.com/m/8CKK). Also note, the NPS may have stopped issuing wilderness permits for the Top-Down Narrows hike, both for day and overnight trips due to a disagreement with landowners near the trailhead which starts on private land. Please respect boundaries and check with the NPS for both rules and current conditions. Disclaimer: your safety is your own responsibility; your adherence to existing and current rules is your representation of us as a hiking community. Additionally, I hope this goes without saying -- [leave no trace!](https://lnt.org/learn/seven-principles-overview).

I hope you find this repository informative and useful!

## Median Water Flow By Month
![p50](https://github.com/Duke-LeTran/zion-data-analysis/blob/master/output/zion-by-month-p50.png)

## 95 percentile Water Flow by Month
![p95](https://github.com/Duke-LeTran/zion-data-analysis/blob/master/output/zion-by-month-p95.png)