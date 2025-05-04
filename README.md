# Hadoop MapReduce: City-Wise Profit & Loss Analysis

This project uses the Hadoop MapReduce framework to process a JSON-based dataset and compute the number of profitable and loss-making stores in different cities.

## 🚀 Overview

- Input: JSON dataset containing store-level profit data with associated city names.
- Output: Count of stores in profit and loss per city.
- Tools: Hadoop Streaming, Python (for mapper and reducer).

## 🛠️ Tech Stack

- **Hadoop** (Streaming)
- **Python** (Mapper and Reducer scripts)
- **JSON** as the data format# hadoop-mapreduce-city-profit-analysis
This project uses the Hadoop MapReduce framework to process a JSON-based dataset and compute the number of profitable and loss-making stores in different cities.


## 🧠 How It Works

1. **Mapper**: Parses each line of the JSON dataset and emits city + profit/loss status.
2. **Reducer**: Groups by city and tallies the count of profitable vs loss-making stores.
3. Results are output in the format:
CityName ProfitableCount LossMakingCount


## 🏃‍♂️ Execution (Hadoop Streaming CLI)

```bash
hadoop jar $HADOOP_STREAMING \
 -input /path/to/input \
 -output /path/to/output \ 
 -mapper "python3 mapper.py" \
 -reducer "python3 reducer.py" \
 -file mapper.py \
 -file reducer.py
```

## 📊 Sample Output ( small data )
```bash
{"city": "Ahmedabad", "profit_stores": 3, "loss_stores": 5}
{"city": "Bangalore", "profit_stores": 5, "loss_stores": 3}
{"city": "Chennai", "profit_stores": 3, "loss_stores": 5}
{"city": "Delhi", "profit_stores": 3, "loss_stores": 4}
{"city": "Hyderabad", "profit_stores": 3, "loss_stores": 5}
{"city": "Jaipur", "profit_stores": 3, "loss_stores": 5}
{"city": "Kanpur", "profit_stores": 0, "loss_stores": 8}
{"city": "Kolkata", "profit_stores": 8, "loss_stores": 1}
{"city": "Lucknow", "profit_stores": 8, "loss_stores": 0}
{"city": "Mumbai", "profit_stores": 4, "loss_stores": 4}
{"city": "Pune", "profit_stores": 2, "loss_stores": 5}
{"city": "Surat", "profit_stores": 3, "loss_stores": 5}
```


## 📊 Sample Output ( big data )
```bash
{"city": "Adoni", "profit_stores": 1283, "loss_stores": 1285}	
{"city": "Ahmadabad", "profit_stores": 1291, "loss_stores": 1314}	
{"city": "Amaravati", "profit_stores": 1253, "loss_stores": 1250}	
{"city": "Ambala", "profit_stores": 1291, "loss_stores": 1258}	
{"city": "Ambikapur", "profit_stores": 1297, "loss_stores": 1346}	
{"city": "Amreli", "profit_stores": 1308, "loss_stores": 1251}	
{"city": "Anantapur", "profit_stores": 1267, "loss_stores": 1239}	
{"city": "Anantnag", "profit_stores": 1324, "loss_stores": 1264}	
{"city": "Ara", "profit_stores": 1313, "loss_stores": 1302}	
{"city": "Baramula", "profit_stores": 1292, "loss_stores": 1248}	
{"city": "Barauni", "profit_stores": 1246, "loss_stores": 1305}	
{"city": "Begusarai", "profit_stores": 1175, "loss_stores": 1254}	
{"city": "Bengaluru", "profit_stores": 1229, "loss_stores": 1184}	
{"city": "Bettiah", "profit_stores": 1237, "loss_stores": 1230}	
{"city": "Bhagalpur", "profit_stores": 1248, "loss_stores": 1258}
```

## 📌 Notes

  Make sure the JSON is newline-delimited (.jsonl format works best).

  Python 3+ is recommended.

  You can extend this to compute average profit/loss, top-performing cities, etc.
