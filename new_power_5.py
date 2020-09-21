import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd

# Load and clean data
stats = pd.read_csv('./data/ncaa_stats.csv', header=0)
stats = stats.loc[:, ~stats.columns.str.contains('^Unnamed')]
stats.dropna(inplace=True)

# Dataframe with desired features
df = stats[['point_spread_pg', 'win_pct', 'off_rank',
            'def_rank', 'yard_spread_pg'
            ]]

vals = df.values
scaler = preprocessing.MinMaxScaler()  # Initialize min-max scaler
x_scaled = scaler.fit_transform(vals)  # Scale features
df_scaled = pd.DataFrame(x_scaled, columns=df.columns)

# Initialize k-means clustering algorithm
kmeans = KMeans(n_clusters=5, random_state=1)
# Fit data points to clusters
clusters = kmeans.fit_predict(df_scaled)

stats['new_conf'] = clusters  # Add cluster numbers to original dataframe

stats.to_csv('./data/football_part_2.csv')  # Save updated df

# Separate schools by conference for plotting
plt_0 = stats[stats["new_conf"] == 0]
plt_1 = stats[stats["new_conf"] == 1]
plt_2 = stats[stats["new_conf"] == 2]
plt_3 = stats[stats["new_conf"] == 3]
plt_4 = stats[stats["new_conf"] == 4]

# Plot details
plt.title('Redistributed Power 5 Conference Schools')
plt.xlabel('Longitude')
plt.ylabel('Latidude')

# Conference 0
plt.scatter(
    plt_0["longitude"].values.tolist(),
    plt_0["latitude"].values.tolist(),
    c='y'
    )

# Conference 1
plt.scatter(
    plt_1["longitude"].values.tolist(),
    plt_1["latitude"].values.tolist(),
    c='r'
    )

# Conference 2
plt.scatter(
    plt_2["longitude"].values.tolist(),
    plt_2["latitude"].values.tolist(),
    c='g'
    )

# Conference 3
plt.scatter(
    plt_3["longitude"].values.tolist(),
    plt_3["latitude"].values.tolist(),
    c='b'
    )

# Conference 4
plt.scatter(
    plt_4["longitude"].values.tolist(),
    plt_4["latitude"].values.tolist(),
    c='purple'
    )

# List schools in each conference
conf_0 = plt_0["team"].values
conf_1 = plt_1["team"].values
conf_2 = plt_2["team"].values
conf_3 = plt_3["team"].values
conf_4 = plt_4["team"].values
