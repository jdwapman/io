.PHONY: 	install clean all

ENGINES_OUTPUTS = output/engines_topc.md \
	output/engines_topc_table_html.md

AB_RANDOM_OUTPUTS = output/do_ab_random.md \
	output/do_ab_random_hollywood-2009_table_html.md \
	output/do_ab_random_indochina-2004_table_html.md \
	output/do_ab_random_rmat_n22_e64_table_html.md \
	output/do_ab_random_rmat_n23_e32_table_html.md \
	output/do_ab_random_rmat_n24_e16_table_html.md \
	output/do_ab_random_road_usa_table_html.md \
	output/do_ab_random_soc-LiveJournal1_table_html.md \
	output/do_ab_random_soc-orkut_table_html.md

GUNROCK_GPUS_OUTPUTS = output/gunrock_gpus.md \
	output/gunrock_gpus_table_html.md

FRONTIER_SIZE_OUTPUTS = output/frontier.md \
	output/frontier_table_html.md

MGPU_SPEEDUP_OUTPUTS = output/mgpu_speedup.md \
	output/mgpu_speedup_geomean_table_html.md \
	output/mgpu_speedup_all_table_html.md

MGPU_PARTITION_OUTPUTS = output/mgpu_partition.md \
	output/mgpu_partition_table_html.md

MGPU_SCALABILITY_OUTPUTS = output/mgpu_scalability.md \
	output/mgpu_scalability_BFS_table_html.md \
	output/mgpu_scalability_DOBFS_table_html.md \
	output/mgpu_scalability_PageRank_table_html.md

GROUTE_OUTPUTS = output/groute.md \
	output/groute_table_html.md \
	output/groute_Tesla\ P100-PCIE-16GB.md \
	output/groute_Tesla\ K40c.md \
	output/groute_Tesla\ K40m.md \
	output/groute_Tesla\ K80.md \
	output/groute_Tesla\ M60.md

ALL = $(ENGINES_OUTPUTS) \
	$(AB_RANDOM_OUTPUTS) \
	$(GUNROCK_GPUS_OUTPUTS) \
	$(FRONTIER_SIZE_OUTPUTS) \
	$(MGPU_SPEEDUP_OUTPUTS) \
	$(MGPU_PARTITION_OUTPUTS) \
	$(MGPU_SCALABILITY_OUTPUTS) \
	$(GROUTE_OUTPUTS)

PLOTTING_FILES = fileops.py filters.py logic.py

DEST = "../../gunrock/doc/stats"

all: $(ALL)

$(ENGINES_OUTPUTS): altair_engines.py $(PLOTTING_FILES)
		./altair_engines.py

$(AB_RANDOM_OUTPUTS): altair_do_ab_random.py $(PLOTTING_FILES)
		./altair_do_ab_random.py

$(GUNROCK_GPUS_OUTPUTS): altair_gunrock_gpus.py $(PLOTTING_FILES)
		./altair_gunrock_gpus.py

$(FRONTIER_SIZE_OUTPUTS): altair_frontier_size.py $(PLOTTING_FILES)
		./altair_frontier_size.py

$(MGPU_SPEEDUP_OUTPUTS): altair_mgpu_speedup.py $(PLOTTING_FILES)
		./altair_mgpu_speedup.py

$(MGPU_PARTITION_OUTPUTS): altair_mgpu_partition.py $(PLOTTING_FILES)
		./altair_mgpu_partition.py

$(MGPU_SCALABILITY_OUTPUTS): altair_mgpu_scalability.py $(PLOTTING_FILES)
		./altair_mgpu_scalability.py

$(GROUTE_OUTPUTS): altair_groute.py $(PLOTTING_FILES)
		./altair_groute.py

install: $(ALL)
		cp $(ALL) $(DEST)

clean:
		rm $(ALL)
