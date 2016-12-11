import pandas  # http://pandas.pydata.org
import os      # built-in
import re      # built-in
import math    # built-in

# possible filtering functions


def fileEndsWithJSON(f):
    return (os.path.isfile(f) and
            (os.path.splitext(f)[1] == ".json") and
            not os.path.basename(f).startswith("_"))


def convertCtimeStringToDate(df):
    # 'time' column is in (text) ctime format
    # datetime.strptime(jsonobj['time'], "%a %b %d %H:%M:%S %Y\n")
    # or
    # http://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime
    # normalize() resets the time to midnight (so it can be == vs. dates)
    df['time'] = df['time'].apply(
        lambda x: pandas.to_datetime(x,
                                     infer_datetime_format=True).normalize())
    return df


def convertCtimeStringToDatetime(df):
    df['time'] = df['time'].apply(
        lambda x: pandas.to_datetime(x,
                                     infer_datetime_format=True))
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


def replaceFromDict(d, out_column, in_column):
    def fn(df):
        for key, value in d.iteritems():
            df.loc[df[in_column] == key, out_column] = value
        return df
    return fn


def normalizePRMTEPS(df):
    if 'search_depth' in df.columns:
        df.loc[df.algorithm == 'PageRank', 'm_teps'] = df[
            'm_teps'] * df['search_depth']
    return df


def gunrockVersionGPU(df):
    if {'gunrock_version', 'gpuinfo.name'}.issubset(df.columns):
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


def selectAnyOfThese(column, these):
    return lambda df: df[df[column].isin(these)]


def selectTag(tag):
    def fn(df):
        if 'tag' in df.columns:
            return df[df['tag'] == tag]
        else:
            return df
    return fn


def deselectTag(tag):
    def fn(df):
        if 'tag' in df.columns:
            return df[df['tag'] != tag]
        else:
            return df
    return fn


def selectOneDataset(dataset):
    return lambda df: df[df['dataset'] == dataset]


def undirectedOnly(df):
    return df[df['undirected'] == True]


def idempotentOnly(df):
    return df[df['idempotent'] == True]


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


def keepLatest(columns, sortBy='time'):
    def fn(df):
        newest = df.groupby(columns)[sortBy].transform(max)
        df = df[df[sortBy] == newest]
        return df
    return fn


def formatColumn(out_column, in_column, string_format):
    # oddly, I was not able to figure out how to do this with a lambda
    def fn(df):
        # df['var3'] = pd.Series(["{0:.2f}%".format(val * 100) for val in
        # df['var3']], index = df.index)
        df[out_column] = df[in_column].map(string_format.format)
        # df[out_column] = pandas.Series(
        #     [string_format.format(f) for f in df[in_column]])
        return df
    return fn


def loclist_expand(df, loclist, sample, sampleMinimum):
    # http://stackoverflow.com/questions/38577737/pandas-unflatten-data-frame-with-columns-containing-array
    rows = []
    for idx, row in df.iterrows():
        sampleRow = sample
        vss = []
        for loc in loclist:
            vss.append(row.at[loc])    # pick out the array, put into vss
        # print "At index ", idx, " I see ", len(vss[0]), " elements in the
        # array"
        n = len(vss[0])
        if n < sampleMinimum:
            sampleRow = False
        nsqrt = math.floor(math.sqrt(n))
        for i, v in enumerate(vss[0]):  # how many elements in the list?
            if sampleRow and (i % nsqrt != 0):  # we're sampling
                continue
            new = row.copy()
            newIsValid = True
            for j, loc in enumerate(loclist):
                if (vss[j][i] == -1):
                    newIsValid = False
                else:
                    new.at[loc] = vss[j][i]
            if newIsValid:
                rows.append(new)

    return pandas.DataFrame(rows)


def flattenArrays(loclist, sample=False, sampleMinimum=100):
    return lambda df: loclist_expand(df,
                                     loclist=loclist,
                                     sample=sample,
                                     sampleMinimum=sampleMinimum
                                     )


def recomputeMTEPSFromMax(df):
    # bet there's a cleaner way to do this
    m = max(df['edges_visited'])
    df['edges_visited'] = df['edges_visited'].apply(lambda x: m)
    df['m_teps'] = df['edges_visited'] / (df['elapsed'] * 1000.0)
    return df


def roundSig(column, significant_figures=1):
    # http://stackoverflow.com/questions/3410976/how-to-round-a-number-to-significant-figures-in-python
    def roundSigFn(x, sig):
        return round(x, sig - int(math.floor(math.log10(x))) - 1)

    def fn(df):
        df[column] = df[column].apply(
            lambda x: roundSigFn(x, significant_figures))
        return df
    return fn
