# DisasterIntelligence Earthquake Guidance Prediction API #
The DisasterIntelligence Earthquake Guidance Prediction API provides the earthquake prediction data opened for public use with up to **70%** of theoretical prediction accuracy. The historical data that is also used as an input to the prediction algorithm is from *United States Geological Survey*. Some of the data is also **openly available** in CSV format for easier re-use.

## Continent Codes ##
Place any these continent legends in {{Continent}} to obtain data for that continent.

| Legend | Continent |
|--------|-----------|
| Af     | Africa    |
| Au     | Australia |
| As     | Asia      |
| Eu     | Europe    |
| Na     | North America |
| Sa     | South America |
| Oc     | The Oceans |

## Historical Heatmaps ##
Historical heatmaps show all **recorded** occurence of earthquakes over the **period of past 100 years** that is **at least the magnitude of 4** on the richter scale. The data on the map is also displayed using the richter scale.

The historical heatmaps data is available in *Google Maps*' static maps. To obtain heatmap, use

```
GET /{{Continent}}G
```

For example, to obtain the data for *North America*, use

```
GET /NaG
```

### Global Heatmaps ###
To obtain the global historical heatmaps shown by **countries**, use

```
GET /DashG
```

### In CSV ###
To get the historical heatmaps data in CSV format, use

```
GET /{{Continent}}_graph_csv 
GET /dash_graph_csv
```

## Prediction Result in CSV ##
> **Please note:** While the mathematical accuracy of the prediction is theoretically up to 70%, the prediction provided here is for guidance purpose only. We don't take any responsibility for any mistake in the prediction. The prediction provided here is in date and predicted magnitude format.

> For web-based prediction service, please use '/service'.

To get prediction result of a country, use
```
GET /result/{{Countrycode}}_{{Year}}_{{Month}}.CSV
```
Where year is in the range of the present year to the next ten years (e.g. 2016-2026), and month is in the range of 1 to 12, and countrycode is one of the following:
### Countrycodes ###

| Countrycode | Country |
|-----|-------------|
| 0   | Afghanistan |
| 1   | Albania |
| 2   | Algeria |
| 3   | Andorra |
| 4   | Angola |
| 5   | Anguilla |
| 6   | Antarctica |
| 7   | Antigua and Barbuda |
| 8   | Argentina |
| 9   | Armenia |
| 10   | Aruba |
| 11   | Australia |
| 12   | Austria |
| 13   | Azerbaijan |
| 14   | Bahamas |
| 15   | Bahrain |
| 16   | Bangladesh |
| 17   | Barbados |
| 18   | Belarus |
| 19   | Belgium |
| 20   | Belize |
| 21   | Benin |
| 22   | Bermuda |
| 23   | Bhutan |
| 24   | Bolivia |
| 25   | Bosnia and Herzegovina |
| 26   | Botswana |
| 27   | Brazil |
| 28   | British Virgin Islands |
| 29   | Brunei Darussalam |
| 30   | Bulgaria |
| 31   | Burkina Faso |
| 32   | Burundi |
| 33   | Cambodia |
| 34   | Cameroon |
| 35   | Canada |
| 36   | Cape Verde |
| 37   | Cayman Islands |
| 38   | Central African Republic |
| 39   | Chad |
| 40   | Chile |
| 41   | China |
| 42   | Christmas Island |
| 43   | Cocos Islands |
| 44   | Colombia |
| 45   | Comoros |
| 46   | Congo |
| 47   | Cook Islands |
| 48   | Costa Rica |
| 49   | Croatia |
| 50   | Cuba |
| 51   | Curacao |
| 52   | Cyprus |
| 53   | Czech Republic |
| 54   | Denmark |
| 55   | Djibouti |
| 56   | Dominica |
| 57   | Dominican Republic |
| 58   | East Timor |
| 59   | Ecuador |
| 60   | Egypt |
| 61   | El Salvador |
| 62   | Equatorial Guinea |
| 63   | Eritrea |
| 64   | Estonia |
| 65   | Ethiopia |
| 66   | Federated States of Micronesia |
| 67   | Fiji |
| 68   | Finland |
| 69   | France |
| 70   | French Southern and Antarctic Lands |
| 71   | Gabon |
| 72   | Georgia |
| 73   | Germany |
| 74   | Ghana |
| 75   | Greece |
| 76   | Greenland |
| 77   | Grenada |
| 78   | Guam |
| 79   | Guatemala |
| 80   | Guinea |
| 81   | Haiti |
| 82   | Honduras |
| 83   | Hungary |
| 84   | Iceland |
| 85   | India |
| 86   | Indonesia |
| 87   | Iran |
| 88   | Iraq |
| 89   | Israel |
| 90   | Italy |
| 91   | Ivory Coast |
| 92   | Jamaica |
| 93   | Japan |
| 94   | Jersey |
| 95   | Jordan |
| 96   | Kazakhstan |
| 97   | Kenya |
| 98   | Kinshasa |
| 99   | Kosovo |
| 100   | Kuwait |
| 101   | Kyrgyzstan |
| 102   | Laos |
| 103   | Lebanon |
| 104   | Lesotho |
| 105   | Liberia |
| 106   | Libya |
| 107   | Liechtenstein |
| 108   | Luxembourg |
| 109   | Macedonia |
| 110   | Madagascar |
| 111   | Malawi |
| 112   | Malaysia |
| 113   | Mali |
| 114   | Mauritania |
| 115   | Mexico |
| 116   | Moldova |
| 117   | Monaco |
| 118   | Mongolia |
| 119   | Montenegro |
| 120   | Montserrat |
| 121   | Morocco |
| 122   | Mozambique |
| 123   | Myanmar |
| 124   | Namibia |
| 125   | Nepal |
| 126   | Netherlands |
| 127   | New Caledonia |
| 128   | New Zealand |
| 129   | Nicaragua |
| 130   | Nigeria |
| 131   | North Korea |
| 132   | Northern Cyprus |
| 133   | Northern Mariana Islands |
| 134   | Norway |
| 135   | Pakistan |
| 136   | Panama |
| 137   | Papua New Guinea |
| 138   | Paraguay |
| 139   | Peru |
| 140   | Philippines |
| 141   | Poland |
| 142   | Portugal |
| 143   | Puerto Rico |
| 144   | Republic of Serbia |
| 145   | Republic of the Congo |
| 146   | Romania |
| 147   | Russia |
| 148   | Rwanda |
| 149   | Saint Kitts and Nevis |
| 150   | Saint Lucia |
| 151   | Saudi Arabia |
| 152   | Siachen Glacier |
| 153   | Slovakia |
| 154   | Slovenia |
| 155   | Solomon Islands |
| 156   | Somalia |
| 157   | Somaliland |
| 158   | South Africa |
| 159   | South Georgia and South Sandwich Islands |
| 160   | South Korea |
| 161   | South Sudan |
| 162   | Spain |
| 163   | Sudan |
| 164   | Swaziland |
| 165   | Sweden |
| 166   | Switzerland |
| 167   | Syria |
| 168   | Taiwan |
| 169   | Tajikistan |
| 170   | Thailand |
| 171   | Tonga |
| 172   | Trinidad and Tobago |
| 173   | Tunisia |
| 174   | Turkey |
| 175   | Turkmenistan |
| 176   | Uganda |
| 177   | Ukraine |
| 178   | United Arab Emirates |
| 179   | United Kingdom |
| 180   | United Republic of Tanzania |
| 181   | United States Virgin Islands |
| 182   | United States of America |
| 183   | Uzbekistan |
| 184   | Vanuatu |
| 185   | Venezuela |
| 186   | Vietnam |
| 187   | West Bank |
| 188   | Yemen |
| 189   | Zambia |
| 190   | Zimbabwe |

