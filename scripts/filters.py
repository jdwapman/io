import pandas  # http://pandas.pydata.org
import os      # built-in
import re      # built-in

# possible filtering functions


def fileEndsWithJSON(f):
    return (os.path.isfile(f) and
            (os.path.splitext(f)[1] == ".json") and
            not os.path.basename(f).startswith("_"))


def convertCtimeStringToDatetime(df):
    # 'time' column is in (text) ctime format
    # datetime.strptime(jsonobj['time'], "%a %b %d %H:%M:%S %Y\n")
    # or
    # http://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime
    # normalize() resets the time to midnight (so it can be == vs. dates)
    df['time'] = df['time'].apply(
        lambda x: pandas.to_datetime(x,
                                     infer_datetime_format=True).normalize())
    return df


def DOBFStoBFS(df):
    df.loc[df.algorithm == 'DOBFS', 'algorithm'] = 'BFS'
    return df


def BFSCCtoCC(df):
    df.loc[df.algorithm == 'BFSCC', 'algorithm'] = 'CC'
    return df


def equateRGG(df):
    df.loc[df.dataset == 'rgg_n_2_24_s0', 'dataset'] = 'rgg_n24_0.000548'
    return df


def equateM40(df):
    df.loc[df['gpuinfo.name'] == 'Tesla M40 24GB', 'gpuinfo.name'] = 'Tesla M40'
    return df


def normalizePRMTEPS(df):
    df.loc[df.algorithm == 'PageRank', 'm_teps'] = df[
        'm_teps'] * df['search_depth']
    return df


def gunrockVersionGPU(df):
    df['gunrock_version_gpu'] = df[
        'gunrock_version'] + " / " + df['gpuinfo.name']
    return df


def addJSONDetailsLink(df):
    df['details'] = df['details'].apply(lambda s: re.sub(
        r'.*/(\w*)-output',
        r'<a href="https://github.com/gunrock/io/tree/master/\1-output',
        s) + '">JSON output</a>')
    return df


def selectAnyOfTheseDates(dates):
    return lambda df: df[df['time'].isin(dates)]


def selectTag(tag):
    return lambda df: df[df['tag'] == tag]


def computeOtherMTEPSFromGunrock(df):
    # if df['m_teps'] is NaN, but df['elapsed'] is there, use
    # Gunrock's edges_visited to compute m_teps
    #
    # formula: edges_visited / (elapsed * 1000.0f)
    df['algorithm_dataset'] = df['algorithm'] + "_" + df['dataset']

    # series mapping {algorithm+dataset} to edges_visited
    # not quite clear why there's duplicates, so average edges_visited
    dfg = df.loc[df['engine'] ==
                 'Gunrock'].groupby(['algorithm_dataset']).mean()['edges_visited']

    # fill in missing values for edges_visited, per algorithm_dataset
    df = df.set_index('algorithm_dataset')
    df['edges_visited'] = df['edges_visited'].fillna(value=dfg)
    df = df.reset_index()

    # now calculate m_teps if it's empty but edges_visited and elapsed are
    # valid
    m = df.edges_visited.notnull() & df.elapsed.notnull() & df.m_teps.isnull()
    df.loc[m, 'm_teps'] = df['edges_visited'] / (df['elapsed'] * 1000.0)
    return df


def computeNewMTEPSFromProcessTimes(df):
    def averagePT(row):
        pt = row['process_times']
        avg = sum(pt) / len(pt)
        pt0 = filter(lambda f: f > (0.2 * avg), pt)
        return sum(pt0) / len(pt0)
    df['process_times_avg'] = df.apply(averagePT, axis=1)
    # now recompute m_teps
    df['m_teps'] = df['edges_visited'] / (df['process_times_avg'] * 1000.0)
    return df


def deleteZeroMTEPS(df):
    return df[df['m_teps'] != 0]


def setLigraAlgorithmFromSubalgorithm(df):
    ligranoalg = df['engine'] == 'Ligra' & df.algorithm.isnull()

    m = ligranoalg & df['subalgorithm'] == "bfs-bitvector"
    df.loc[m, 'algorithm'] = 'BFS'

    return df
