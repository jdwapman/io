#!/bin/bash

INDIR=${2:-"/nfs/mario-2TB/gunrock_dataset/large"}
OUTDIR=${2:-"/nfs/mario-2TB/gunrock_dataset/large-rcm"}
VISDIR=${2:-"/home/jowens/working/gunrock-io/visualizations/graphs"}

RCM=${2:-"/home/jowens/working/gunrock-io/scripts/reversecuthillmckee.py"}


NAME[0]="ak2010"

NAME[ 1]="delaunay_n10"
NAME[ 2]="delaunay_n11"
NAME[ 3]="delaunay_n12"
NAME[ 4]="delaunay_n13"
NAME[ 5]="delaunay_n14"
NAME[ 6]="delaunay_n15"
NAME[ 7]="delaunay_n16"
NAME[ 8]="delaunay_n17"
NAME[ 9]="delaunay_n18"
NAME[10]="delaunay_n19"
NAME[11]="delaunay_n20"
NAME[12]="delaunay_n21"
NAME[13]="delaunay_n22"
NAME[14]="delaunay_n23"
NAME[15]="delaunay_n24"

NAME[21]="kron_g500-logn16"
NAME[22]="kron_g500-logn17"
NAME[23]="kron_g500-logn18"
NAME[24]="kron_g500-logn19"
NAME[25]="kron_g500-logn20"
NAME[26]="kron_g500-logn21"

NAME[27]="rmat_n24_e16"      &&    GRAPH[27]="rmat --graph-scale=24 --graph-edgefactor=16"
NAME[28]="rmat_n23_e32"      &&    GRAPH[28]="rmat --graph-scale=23 --graph-edgefactor=32"
NAME[29]="rmat_n22_e64"      &&    GRAPH[29]="rmat --graph-scale=22 --graph-edgefactor=64"

NAME[31]="coAuthorsDBLP"
NAME[32]="coAuthorsCiteseer"
NAME[33]="coPapersDBLP"
NAME[34]="coPapersCiteseer"
NAME[35]="citationCiteseer"
NAME[36]="preferentialAttachment"

NAME[41]="soc-LiveJournal1"
NAME[42]="soc-twitter-2010"
NAME[43]="soc-orkut"
NAME[44]="hollywood-2009"
NAME[45]="soc-sinaweibo"

NAME[51]="webbase-1M"
NAME[52]="arabic-2005"
NAME[53]="uk-2002"
NAME[54]="uk-2005"
NAME[55]="webbase-2001"
NAME[56]="indochina-2004"
NAME[57]="caidaRouterLevel"

NAME[61]="roadNet-CA"
NAME[62]="belgium_osm"
NAME[63]="netherlands_osm"
NAME[64]="italy_osm"
NAME[65]="luxembourg_osm"
NAME[66]="great-britain_osm"
NAME[67]="germany_osm"
NAME[68]="asia_osm"
NAME[69]="europe_osm"
NAME[70]="road_usa"
NAME[71]="road_central"

mkdir -p $OUTDIR

for i in {0..71}; do
    if [ "${NAME[$i]}" = "" ]; then
        continue
    fi
    if [[ "${NAME[$i]}" = rmat* ]]; then
        echo "${NAME[$i]}" skipped, ignoring rmat
        continue
    fi

    GRAPH=${NAME[$i]}
    echo $RCM -i $INDIR/$GRAPH/$GRAPH.mtx -v $VISDIR/$GRAPH.png
    echo $RCM -i $OUTDIR/$GRAPH/$GRAPH.mtx -v $VISDIR/${GRAPH}-rcm.png
    $RCM -i $INDIR/$GRAPH/$GRAPH.mtx -v $VISDIR/$GRAPH.png
    $RCM -i $OUTDIR/$GRAPH/$GRAPH.mtx -v $VISDIR/${GRAPH}-rcm.png
done
