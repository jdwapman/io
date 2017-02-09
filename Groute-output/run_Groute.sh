#!/bin/bash

DATADIR="/home/sgpyc/Projects/Groute/ppopp17-artifact/dataset"
EXECDIR="/home/sgpyc/Projects/Groute/ppopp17-artifact/code/groute/build"
LOGDIR="/home/sgpyc/Projects/Groute/ppopp17-artifact/output"
OUTPUTDIR=""
GPU="k40"

GRAPH[0]="kron21.sym"       && METIS_OPT[0]="-nopn" && BFS_PRIO_DELTA[0]="1"    && SSSP_PRIO_DELTA[0]="30"
GRAPH[1]="OSM-eur-k"        && METIS_OPT[1]=""      && BFS_PRIO_DELTA[1]="100"  && SSSP_PRIO_DELTA[1]="10000" 
GRAPH[2]="soc-LiveJournal1" && METIS_OPT[2]=""      && BFS_PRIO_DELTA[2]="5000" && SSSP_PRIO_DELTA[2]="1000"
GRAPH[3]="twitter"          && METIS_OPT[3]="-nopn" && BFS_PRIO_DELTA[3]="10"   && SSSP_PRIO_DELTA[3]="2"
GRAPH[4]="USA"              && METIS_OPT[4]=""      && BFS_PRIO_DELTA[4]="100"  && SSSP_PRIO_DELTA[4]="100000"

FILE[0]="kron_g500-simple-logn21-weighted-random.sym.gr"
FILE[1]="osm-eur-karlsruhe.gr"
FILE[2]="soc-LiveJournal1-weighted-1.gr"
FILE[3]="twitter-ICWSM10-component.gr"
FILE[4]="USA-road-d.USA.gr"

APP[0]="bfs"
APP[1]="sssp"
APP[2]="pr"
APP[3]="cc"

for i in {0..3}
do for d in {1..4}
do
    for g in {0..4}
    do
        EXEC="${EXECDIR}/${APP[$i]}"
        OPTION="-num_gpus $d -startwith $d"
        if [ "$i" -ne "3" ]; then
            OPTION="$OPTION ${METIS_OPT[$g]}"
        fi
        if [ "$i" -eq "0" ]; then
            OPTION="$OPTION --prio_delta=${BFS_PRIO_DELTA[$g]}"
        fi
        if [ "$i" -eq "1" ]; then
            OPTION="$OPTION --prio_delta=${SSSP_PRIO_DELTA[$g]}"
        fi

        GRAPH_INPUT="-graphfile ${DATADIR}/${GRAPH[$g]}/${FILE[$g]}"
        echo $EXEC $OPTION $GRAPH_INPUT "> ${LOGDIR}/Groute.${APP[$i]}.${GPU}x${d}.${GRAPH[$g]}.txt 2>&1"
             $EXEC $OPTION $GRAPH_INPUT  > ${LOGDIR}/Groute.${APP[$i]}.${GPU}x${d}.${GRAPH[$g]}.txt 2>&1
    done
done;done

