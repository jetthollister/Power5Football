from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# Load data
football = pd.read_csv('./data/football_college.csv', header=0)
academics = pd.read_csv('./data/college_academics.csv', header=0)

# Pull latitude/longitude data
longlat = academics[[
    'Institution Name',
    'Longitude location of institution (HD2017)',
    'Latitude location of institution (HD2017)'
    ]]

# Merge academic and athletic data
df = football.merge(longlat, on='Institution Name', how='left')

# Save new dataset
df.to_csv('./data/football_part_1.csv')

# Temporarily remove non Power-5 Schools
df = df[df['Institution Name'] != 'Brigham Young University-Provo']
df = df[df['Institution Name'] != 'University of Massachusetts-Amherst']
df = df[df['Institution Name'] != 'University of Notre Dame']

# Dataframe with desired features
df_feat = df[[
              "Longitude location of institution (HD2017)",
              "Latitude location of institution (HD2017)",
              "Revenues Men's Team",
              "Total Undergraduates",
              "# Participants Men's Team",
              "Operating Expenses per Participant/Men's Team"
              ]]


def test(df):
    '''

    Determines how accurately schools are grouped into their current
    conference by finding the total percentage of schools that were assigned
    correctly.

    Parameters
    ----------
    df : DataFrame
        Original DataFrame

    Returns
    -------
    accuracy : float
        Ratio of correctly-assigned schools to total number of schools

    '''

    # List of current Power 5 conferences
    conferences = ['acc', 'big10', 'big12', 'pac12', 'sec']

    # Newly-generated conferences
    gen = {f'conf_{i}': df[df["new_conf"] == i]["Institution Name"].values
           for i in range(5)}
    # Current conferences
    confs = {j: df[df["curr_conf"] == i]["Institution Name"].values
             for i, j in zip(range(1, 6), conferences)}

    # Find number of schools that are similar between new/current conferences
    def check_conf(confs, gen, new, group):
        count = 0

        if len(gen[new]) == 0:
            return 0

        for school in confs[group]:
            if school in gen[new]:
                count += 1

        return count

    # Find most accurate assignments of new and current conferences
    def get_accuracy(scores):
        seen = [-1]*5
        counts = [0]*5

        for i in range(0, len(scores), 5):
            high = max(scores[i:i+5])

            if scores[i:i+5].index(high) not in seen:
                counts[i//5] = high
                seen[i//5] = scores[i:i+5].index(high)
            else:
                continue

        return sum(counts)/64

    scores = [check_conf(confs, gen, new, group) for group in confs
              for new in gen]

    accuracy = get_accuracy(scores)

    return accuracy


def cluster(df_feat, w1, w2, w3, w4, w5, w6):
    '''

    Peforms the entire k-means clustering pipeline, from data extraction to
    testing.

    Parameters
    ----------
    df_feat : DataFrame
        DataFrame containing only desired features

    w1 : float
        Longitude feature weight.

    w2 : float
        Latitude feature weight.

    w3 : float
        Men's revenue feature weight

    w4 : float
        Total undergraduates feature weight.

    w5 : float
        Operating expenses feature weight.

    w6 : float
        # Participants feature weight.


    Returns
    -------
    score : float
        Accuracy of clusters, as defined in test() function.

    '''

    global df

    vals = df_feat.values
    scaler = preprocessing.MinMaxScaler()  # Initialize min-max scaler
    x_scaled = scaler.fit_transform(vals)  # Scale features
    df_scaled = pd.DataFrame(x_scaled, columns=df_feat.columns)

    # Add feature weights
    df_scaled.loc[:, "Longitude location of institution (HD2017)"] *= w1
    df_scaled.loc[:, "Latitude location of institution (HD2017)"] *= w2
    df_scaled.loc[:, "Revenues Men's Team"] *= w3
    df_scaled.loc[:, "Total Undergraduates"] *= w4
    df_scaled.loc[:, "Operating Expenses per Participant/Men's Team"] *= w5
    df_scaled.loc[:, "# Participants Men's Team"] *= w6

    # Initialize k-means clustering algorithm
    kmeans = KMeans(n_clusters=5, random_state=1)
    # Fit data points to clusters
    clusters = kmeans.fit_predict(df_scaled)

    df['new_conf'] = clusters  # Add cluster numbers to original dataframe
    score = test(df)  # Scores clusters based on current conferences

    return score


best_acc = 0  # Stores highest-recorded accuracy

# Exhaustive grid search of all weight combinations
for w1 in np.arange(0, 3, 0.5):
    for w2 in np.arange(0, 3, 0.5):
        for w3 in np.arange(0, 3, 0.5):
            for w4 in np.arange(0, 3, 0.5):
                for w5 in np.arange(0, 3, 0.5):
                    for w6 in np.arange(0, 3, 0.5):
                        print(w1, w2, w3, w4)
                        temp_acc = cluster(df_feat, w1, w2, w3, w4, w5, w6)
                        if temp_acc > best_acc:
                            best_acc = temp_acc
                            weights = [w1, w2, w3, w4, w5, w6]

print(f'Total Accuracy: {best_acc}')
