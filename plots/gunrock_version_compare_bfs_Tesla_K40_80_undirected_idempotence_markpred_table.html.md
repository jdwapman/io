---
title: Source data for gunrock_version_compare_bfs_Tesla_K40_80_undirected_idempotence_markpred
full_length: true
---

# Source data for gunrock_version_compare_bfs_Tesla_K40_80_undirected_idempotence_markpred

<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>primitive</th>
      <th>dataset</th>
      <th>avg_mteps</th>
      <th>avg_process_time</th>
      <th>avg_process_time_10+</th>
      <th>speedup_vs_10+</th>
      <th>engine</th>
      <th>gunrock_version</th>
      <th>gpuinfo_name</th>
      <th>gpuinfo_name_full</th>
      <th>num_vertices</th>
      <th>num_edges</th>
      <th>nodes_visited</th>
      <th>edges_visited</th>
      <th>search_depth</th>
      <th>advance_mode</th>
      <th>idempotence</th>
      <th>undirected</th>
      <th>mark_pred</th>
      <th>undirected_idempotence_markpred</th>
      <th>undirected_markpred</th>
      <th>undirected_pull</th>
      <th>pull</th>
      <th>64bit_SizeT</th>
      <th>64bit_VertexT</th>
      <th>time</th>
      <th>details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bfs</td>
      <td>ak2010</td>
      <td>49.550802</td>
      <td>4.120660</td>
      <td>4.120660</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>45292.0</td>
      <td>2.170980e+05</td>
      <td>42381.0</td>
      <td>2.041820e+05</td>
      <td>60.0</td>
      <td>LB</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False / False / True</td>
      <td>False / True</td>
      <td>False / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Mon Mar  9 16:48:52 2020\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/launch_bounds_comparison/k40c/bfs_ak2010_Mon Mar  9 164852 136 2020.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>arabic-2005</td>
      <td>NaN</td>
      <td>183.290939</td>
      <td>141.477585</td>
      <td>0.771874</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40m</td>
      <td>22744080.0</td>
      <td>1.107806e+09</td>
      <td>22634275.0</td>
      <td>1.104464e+09</td>
      <td>28.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Fri Jan 27 05:58:42 2017\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ipdps17/eval_fig4/BFS_arabic-2005_Fri Jan 27 055842 2017.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>arabic-2005</td>
      <td>4367.442317</td>
      <td>141.477585</td>
      <td>141.477585</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>22744080.0</td>
      <td>6.311537e+08</td>
      <td>22359925.0</td>
      <td>6.178952e+08</td>
      <td>55.0</td>
      <td>LB</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False / False / False</td>
      <td>False / False</td>
      <td>False / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 05:14:44 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/arabic-2005/bfs_arabic-2005_Fri Oct  4 051444 308 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>asia_osm</td>
      <td>6.130173</td>
      <td>4147.224855</td>
      <td>4147.224855</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>11950757.0</td>
      <td>2.542321e+07</td>
      <td>11950757.0</td>
      <td>2.542321e+07</td>
      <td>40853.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 17:23:05 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/asia_osm/bfs_asia_osm_Fri Oct  4 172305 432 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>belgium_osm</td>
      <td>NaN</td>
      <td>122.067810</td>
      <td>187.375440</td>
      <td>1.535011</td>
      <td>Gunrock</td>
      <td>0.3.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1441295.0</td>
      <td>3.099940e+06</td>
      <td>1459.0</td>
      <td>-1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Tue Aug 18 21:35:16 2015\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ab/DOBFS_belgium_osm_Tue Aug 18 213516 2015.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>belgium_osm</td>
      <td>16.544004</td>
      <td>187.375440</td>
      <td>187.375440</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>1441295.0</td>
      <td>3.099940e+06</td>
      <td>1441295.0</td>
      <td>3.099940e+06</td>
      <td>1591.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True / False / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 16:08:23 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/belgium_osm/bfs_belgium_osm_Fri Oct  4 160823 262 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>caidaRouterLevel</td>
      <td>353.789229</td>
      <td>3.434870</td>
      <td>3.434870</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>192244.0</td>
      <td>1.218132e+06</td>
      <td>190914.0</td>
      <td>1.215220e+06</td>
      <td>18.0</td>
      <td>LB</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True / True / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 16:04:35 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/caidaRouterLevel/bfs_caidaRouterLevel_Fri Oct  4 160435 92 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>citationCiteseer</td>
      <td>717.599163</td>
      <td>3.223658</td>
      <td>3.223658</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>268495.0</td>
      <td>2.313294e+06</td>
      <td>268495.0</td>
      <td>2.313294e+06</td>
      <td>24.0</td>
      <td>LB</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True / True / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Mon Sep 30 21:33:53 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/citationCiteseer/bfs_citationCiteseer_Mon Sep 30 213353 406 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>coAuthorsCiteseer</td>
      <td>630.384998</td>
      <td>2.582974</td>
      <td>2.582974</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>227320.0</td>
      <td>1.628268e+06</td>
      <td>227320.0</td>
      <td>1.628268e+06</td>
      <td>24.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Mon Sep 30 21:29:03 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/coAuthorsCiteseer/bfs_coAuthorsCiteseer_Mon Sep 30 212903 954 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>coAuthorsDBLP</td>
      <td>921.039012</td>
      <td>2.122985</td>
      <td>2.122985</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>299067.0</td>
      <td>1.955352e+06</td>
      <td>299067.0</td>
      <td>1.955352e+06</td>
      <td>19.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True / True / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Mon Sep 30 21:28:37 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/coAuthorsDBLP/bfs_coAuthorsDBLP_Mon Sep 30 212837 990 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>coPapersCiteseer</td>
      <td>5076.731048</td>
      <td>6.317735</td>
      <td>6.317735</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>434102.0</td>
      <td>3.207344e+07</td>
      <td>434102.0</td>
      <td>3.207344e+07</td>
      <td>25.0</td>
      <td>LB</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Mon Sep 30 21:31:53 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/coPapersCiteseer/bfs_coPapersCiteseer_Mon Sep 30 213153 296 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>coPapersDBLP</td>
      <td>7608.852857</td>
      <td>4.007366</td>
      <td>4.007366</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>540486.0</td>
      <td>3.049146e+07</td>
      <td>540486.0</td>
      <td>3.049146e+07</td>
      <td>15.0</td>
      <td>LB</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Mon Sep 30 21:29:32 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/coPapersDBLP/bfs_coPapersDBLP_Mon Sep 30 212932 706 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n10</td>
      <td>3.164809</td>
      <td>1.931238</td>
      <td>1.931238</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>1024.0</td>
      <td>6.112000e+03</td>
      <td>1024.0</td>
      <td>6.112000e+03</td>
      <td>20.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True / False / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:04:49 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n10/bfs_delaunay_n10_Thu Sep 26 210449 529 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n11</td>
      <td>5.094411</td>
      <td>2.405381</td>
      <td>2.405381</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>2048.0</td>
      <td>1.225400e+04</td>
      <td>2048.0</td>
      <td>1.225400e+04</td>
      <td>24.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True / False / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:04:54 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n11/bfs_delaunay_n11_Thu Sep 26 210454 91 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n12</td>
      <td>8.055018</td>
      <td>3.045058</td>
      <td>3.045058</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>4096.0</td>
      <td>2.452800e+04</td>
      <td>4096.0</td>
      <td>2.452800e+04</td>
      <td>35.0</td>
      <td>LB</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True / True / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:04:59 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n12/bfs_delaunay_n12_Thu Sep 26 210459 645 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n13</td>
      <td>11.762077</td>
      <td>4.173923</td>
      <td>4.173923</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>8192.0</td>
      <td>4.909400e+04</td>
      <td>8192.0</td>
      <td>4.909400e+04</td>
      <td>43.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True / False / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:05:05 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n13/bfs_delaunay_n13_Thu Sep 26 210505 772 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n14</td>
      <td>17.192522</td>
      <td>5.714345</td>
      <td>5.714345</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>16384.0</td>
      <td>9.824400e+04</td>
      <td>16384.0</td>
      <td>9.824400e+04</td>
      <td>62.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True / True / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:05:13 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n14/bfs_delaunay_n14_Thu Sep 26 210513 708 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n15</td>
      <td>25.359750</td>
      <td>7.750392</td>
      <td>7.750392</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>32768.0</td>
      <td>1.965480e+05</td>
      <td>32768.0</td>
      <td>1.965480e+05</td>
      <td>82.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True / False / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:05:23 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n15/bfs_delaunay_n15_Thu Sep 26 210523 858 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n16</td>
      <td>34.217742</td>
      <td>11.489654</td>
      <td>11.489654</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>65536.0</td>
      <td>3.931500e+05</td>
      <td>65536.0</td>
      <td>3.931500e+05</td>
      <td>111.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:05:35 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n16/bfs_delaunay_n16_Thu Sep 26 210535 705 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n17</td>
      <td>48.895099</td>
      <td>16.082430</td>
      <td>16.082430</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>131072.0</td>
      <td>7.863520e+05</td>
      <td>131072.0</td>
      <td>7.863520e+05</td>
      <td>163.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:05:55 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n17/bfs_delaunay_n17_Thu Sep 26 210555 728 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n18</td>
      <td>64.164443</td>
      <td>24.511894</td>
      <td>24.511894</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>262144.0</td>
      <td>1.572792e+06</td>
      <td>262144.0</td>
      <td>1.572792e+06</td>
      <td>217.0</td>
      <td>LB</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:06:25 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n18/bfs_delaunay_n18_Thu Sep 26 210625 987 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n19</td>
      <td>82.489475</td>
      <td>38.133907</td>
      <td>38.133907</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>524288.0</td>
      <td>3.145646e+06</td>
      <td>524288.0</td>
      <td>3.145646e+06</td>
      <td>287.0</td>
      <td>LB</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True / False / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:07:22 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n19/bfs_delaunay_n19_Thu Sep 26 210722 249 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n20</td>
      <td>110.308914</td>
      <td>57.034122</td>
      <td>57.034122</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>1048576.0</td>
      <td>6.291372e+06</td>
      <td>1048576.0</td>
      <td>6.291372e+06</td>
      <td>417.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:08:33 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n20/bfs_delaunay_n20_Thu Sep 26 210833 63 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n21</td>
      <td>NaN</td>
      <td>59.821983</td>
      <td>82.254004</td>
      <td>1.374980</td>
      <td>Gunrock</td>
      <td>0.3.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2097152.0</td>
      <td>1.258282e+07</td>
      <td>564.0</td>
      <td>-1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Tue Aug 18 19:01:00 2015\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ab/DOBFS_delaunay_n21_Tue Aug 18 190100 2015.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n21</td>
      <td>152.975118</td>
      <td>82.254004</td>
      <td>82.254004</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>2097152.0</td>
      <td>1.258282e+07</td>
      <td>2097152.0</td>
      <td>1.258282e+07</td>
      <td>556.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True / True / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:10:59 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n21/bfs_delaunay_n21_Thu Sep 26 211059 719 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n22</td>
      <td>208.674958</td>
      <td>120.597786</td>
      <td>120.597786</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>4194304.0</td>
      <td>2.516574e+07</td>
      <td>4194304.0</td>
      <td>2.516574e+07</td>
      <td>761.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:14:25 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n22/bfs_delaunay_n22_Thu Sep 26 211425 760 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n23</td>
      <td>271.673527</td>
      <td>185.264897</td>
      <td>185.264897</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>8388608.0</td>
      <td>5.033157e+07</td>
      <td>8388608.0</td>
      <td>5.033157e+07</td>
      <td>1192.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:21:00 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n23/bfs_delaunay_n23_Thu Sep 26 212100 931 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n24</td>
      <td>NaN</td>
      <td>207.433762</td>
      <td>278.966284</td>
      <td>1.344845</td>
      <td>Gunrock</td>
      <td>0.3.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>16777216.0</td>
      <td>1.006632e+08</td>
      <td>1651.0</td>
      <td>-1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Tue Aug 18 20:01:48 2015\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ab/DOBFS_delaunay_n24_Tue Aug 18 200148 2015.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n24</td>
      <td>360.843614</td>
      <td>278.966284</td>
      <td>278.966284</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>16777216.0</td>
      <td>1.006632e+08</td>
      <td>16777216.0</td>
      <td>1.006632e+08</td>
      <td>1699.0</td>
      <td>LB</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:33:36 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/delaunay_n24/bfs_delaunay_n24_Thu Sep 26 213336 141 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>europe_osm</td>
      <td>NaN</td>
      <td>1687.560791</td>
      <td>2412.557125</td>
      <td>1.429612</td>
      <td>Gunrock</td>
      <td>0.3.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>50912018.0</td>
      <td>1.081093e+08</td>
      <td>17346.0</td>
      <td>-1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Tue Aug 18 23:22:29 2015\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ab/DOBFS_europe_osm_Tue Aug 18 232229 2015.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>europe_osm</td>
      <td>44.811092</td>
      <td>2412.557125</td>
      <td>2412.557125</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>50912018.0</td>
      <td>1.081093e+08</td>
      <td>50912018.0</td>
      <td>1.081093e+08</td>
      <td>20926.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 18:43:24 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/europe_osm/bfs_europe_osm_Fri Oct  4 184324 991 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>germany_osm</td>
      <td>38.066853</td>
      <td>649.866223</td>
      <td>649.866223</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>11548845.0</td>
      <td>2.473836e+07</td>
      <td>11548845.0</td>
      <td>2.473836e+07</td>
      <td>4426.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 17:01:24 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/germany_osm/bfs_germany_osm_Fri Oct  4 170124 923 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>great-britain_osm</td>
      <td>18.927389</td>
      <td>861.874485</td>
      <td>861.874485</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>7733822.0</td>
      <td>1.631303e+07</td>
      <td>7733822.0</td>
      <td>1.631303e+07</td>
      <td>5494.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 16:41:37 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/great-britain_osm/bfs_great-britain_osm_Fri Oct  4 164137 971 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>hollywood-2009</td>
      <td>NaN</td>
      <td>19.963360</td>
      <td>9.066558</td>
      <td>0.454160</td>
      <td>Gunrock</td>
      <td>0.3.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1069126.0</td>
      <td>1.126133e+08</td>
      <td>11.0</td>
      <td>-1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Fri Nov 11 16:08:56 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ppopp16/DOBFS_hollywood-2009_Fri Nov 11 160856 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>hollywood-2009</td>
      <td>NaN</td>
      <td>19.953056</td>
      <td>9.066558</td>
      <td>0.454394</td>
      <td>Gunrock</td>
      <td>0.3.1</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1069126.0</td>
      <td>1.126133e+08</td>
      <td>11.0</td>
      <td>-1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Nov 12 13:29:34 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ppopp16/DOBFS_hollywood-2009_Sat Nov 12 132934 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>hollywood-2009</td>
      <td>NaN</td>
      <td>4.420612</td>
      <td>9.066558</td>
      <td>2.050974</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40m</td>
      <td>1139905.0</td>
      <td>1.127514e+08</td>
      <td>1069126.0</td>
      <td>1.126133e+08</td>
      <td>9.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Wed Nov 30 02:30:05 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/topc/BFS.CentOS7.2_k40cx1_do_sweep2/BFS_hollywood-2009_Wed Nov 30 023005 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>hollywood-2009</td>
      <td>12420.734245</td>
      <td>9.066558</td>
      <td>9.066558</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>1139905.0</td>
      <td>1.127514e+08</td>
      <td>1069126.0</td>
      <td>1.126133e+08</td>
      <td>10.0</td>
      <td>LB</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Wed Oct  2 08:56:13 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/hollywood-2009/bfs_hollywood-2009_Wed Oct  2 085613 265 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>indochina-2004</td>
      <td>NaN</td>
      <td>62.822369</td>
      <td>34.898305</td>
      <td>0.555508</td>
      <td>Gunrock</td>
      <td>0.3.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7320539.0</td>
      <td>2.981097e+08</td>
      <td>26.0</td>
      <td>-1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Fri Nov 11 16:09:00 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ppopp16/DOBFS_indochina-2004_Fri Nov 11 160900 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>indochina-2004</td>
      <td>NaN</td>
      <td>63.085247</td>
      <td>34.898305</td>
      <td>0.553193</td>
      <td>Gunrock</td>
      <td>0.3.1</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7320539.0</td>
      <td>2.981097e+08</td>
      <td>26.0</td>
      <td>-1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Nov 12 13:29:38 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ppopp16/DOBFS_indochina-2004_Sat Nov 12 132938 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>indochina-2004</td>
      <td>NaN</td>
      <td>51.126980</td>
      <td>34.898305</td>
      <td>0.682581</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>7414866.0</td>
      <td>3.019696e+08</td>
      <td>7320539.0</td>
      <td>2.981097e+08</td>
      <td>26.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Mon Dec  5 12:57:57 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/topc/optimization-switch/BFS_indochina-2004_Mon Dec  5 125757 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>indochina-2004</td>
      <td>5358.964492</td>
      <td>34.898305</td>
      <td>34.898305</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>7414866.0</td>
      <td>1.916068e+08</td>
      <td>7216095.0</td>
      <td>1.870188e+08</td>
      <td>51.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False / True / False</td>
      <td>False / False</td>
      <td>False / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 15:53:06 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/indochina-2004/bfs_indochina-2004_Fri Oct  4 155306 814 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>italy_osm</td>
      <td>13.786124</td>
      <td>1017.541671</td>
      <td>1017.541671</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>6686493.0</td>
      <td>1.402796e+07</td>
      <td>6686493.0</td>
      <td>1.402796e+07</td>
      <td>8050.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 16:17:30 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/italy_osm/bfs_italy_osm_Fri Oct  4 161730 172 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn16</td>
      <td>7406.417801</td>
      <td>0.663228</td>
      <td>0.663228</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>65536.0</td>
      <td>4.912142e+06</td>
      <td>55319.0</td>
      <td>4.912140e+06</td>
      <td>5.0</td>
      <td>LB</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:54:18 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/kron_g500-logn16/bfs_kron_g500-logn16_Thu Sep 26 215418 673 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn17</td>
      <td>11111.187010</td>
      <td>0.920510</td>
      <td>0.920510</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>131072.0</td>
      <td>1.022797e+07</td>
      <td>107901.0</td>
      <td>1.022796e+07</td>
      <td>6.0</td>
      <td>LB</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 21:57:14 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/kron_g500-logn17/bfs_kron_g500-logn17_Thu Sep 26 215714 283 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn18</td>
      <td>23477.579604</td>
      <td>0.901514</td>
      <td>0.901514</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>262144.0</td>
      <td>2.116537e+07</td>
      <td>210141.0</td>
      <td>2.116536e+07</td>
      <td>5.0</td>
      <td>LB</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 22:06:09 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/kron_g500-logn18/bfs_kron_g500-logn18_Thu Sep 26 220609 909 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn19</td>
      <td>31501.226870</td>
      <td>1.382852</td>
      <td>1.382852</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>524288.0</td>
      <td>4.356157e+07</td>
      <td>409123.0</td>
      <td>4.356152e+07</td>
      <td>6.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 22:27:06 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/kron_g500-logn19/bfs_kron_g500-logn19_Thu Sep 26 222706 600 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn20</td>
      <td>44208.568764</td>
      <td>2.018584</td>
      <td>2.018584</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>1048576.0</td>
      <td>8.923880e+07</td>
      <td>795153.0</td>
      <td>8.923872e+07</td>
      <td>6.0</td>
      <td>LB</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Sep 26 23:29:09 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/kron_g500-logn20/bfs_kron_g500-logn20_Thu Sep 26 232909 620 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn21</td>
      <td>NaN</td>
      <td>3.631726</td>
      <td>3.729926</td>
      <td>1.027040</td>
      <td>Gunrock</td>
      <td>0.3.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40m</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1543901.0</td>
      <td>1.820817e+08</td>
      <td>6.0</td>
      <td>LB</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False / False / False</td>
      <td>False / False</td>
      <td>False / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Fri Mar  3 09:50:44 2017\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/20170303/dobfs_k40mx1_kron_g500-logn21.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn21</td>
      <td>NaN</td>
      <td>23.855743</td>
      <td>3.729926</td>
      <td>0.156353</td>
      <td>Gunrock</td>
      <td>0.3.1</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1543901.0</td>
      <td>1.820817e+08</td>
      <td>6.0</td>
      <td>-1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Nov 12 13:29:43 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ppopp16/DOBFS_kron_g500-logn21_Sat Nov 12 132943 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn21</td>
      <td>NaN</td>
      <td>2.839655</td>
      <td>3.729926</td>
      <td>1.313514</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>2097152.0</td>
      <td>1.820819e+08</td>
      <td>1543901.0</td>
      <td>1.820817e+08</td>
      <td>5.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Thu Jan 26 00:40:43 2017\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ipdps17/eval_fig2/BFS_kron_g500-logn21_Thu Jan 26 004043 2017.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn21</td>
      <td>48816.428929</td>
      <td>3.729926</td>
      <td>3.729926</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>2097152.0</td>
      <td>1.820819e+08</td>
      <td>1543901.0</td>
      <td>1.820817e+08</td>
      <td>6.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Sep 27 01:52:35 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/kron_g500-logn21/bfs_kron_g500-logn21_Fri Sep 27 015235 698 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>luxembourg_osm</td>
      <td>2.119194</td>
      <td>112.935400</td>
      <td>112.935400</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>114599.0</td>
      <td>2.393320e+05</td>
      <td>114599.0</td>
      <td>2.393320e+05</td>
      <td>862.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 16:39:05 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/luxembourg_osm/bfs_luxembourg_osm_Fri Oct  4 163905 750 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>netherlands_osm</td>
      <td>21.945790</td>
      <td>222.478938</td>
      <td>222.478938</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>2216688.0</td>
      <td>4.882476e+06</td>
      <td>2216688.0</td>
      <td>4.882476e+06</td>
      <td>1495.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 16:12:14 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/netherlands_osm/bfs_netherlands_osm_Fri Oct  4 161214 213 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>preferentialAttachment</td>
      <td>1270.578058</td>
      <td>0.787020</td>
      <td>0.787020</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>100000.0</td>
      <td>9.999700e+05</td>
      <td>100000.0</td>
      <td>9.999700e+05</td>
      <td>6.0</td>
      <td>LB</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True / True / True</td>
      <td>True / True</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Mon Sep 30 21:34:30 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/preferentialAttachment/bfs_preferentialAttachment_Mon Sep 30 213430 98 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>rmat_n22_e64.000000</td>
      <td>56938.755644</td>
      <td>4.379378</td>
      <td>4.379378</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>4194304.0</td>
      <td>2.498847e+08</td>
      <td>2843579.0</td>
      <td>2.493564e+08</td>
      <td>6.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Sun Sep 29 16:50:06 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/rmat_n22_e64/bfs_rmat_n22_e64.000000_Sun Sep 29 165006 387 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>rmat_n23_e32.000000</td>
      <td>26119.639869</td>
      <td>9.839694</td>
      <td>9.839694</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>8388608.0</td>
      <td>2.581364e+08</td>
      <td>4757829.0</td>
      <td>2.570093e+08</td>
      <td>8.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False / True / False</td>
      <td>False / False</td>
      <td>False / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Sun Sep 29 03:13:50 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/rmat_n23_e32/bfs_rmat_n23_e32.000000_Sun Sep 29 031350 822 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>rmat_n24_e16.000000</td>
      <td>13413.819835</td>
      <td>19.439793</td>
      <td>19.439793</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>16777216.0</td>
      <td>2.629841e+08</td>
      <td>7637215.0</td>
      <td>2.607619e+08</td>
      <td>8.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Sep 27 09:03:40 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/rmat_n24_e16/bfs_rmat_n24_e16.000000_Fri Sep 27 090340 884 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>roadNet-CA</td>
      <td>NaN</td>
      <td>33.988953</td>
      <td>106.572628</td>
      <td>3.135508</td>
      <td>Gunrock</td>
      <td>0.3.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1957027.0</td>
      <td>5.520776e+06</td>
      <td>555.0</td>
      <td>1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Fri Nov 11 16:09:17 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ppopp16/BFS_roadNet-CA_Fri Nov 11 160917 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>roadNet-CA</td>
      <td>NaN</td>
      <td>34.869911</td>
      <td>106.572628</td>
      <td>3.056292</td>
      <td>Gunrock</td>
      <td>0.3.1</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1957027.0</td>
      <td>5.520776e+06</td>
      <td>555.0</td>
      <td>1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Nov 12 13:29:47 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ppopp16/BFS_roadNet-CA_Sat Nov 12 132947 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>roadNet-CA</td>
      <td>51.802945</td>
      <td>106.572628</td>
      <td>106.572628</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>1971281.0</td>
      <td>5.533214e+06</td>
      <td>1957027.0</td>
      <td>5.520776e+06</td>
      <td>748.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 16:04:55 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/roadNet-CA/bfs_roadNet-CA_Fri Oct  4 160455 102 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>road_central</td>
      <td>57.675494</td>
      <td>587.196112</td>
      <td>587.196112</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>14081816.0</td>
      <td>3.386683e+07</td>
      <td>14081816.0</td>
      <td>3.386683e+07</td>
      <td>3482.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 20:32:21 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/road_central/bfs_road_central_Fri Oct  4 203221 919 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>road_usa</td>
      <td>NaN</td>
      <td>646.177246</td>
      <td>897.313023</td>
      <td>1.388648</td>
      <td>Gunrock</td>
      <td>0.3.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>23947347.0</td>
      <td>5.770862e+07</td>
      <td>6262.0</td>
      <td>-1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Tue Aug 18 23:59:23 2015\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ab/DOBFS_road_usa_Tue Aug 18 235923 2015.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>road_usa</td>
      <td>NaN</td>
      <td>546.733032</td>
      <td>897.313023</td>
      <td>1.641227</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>23947347.0</td>
      <td>5.770862e+07</td>
      <td>23947347.0</td>
      <td>5.770862e+07</td>
      <td>6262.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Mon Dec  5 12:58:48 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/topc/optimization-switch/BFS_road_usa_Mon Dec  5 125848 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>road_usa</td>
      <td>64.312701</td>
      <td>897.313023</td>
      <td>897.313023</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>23947347.0</td>
      <td>5.770862e+07</td>
      <td>23947347.0</td>
      <td>5.770862e+07</td>
      <td>7533.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 20:01:19 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/road_usa/bfs_road_usa_Fri Oct  4 200119 374 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-LiveJournal1</td>
      <td>NaN</td>
      <td>23.133032</td>
      <td>11.979103</td>
      <td>0.517835</td>
      <td>Gunrock</td>
      <td>0.3.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K80</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4400347.0</td>
      <td>6.768093e+07</td>
      <td>15.0</td>
      <td>LB</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False / True / False</td>
      <td>False / False</td>
      <td>False / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Fri Mar  3 09:14:22 2017\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/20170303/dobfs-idem_k80x1_soc-LiveJournal1.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-LiveJournal1</td>
      <td>NaN</td>
      <td>10.802359</td>
      <td>11.979103</td>
      <td>1.108934</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40m</td>
      <td>4847571.0</td>
      <td>8.570247e+07</td>
      <td>4843953.0</td>
      <td>8.569137e+07</td>
      <td>14.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Wed Nov 30 02:42:32 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/topc/BFS.CentOS7.2_k40cx1_do_sweep2/BFS_soc-LiveJournal1_Wed Nov 30 024232 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-LiveJournal1</td>
      <td>7153.404338</td>
      <td>11.979103</td>
      <td>11.979103</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>4847571.0</td>
      <td>8.570247e+07</td>
      <td>4843953.0</td>
      <td>8.569137e+07</td>
      <td>14.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Mon Sep 30 21:35:27 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/soc-LiveJournal1/bfs_soc-LiveJournal1_Mon Sep 30 213527 370 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-orkut</td>
      <td>NaN</td>
      <td>48.240032</td>
      <td>27.566142</td>
      <td>0.571437</td>
      <td>Gunrock</td>
      <td>0.3.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2997166.0</td>
      <td>2.126984e+08</td>
      <td>8.0</td>
      <td>-1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Fri Nov 11 16:08:51 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ppopp16/DOBFS_soc-orkut_Fri Nov 11 160851 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-orkut</td>
      <td>NaN</td>
      <td>55.364193</td>
      <td>27.566142</td>
      <td>0.497906</td>
      <td>Gunrock</td>
      <td>0.3.1</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2997166.0</td>
      <td>2.126984e+08</td>
      <td>8.0</td>
      <td>-1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Nov 12 13:29:29 2016\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ppopp16/DOBFS_soc-orkut_Sat Nov 12 132929 2016.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-orkut</td>
      <td>NaN</td>
      <td>5.312634</td>
      <td>27.566142</td>
      <td>5.188790</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>2997166.0</td>
      <td>2.126984e+08</td>
      <td>2997166.0</td>
      <td>2.126984e+08</td>
      <td>8.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Sat Jun 24 13:28:53 2017\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/cuda9/BFS_soc-orkut_Sat Jun 24 132853 2017.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-orkut</td>
      <td>7715.929979</td>
      <td>27.566142</td>
      <td>27.566142</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>2997166.0</td>
      <td>2.126984e+08</td>
      <td>2997166.0</td>
      <td>2.126984e+08</td>
      <td>9.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Wed Oct  2 07:59:18 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/soc-orkut/bfs_soc-orkut_Wed Oct  2 075918 748 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-sinaweibo</td>
      <td>NaN</td>
      <td>53.633884</td>
      <td>48.132314</td>
      <td>0.897424</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40m</td>
      <td>58655849.0</td>
      <td>5.226421e+08</td>
      <td>58655820.0</td>
      <td>5.226420e+08</td>
      <td>5.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Fri Jan 27 05:51:33 2017\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ipdps17/eval_fig4/BFS_soc-sinaweibo_Fri Jan 27 055133 2017.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-sinaweibo</td>
      <td>10858.444082</td>
      <td>48.132314</td>
      <td>48.132314</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>58655849.0</td>
      <td>5.226421e+08</td>
      <td>58655820.0</td>
      <td>5.226420e+08</td>
      <td>7.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False / False / False</td>
      <td>False / False</td>
      <td>False / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Thu Oct  3 07:08:21 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/soc-sinaweibo/bfs_soc-sinaweibo_Thu Oct  3 070821 100 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-twitter-2010</td>
      <td>NaN</td>
      <td>75.237823</td>
      <td>57.970126</td>
      <td>0.770492</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40m</td>
      <td>21297772.0</td>
      <td>5.300511e+08</td>
      <td>21297772.0</td>
      <td>5.300511e+08</td>
      <td>15.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Fri Jan 27 05:02:42 2017\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ipdps17/eval_fig4/BFS_soc-twitter-2010_Fri Jan 27 050242 2017.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-twitter-2010</td>
      <td>9143.521367</td>
      <td>57.970126</td>
      <td>57.970126</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>21297772.0</td>
      <td>5.300511e+08</td>
      <td>21297772.0</td>
      <td>5.300511e+08</td>
      <td>18.0</td>
      <td>LB</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Mon Sep 30 22:32:20 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/soc-twitter-2010/bfs_soc-twitter-2010_Mon Sep 30 223220 737 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>uk-2002</td>
      <td>NaN</td>
      <td>111.568153</td>
      <td>83.500783</td>
      <td>0.748428</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40m</td>
      <td>18520486.0</td>
      <td>5.235745e+08</td>
      <td>18459128.0</td>
      <td>5.231134e+08</td>
      <td>25.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True / False / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Fri Jan 27 05:33:07 2017\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/ipdps17/eval_fig4/BFS_uk-2002_Fri Jan 27 053307 2017.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>uk-2002</td>
      <td>3403.054582</td>
      <td>83.500783</td>
      <td>83.500783</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>18520486.0</td>
      <td>2.922437e+08</td>
      <td>17994090.0</td>
      <td>2.841577e+08</td>
      <td>43.0</td>
      <td>LB</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False / True / False</td>
      <td>False / False</td>
      <td>False / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 08:27:12 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/uk-2002/bfs_uk-2002_Fri Oct  4 082712 88 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>uk-2005</td>
      <td>3820.762539</td>
      <td>239.252143</td>
      <td>239.252143</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>39459925.0</td>
      <td>9.213451e+08</td>
      <td>38839146.0</td>
      <td>9.141256e+08</td>
      <td>200.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False / False / False</td>
      <td>False / False</td>
      <td>False / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 08:56:42 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/uk-2005/bfs_uk-2005_Fri Oct  4 085642 213 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>webbase-1M</td>
      <td>0.367228</td>
      <td>2.429008</td>
      <td>2.429008</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla K40/80</td>
      <td>Tesla K40c</td>
      <td>1000005.0</td>
      <td>2.105531e+06</td>
      <td>231.0</td>
      <td>8.920000e+02</td>
      <td>3.0</td>
      <td>LB_CULL</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False / False / True</td>
      <td>False / True</td>
      <td>False / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>Fri Oct  4 05:05:57 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/TeslaK40c/webbase-1M/bfs_webbase-1M_Fri Oct  4 050557 623 2019.json">JSON output</a></td>
    </tr>
  </tbody>
</table>
