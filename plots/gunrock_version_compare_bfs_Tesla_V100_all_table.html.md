---
title: Source data for gunrock_version_compare_bfs_Tesla_V100_all
full_length: true
---

# Source data for gunrock_version_compare_bfs_Tesla_V100_all

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
      <td>61.363507</td>
      <td>3.327417</td>
      <td>3.327417</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Tesla V100-DGXS-32GB</td>
      <td>45292.0</td>
      <td>2.170980e+05</td>
      <td>42381.0</td>
      <td>2.041820e+05</td>
      <td>50.0</td>
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
      <td>Thu Feb 13 16:28:42 2020\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/launch_bounds_comparison/v100/bfs_ak2010_Thu Feb 13 162842 338 2020.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>arabic-2005</td>
      <td>23689.560350</td>
      <td>26.083016</td>
      <td>26.083016</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
      <td>22744080.0</td>
      <td>6.311537e+08</td>
      <td>22359925.0</td>
      <td>6.178952e+08</td>
      <td>58.0</td>
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
      <td>Fri Oct 25 02:14:06 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/V100/arabic-2005/bfs_arabic-2005_Fri Oct 25 021406 735 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>asia_osm</td>
      <td>9.746388</td>
      <td>2608.474758</td>
      <td>2608.474758</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>11950757.0</td>
      <td>2.542321e+07</td>
      <td>11950757.0</td>
      <td>2.542321e+07</td>
      <td>30882.0</td>
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
      <td>Fri Oct 25 19:21:15 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/asia_osm/bfs_asia_osm_Fri Oct 25 192115 167 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>belgium_osm</td>
      <td>30.796039</td>
      <td>100.660348</td>
      <td>100.660348</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>1441295.0</td>
      <td>3.099940e+06</td>
      <td>1441295.0</td>
      <td>3.099940e+06</td>
      <td>1361.0</td>
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
      <td>Fri Oct 25 18:37:19 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/belgium_osm/bfs_belgium_osm_Fri Oct 25 183719 171 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>caidaRouterLevel</td>
      <td>822.524591</td>
      <td>1.477427</td>
      <td>1.477427</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>192244.0</td>
      <td>1.218132e+06</td>
      <td>190914.0</td>
      <td>1.215220e+06</td>
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
      <td>Fri Oct 25 18:35:51 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/caidaRouterLevel/bfs_caidaRouterLevel_Fri Oct 25 183551 456 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>citationCiteseer</td>
      <td>1767.333020</td>
      <td>1.308918</td>
      <td>1.308918</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>268495.0</td>
      <td>2.313294e+06</td>
      <td>268495.0</td>
      <td>2.313294e+06</td>
      <td>23.0</td>
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
      <td>Thu Oct 24 02:46:00 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/citationCiteseer/bfs_citationCiteseer_Thu Oct 24 024600 278 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>coAuthorsCiteseer</td>
      <td>1106.342295</td>
      <td>1.471758</td>
      <td>1.471758</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>227320.0</td>
      <td>1.628268e+06</td>
      <td>227320.0</td>
      <td>1.628268e+06</td>
      <td>24.0</td>
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
      <td>Thu Oct 24 02:44:27 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/coAuthorsCiteseer/bfs_coAuthorsCiteseer_Thu Oct 24 024427 947 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>coAuthorsDBLP</td>
      <td>1932.774189</td>
      <td>1.011682</td>
      <td>1.011682</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>299067.0</td>
      <td>1.955352e+06</td>
      <td>299067.0</td>
      <td>1.955352e+06</td>
      <td>17.0</td>
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
      <td>Thu Oct 24 02:44:17 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/coAuthorsDBLP/bfs_coAuthorsDBLP_Thu Oct 24 024417 820 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>coPapersCiteseer</td>
      <td>15991.280367</td>
      <td>2.005683</td>
      <td>2.005683</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>434102.0</td>
      <td>3.207344e+07</td>
      <td>434102.0</td>
      <td>3.207344e+07</td>
      <td>27.0</td>
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
      <td>Thu Oct 24 02:45:20 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/coPapersCiteseer/bfs_coPapersCiteseer_Thu Oct 24 024520 375 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>coPapersDBLP</td>
      <td>23648.380964</td>
      <td>1.289368</td>
      <td>1.289368</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>540486.0</td>
      <td>3.049146e+07</td>
      <td>540486.0</td>
      <td>3.049146e+07</td>
      <td>16.0</td>
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
      <td>Thu Oct 24 02:44:39 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/coPapersDBLP/bfs_coPapersDBLP_Thu Oct 24 024439 332 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n10</td>
      <td>6.247334</td>
      <td>0.978337</td>
      <td>0.978337</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>1024.0</td>
      <td>6.112000e+03</td>
      <td>1024.0</td>
      <td>6.112000e+03</td>
      <td>19.0</td>
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
      <td>Wed Oct 23 11:19:28 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n10/bfs_delaunay_n10_Wed Oct 23 111928 941 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n11</td>
      <td>8.500008</td>
      <td>1.441646</td>
      <td>1.441646</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>2048.0</td>
      <td>1.225400e+04</td>
      <td>2048.0</td>
      <td>1.225400e+04</td>
      <td>25.0</td>
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
      <td>Wed Oct 23 11:19:33 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n11/bfs_delaunay_n11_Wed Oct 23 111933 136 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n12</td>
      <td>12.681404</td>
      <td>1.934171</td>
      <td>1.934171</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>4096.0</td>
      <td>2.452800e+04</td>
      <td>4096.0</td>
      <td>2.452800e+04</td>
      <td>35.0</td>
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
      <td>Wed Oct 23 11:19:37 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n12/bfs_delaunay_n12_Wed Oct 23 111937 875 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n13</td>
      <td>19.757929</td>
      <td>2.484775</td>
      <td>2.484775</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>8192.0</td>
      <td>4.909400e+04</td>
      <td>8192.0</td>
      <td>4.909400e+04</td>
      <td>47.0</td>
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
      <td>Wed Oct 23 11:19:43 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n13/bfs_delaunay_n13_Wed Oct 23 111943 321 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n14</td>
      <td>27.562705</td>
      <td>3.564382</td>
      <td>3.564382</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>16384.0</td>
      <td>9.824400e+04</td>
      <td>16384.0</td>
      <td>9.824400e+04</td>
      <td>61.0</td>
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
      <td>Wed Oct 23 11:19:51 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n14/bfs_delaunay_n14_Wed Oct 23 111951 183 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n15</td>
      <td>43.460124</td>
      <td>4.522491</td>
      <td>4.522491</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>32768.0</td>
      <td>1.965480e+05</td>
      <td>32768.0</td>
      <td>1.965480e+05</td>
      <td>80.0</td>
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
      <td>Wed Oct 23 11:19:57 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n15/bfs_delaunay_n15_Wed Oct 23 111957 887 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n16</td>
      <td>63.152617</td>
      <td>6.225395</td>
      <td>6.225395</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>65536.0</td>
      <td>3.931500e+05</td>
      <td>65536.0</td>
      <td>3.931500e+05</td>
      <td>117.0</td>
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
      <td>Wed Oct 23 11:20:08 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n16/bfs_delaunay_n16_Wed Oct 23 112008 927 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n17</td>
      <td>90.386664</td>
      <td>8.699867</td>
      <td>8.699867</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>131072.0</td>
      <td>7.863520e+05</td>
      <td>131072.0</td>
      <td>7.863520e+05</td>
      <td>145.0</td>
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
      <td>Wed Oct 23 11:20:19 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n17/bfs_delaunay_n17_Wed Oct 23 112019 128 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n18</td>
      <td>125.540092</td>
      <td>12.528205</td>
      <td>12.528205</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>262144.0</td>
      <td>1.572792e+06</td>
      <td>262144.0</td>
      <td>1.572792e+06</td>
      <td>205.0</td>
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
      <td>Wed Oct 23 11:20:33 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n18/bfs_delaunay_n18_Wed Oct 23 112033 852 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n19</td>
      <td>156.309406</td>
      <td>20.124483</td>
      <td>20.124483</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>524288.0</td>
      <td>3.145646e+06</td>
      <td>524288.0</td>
      <td>3.145646e+06</td>
      <td>293.0</td>
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
      <td>Wed Oct 23 11:20:59 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n19/bfs_delaunay_n19_Wed Oct 23 112059 673 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n20</td>
      <td>230.962493</td>
      <td>27.239799</td>
      <td>27.239799</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>1048576.0</td>
      <td>6.291372e+06</td>
      <td>1048576.0</td>
      <td>6.291372e+06</td>
      <td>438.0</td>
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
      <td>Wed Oct 23 11:21:32 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n20/bfs_delaunay_n20_Wed Oct 23 112132 824 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n21</td>
      <td>269.305946</td>
      <td>46.723127</td>
      <td>46.723127</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>2097152.0</td>
      <td>1.258282e+07</td>
      <td>2097152.0</td>
      <td>1.258282e+07</td>
      <td>607.0</td>
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
      <td>Wed Oct 23 11:22:23 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n21/bfs_delaunay_n21_Wed Oct 23 112223 381 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n22</td>
      <td>426.549715</td>
      <td>58.998370</td>
      <td>58.998370</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>4194304.0</td>
      <td>2.516574e+07</td>
      <td>4194304.0</td>
      <td>2.516574e+07</td>
      <td>779.0</td>
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
      <td>Wed Oct 23 11:23:36 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n22/bfs_delaunay_n22_Wed Oct 23 112336 716 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n23</td>
      <td>568.615502</td>
      <td>88.515997</td>
      <td>88.515997</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>8388608.0</td>
      <td>5.033157e+07</td>
      <td>8388608.0</td>
      <td>5.033157e+07</td>
      <td>1184.0</td>
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
      <td>Wed Oct 23 11:26:05 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n23/bfs_delaunay_n23_Wed Oct 23 112605 204 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>delaunay_n24</td>
      <td>777.384092</td>
      <td>129.489660</td>
      <td>129.489660</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>16777216.0</td>
      <td>1.006632e+08</td>
      <td>16777216.0</td>
      <td>1.006632e+08</td>
      <td>1623.0</td>
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
      <td>Wed Oct 23 11:29:59 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/delaunay_n24/bfs_delaunay_n24_Wed Oct 23 112959 691 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>europe_osm</td>
      <td>74.966845</td>
      <td>1442.095094</td>
      <td>1442.095094</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>50912018.0</td>
      <td>1.081093e+08</td>
      <td>50912018.0</td>
      <td>1.081093e+08</td>
      <td>17280.0</td>
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
      <td>Fri Oct 25 19:58:32 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/europe_osm/bfs_europe_osm_Fri Oct 25 195832 863 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>germany_osm</td>
      <td>71.251016</td>
      <td>347.200131</td>
      <td>347.200131</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>11548845.0</td>
      <td>2.473836e+07</td>
      <td>11548845.0</td>
      <td>2.473836e+07</td>
      <td>3745.0</td>
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
      <td>Fri Oct 25 19:04:44 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/germany_osm/bfs_germany_osm_Fri Oct 25 190444 590 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>great-britain_osm</td>
      <td>30.977808</td>
      <td>526.603889</td>
      <td>526.603889</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>7733822.0</td>
      <td>1.631303e+07</td>
      <td>7733822.0</td>
      <td>1.631303e+07</td>
      <td>7837.0</td>
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
      <td>Fri Oct 25 18:54:52 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/great-britain_osm/bfs_great-britain_osm_Fri Oct 25 185452 686 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>hollywood-2009</td>
      <td>NaN</td>
      <td>1.619768</td>
      <td>1.008248</td>
      <td>0.622465</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
      <td>1139905.0</td>
      <td>1.127514e+08</td>
      <td>1069126.0</td>
      <td>1.126133e+08</td>
      <td>11.0</td>
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
      <td>Wed Jul 11 13:32:28 2018\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/5Apps.ubuntu16.04_v100x1_dev_sha-b8949e8/BFS_hollywood-2009_Wed Jul 11 133228 2018.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>hollywood-2009</td>
      <td>111692.033344</td>
      <td>1.008248</td>
      <td>1.008248</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
      <td>1139905.0</td>
      <td>1.127514e+08</td>
      <td>1069126.0</td>
      <td>1.126133e+08</td>
      <td>9.0</td>
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
      <td>Thu Oct 24 10:02:44 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/V100/hollywood-2009/bfs_hollywood-2009_Thu Oct 24 100244 902 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>indochina-2004</td>
      <td>NaN</td>
      <td>13.088202</td>
      <td>7.455134</td>
      <td>0.569607</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla V100</td>
      <td>Tesla V100-DGXS-16GB</td>
      <td>7414866.0</td>
      <td>3.019696e+08</td>
      <td>7320539.0</td>
      <td>2.981097e+08</td>
      <td>26.0</td>
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
      <td>Fri Jul 13 14:48:05 2018\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/5Apps.ubuntu16.04_v100x4_dev_fusion/BFS_indochina-2004_Fri Jul 13 144805 2018.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>indochina-2004</td>
      <td>25085.902838</td>
      <td>7.455134</td>
      <td>7.455134</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
      <td>7414866.0</td>
      <td>1.916068e+08</td>
      <td>7216095.0</td>
      <td>1.870188e+08</td>
      <td>40.0</td>
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
      <td>Fri Oct 25 18:10:42 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/V100/indochina-2004/bfs_indochina-2004_Fri Oct 25 181042 28 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>italy_osm</td>
      <td>22.230147</td>
      <td>631.032970</td>
      <td>631.032970</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>6686493.0</td>
      <td>1.402796e+07</td>
      <td>6686493.0</td>
      <td>1.402796e+07</td>
      <td>10743.0</td>
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
      <td>Fri Oct 25 18:41:40 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/italy_osm/bfs_italy_osm_Fri Oct 25 184140 263 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn16</td>
      <td>15463.854229</td>
      <td>0.317653</td>
      <td>0.317653</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>65536.0</td>
      <td>4.912142e+06</td>
      <td>55319.0</td>
      <td>4.912140e+06</td>
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
      <td>Wed Oct 23 11:35:24 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/kron_g500-logn16/bfs_kron_g500-logn16_Wed Oct 23 113524 591 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn17</td>
      <td>23497.388360</td>
      <td>0.435281</td>
      <td>0.435281</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
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
      <td>Wed Oct 23 11:35:40 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/kron_g500-logn17/bfs_kron_g500-logn17_Wed Oct 23 113540 856 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn18</td>
      <td>47106.038057</td>
      <td>0.449313</td>
      <td>0.449313</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>262144.0</td>
      <td>2.116537e+07</td>
      <td>210141.0</td>
      <td>2.116536e+07</td>
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
      <td>False</td>
      <td>Wed Oct 23 11:36:20 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/kron_g500-logn18/bfs_kron_g500-logn18_Wed Oct 23 113620 843 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn19</td>
      <td>93050.723955</td>
      <td>0.468148</td>
      <td>0.468148</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>524288.0</td>
      <td>4.356157e+07</td>
      <td>409123.0</td>
      <td>4.356152e+07</td>
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
      <td>Wed Oct 23 11:38:18 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/kron_g500-logn19/bfs_kron_g500-logn19_Wed Oct 23 113818 619 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn20</td>
      <td>137744.931908</td>
      <td>0.647855</td>
      <td>0.647855</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>1048576.0</td>
      <td>8.923880e+07</td>
      <td>795153.0</td>
      <td>8.923872e+07</td>
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
      <td>Wed Oct 23 11:44:48 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/kron_g500-logn20/bfs_kron_g500-logn20_Wed Oct 23 114448 872 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>kron_g500-logn21</td>
      <td>175942.077337</td>
      <td>1.034896</td>
      <td>1.034896</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>2097152.0</td>
      <td>1.820819e+08</td>
      <td>1543901.0</td>
      <td>1.820817e+08</td>
      <td>7.0</td>
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
      <td>Wed Oct 23 11:57:49 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/kron_g500-logn21/bfs_kron_g500-logn21_Wed Oct 23 115749 745 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>luxembourg_osm</td>
      <td>3.834410</td>
      <td>62.416911</td>
      <td>62.416911</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>114599.0</td>
      <td>2.393320e+05</td>
      <td>114599.0</td>
      <td>2.393320e+05</td>
      <td>1019.0</td>
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
      <td>Fri Oct 25 18:53:28 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/luxembourg_osm/bfs_luxembourg_osm_Fri Oct 25 185328 751 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>netherlands_osm</td>
      <td>42.155272</td>
      <td>115.821242</td>
      <td>115.821242</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>2216688.0</td>
      <td>4.882476e+06</td>
      <td>2216688.0</td>
      <td>4.882476e+06</td>
      <td>2070.0</td>
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
      <td>Fri Oct 25 18:39:16 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/netherlands_osm/bfs_netherlands_osm_Fri Oct 25 183916 361 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>preferentialAttachment</td>
      <td>2590.598005</td>
      <td>0.386000</td>
      <td>0.386000</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>100000.0</td>
      <td>9.999700e+05</td>
      <td>100000.0</td>
      <td>9.999700e+05</td>
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
      <td>Thu Oct 24 02:46:11 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/preferentialAttachment/bfs_preferentialAttachment_Thu Oct 24 024611 38 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>rmat_n22_e64.000000</td>
      <td>184479.179607</td>
      <td>1.351674</td>
      <td>1.351674</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>4194304.0</td>
      <td>2.498844e+08</td>
      <td>2843617.0</td>
      <td>2.493558e+08</td>
      <td>6.0</td>
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
      <td>Thu Oct 24 00:57:36 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/rmat_n22_e64/bfs_rmat_n22_e64.000000_Thu Oct 24 005736 117 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>rmat_n23_e32.000000</td>
      <td>107154.652433</td>
      <td>2.398517</td>
      <td>2.398517</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
      <td>8388608.0</td>
      <td>2.581394e+08</td>
      <td>4756367.0</td>
      <td>2.570123e+08</td>
      <td>7.0</td>
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
      <td>Wed Oct 23 19:54:11 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/V100/rmat_n23_e32/bfs_rmat_n23_e32.000000_Wed Oct 23 195411 446 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>rmat_n24_e16.000000</td>
      <td>56485.660079</td>
      <td>4.616552</td>
      <td>4.616552</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>16777216.0</td>
      <td>2.629909e+08</td>
      <td>7636725.0</td>
      <td>2.607690e+08</td>
      <td>8.0</td>
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
      <td>Wed Oct 23 15:19:38 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/rmat_n24_e16/bfs_rmat_n24_e16.000000_Wed Oct 23 151938 731 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>roadNet-CA</td>
      <td>108.346089</td>
      <td>50.955009</td>
      <td>50.955009</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>1971281.0</td>
      <td>5.533214e+06</td>
      <td>1957027.0</td>
      <td>5.520776e+06</td>
      <td>787.0</td>
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
      <td>Fri Oct 25 18:36:01 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/roadNet-CA/bfs_roadNet-CA_Fri Oct 25 183601 222 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>road_central</td>
      <td>112.203115</td>
      <td>301.834989</td>
      <td>301.834989</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>14081816.0</td>
      <td>3.386683e+07</td>
      <td>14081816.0</td>
      <td>3.386683e+07</td>
      <td>3804.0</td>
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
      <td>Fri Oct 25 20:45:01 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/road_central/bfs_road_central_Fri Oct 25 204501 988 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>road_usa</td>
      <td>NaN</td>
      <td>768.462158</td>
      <td>512.649298</td>
      <td>0.667111</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
      <td>23947347.0</td>
      <td>5.770862e+07</td>
      <td>23947347.0</td>
      <td>5.770862e+07</td>
      <td>6262.0</td>
      <td>TWC</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True / True / False</td>
      <td>True / False</td>
      <td>True / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Mon Aug  6 19:19:43 2018\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/cuda10/BFS_road_usa_Mon Aug  6 191943 2018.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>road_usa</td>
      <td>NaN</td>
      <td>608.476318</td>
      <td>512.649298</td>
      <td>0.842513</td>
      <td>Gunrock</td>
      <td>0.5.0</td>
      <td>Tesla V100</td>
      <td>Tesla V100-DGXS-32GB</td>
      <td>23947347.0</td>
      <td>5.770862e+07</td>
      <td>23947347.0</td>
      <td>5.770862e+07</td>
      <td>6262.0</td>
      <td>LB_CULL</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False / True / False</td>
      <td>False / False</td>
      <td>False / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Sat Mar 14 09:17:04 2020\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/review-request-200314/bfs/BFS_road_usa_Sat Mar 14 091704 2020.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>road_usa</td>
      <td>112.569400</td>
      <td>512.649298</td>
      <td>512.649298</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>23947347.0</td>
      <td>5.770862e+07</td>
      <td>23947347.0</td>
      <td>5.770862e+07</td>
      <td>6249.0</td>
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
      <td>Fri Oct 25 20:33:29 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/road_usa/bfs_road_usa_Fri Oct 25 203329 425 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-LiveJournal1</td>
      <td>NaN</td>
      <td>3.096509</td>
      <td>3.020975</td>
      <td>0.975607</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
      <td>4847571.0</td>
      <td>8.570247e+07</td>
      <td>4843953.0</td>
      <td>8.569137e+07</td>
      <td>12.0</td>
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
      <td>Thu Jun 28 19:51:41 2018\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/5Apps.ubuntu16.04_v100x1_dev/BFS_soc-LiveJournal1_Thu Jun 28 195141 2018.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-LiveJournal1</td>
      <td>28365.464390</td>
      <td>3.020975</td>
      <td>3.020975</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>4847571.0</td>
      <td>8.570247e+07</td>
      <td>4843953.0</td>
      <td>8.569137e+07</td>
      <td>13.0</td>
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
      <td>Thu Oct 24 02:46:26 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/soc-LiveJournal1/bfs_soc-LiveJournal1_Thu Oct 24 024626 609 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-orkut</td>
      <td>NaN</td>
      <td>1.650810</td>
      <td>3.985810</td>
      <td>2.414457</td>
      <td>Gunrock</td>
      <td>0.4.0</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
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
      <td>Mon Aug  6 16:48:08 2018\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/cuda10/BFS_soc-orkut_Mon Aug  6 164808 2018.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-orkut</td>
      <td>NaN</td>
      <td>0.150442</td>
      <td>3.985810</td>
      <td>26.493978</td>
      <td>Gunrock</td>
      <td>0.5.0</td>
      <td>Tesla V100</td>
      <td>Tesla V100-DGXS-32GB</td>
      <td>2997166.0</td>
      <td>1.063492e+08</td>
      <td>1.0</td>
      <td>0.000000e+00</td>
      <td>1.0</td>
      <td>LB</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False / True / False</td>
      <td>False / False</td>
      <td>False / nan</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Sat Mar 14 13:49:13 2020\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/review-request-200314/dobfs/BFS_soc-orkut_Sat Mar 14 134913 2020.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-orkut</td>
      <td>53363.909235</td>
      <td>3.985810</td>
      <td>3.985810</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
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
      <td>False</td>
      <td>Thu Oct 24 10:15:31 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/soc-orkut/bfs_soc-orkut_Thu Oct 24 101531 114 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-sinaweibo</td>
      <td>48657.061991</td>
      <td>10.741340</td>
      <td>10.741340</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
      <td>58655849.0</td>
      <td>5.226421e+08</td>
      <td>58655820.0</td>
      <td>5.226420e+08</td>
      <td>7.0</td>
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
      <td>Thu Oct 24 10:07:38 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/V100/soc-sinaweibo/bfs_soc-sinaweibo_Thu Oct 24 100738 582 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>soc-twitter-2010</td>
      <td>34346.852052</td>
      <td>15.432305</td>
      <td>15.432305</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
      <td>21297772.0</td>
      <td>5.300511e+08</td>
      <td>21297772.0</td>
      <td>5.300511e+08</td>
      <td>16.0</td>
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
      <td>Thu Oct 24 02:08:35 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/V100/soc-twitter-2010/bfs_soc-twitter-2010_Thu Oct 24 020835 557 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>uk-2002</td>
      <td>17080.320174</td>
      <td>16.636557</td>
      <td>16.636557</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Quadro GV100</td>
      <td>18520486.0</td>
      <td>2.922437e+08</td>
      <td>17994090.0</td>
      <td>2.841577e+08</td>
      <td>48.0</td>
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
      <td>Fri Oct 25 04:02:10 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/GV100/uk-2002/bfs_uk-2002_Fri Oct 25 040210 38 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>uk-2005</td>
      <td>35124.652599</td>
      <td>44.495238</td>
      <td>44.495238</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
      <td>39459925.0</td>
      <td>1.566054e+09</td>
      <td>39252879.0</td>
      <td>1.562880e+09</td>
      <td>22.0</td>
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
      <td>Fri Oct 25 03:26:23 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/V100/uk-2005/bfs_uk-2005_Fri Oct 25 032623 591 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>webbase-1M</td>
      <td>1.142145</td>
      <td>1.466539</td>
      <td>1.466539</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
      <td>1000005.0</td>
      <td>2.105531e+06</td>
      <td>390.0</td>
      <td>1.675000e+03</td>
      <td>7.0</td>
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
      <td>Thu Oct 24 20:52:12 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/V100/webbase-1M/bfs_webbase-1M_Thu Oct 24 205212 154 2019.json">JSON output</a></td>
    </tr>
    <tr>
      <td>bfs</td>
      <td>webbase-2001</td>
      <td>0.037884</td>
      <td>61.634874</td>
      <td>61.634874</td>
      <td>1.000000</td>
      <td>Gunrock</td>
      <td>1.0+</td>
      <td>Tesla V100</td>
      <td>Tesla V100-PCIE-32GB</td>
      <td>118142155.0</td>
      <td>9.928449e+08</td>
      <td>830.0</td>
      <td>2.335000e+03</td>
      <td>16.0</td>
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
      <td>Fri Oct 25 16:42:35 2019\n</td>
      <td><a href="https://github.com/gunrock/io/tree/master/gunrock-output/v1-0-0/bfs/V100/webbase-2001/bfs_webbase-2001_Fri Oct 25 164235 763 2019.json">JSON output</a></td>
    </tr>
  </tbody>
</table>