## Graphs ##
There are many kind of ready-for-use graphs available in the API.

### Graphcodes ###
Listed here is the list of available graphs, and their graphcodes.

| Graphcode | Graph |
|------------|-------|
| 2 | Magnitude Range Pie Chart |
| 3 | Depth Range Pie Chart |
| 4 | Magnitude v. Frequency Histogram |
| 5 | Depth v. Frequency Histogram |
| 6 | Magnitude Range v. Frequency Table |
| 7 | Depth Range v. Frequency Table |
| 8 | Top 5 Countries Table |
| 9 | Magnitude v. Depth v. Frequency Chart |

To query for ready-for-use graphs, use
```
GET /{{Continent}}G{{Graphcode}}
```

For example, to query for Africa's Depth Range Pie Chart, use
```
GET /AfG3
```

### In CSV ###
The raw graphs data is also available in CSV format for easier reuse, to get graph data in CSV format, use
```
GET /{{Continent}}{{Graphcode}}_graph_csv
```
> **Note:** CSV format available only for **graphcode ranging from 2 to 5.**

## Daily Earthquake Frequency Calendars ##
We have ready-for-use calendars of daily earthquake frequency from **1900 to present** available. To query for the ready-for-use calendar, use
```
GET /C{{FromYear}}_{{ToYear}}
```

Where FromYear and ToYear can be one of the following pairs:

| FromYear | ToYear |
|----------|--------|
| 1900 | 1910 |
| 1910 | 1920 |
| 1920 | 1930 |
| 1930 | 1940 |
| 1940 | 1950 |
| 1950 | 1960 |
| 1960 | 1970 |
| 1970 | 1980 |
| 1980 | 1990 |
| 1990 | 2000 |
| 2000 | 2010 |
| 2010 | 2020* |

> **Note*:** The data will only be displayed from 2010 to the present day.

### In CSV ###
The daily earthquake frequecy calendar is also available in the CSV format, to query all the data from 1900 to present day, simply use
```
GET /cal_csv
```

## Magnitude v. Depth Maps ##
We also have the ready-for-use map of depths grouped by range of magnitude, to query, use
```
GET /C{{FromMagnitude}}_{{ToMagnitude}}
```
Where FromMagnitude and ToMagnitude is one of the following pairs:

| FromMagnitude | ToMagnitude |
|---------------|-------------|
| 4 | 5 |
| 5 | 6 |
| 6 | 7 |
| 7 | 8 |
| 8 | 9 |

### In CSV ###
To get the Magnitude v. Depth Maps in CSV format, use
```
GET /C{{FromMagnitude}}_{{ToMagnitude}}_csv
```

## Coordinates and magnitude ##
To query for coordinates and magnitude maps, use
```
GET /llN
```

### In CSV ###
For the coordinates and magnitude maps in CSV format, use
```
GET /llN_csv
```

## Top 5 Maps ##
For the ready-for-use top 5 earthquakes maps, use
```
GET /InG
```
