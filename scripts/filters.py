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


def equateRGG(df):
    df.loc[df.dataset == 'rgg_n_2_24_s0', 'dataset'] = 'rgg_n24_0.000548'
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
        r'.*gunrock-output',
        '<a href="https://github.com/gunrock/io/tree/master/gunrock-output',
        s) + '">JSON output</a>')
    return df


def selectAnyOfTheseDates(dates):
    return lambda df: df[df['time'].isin(dates)]


def deleteZeroMTEPS(df):
    return df[df['m_teps'] != 0]
