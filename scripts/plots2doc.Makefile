.PHONY: 	install clean all

ENGINES_OUTPUTS = output/engines_topc.md
ENGINES_TABLES = output/engines_topc_table.html.md

AB_RANDOM_OUTPUTS = output/do_ab_random.md
AB_RANDOM_TABLES = output/do_ab_random_hollywood-2009_table.html.md \
	output/do_ab_random_indochina-2004_table.html.md \
	output/do_ab_random_rmat_n22_e64_table.html.md \
	output/do_ab_random_rmat_n23_e32_table.html.md \
	output/do_ab_random_rmat_n24_e16_table.html.md \
	output/do_ab_random_road_usa_table.html.md \
	output/do_ab_random_soc-LiveJournal1_table.html.md \
	output/do_ab_random_soc-orkut_table.html.md

GUNROCK_GPUS_OUTPUTS = output/gunrock_gpus.md
GUNROCK_GPUS_TABLES = output/gunrock_gpus_table.html.md

FRONTIER_SIZE_OUTPUTS = output/frontier.md
FRONTIER_SIZE_TABLES = output/frontier_table.html.md

MGPU_SPEEDUP_OUTPUTS = output/mgpu_speedup.md
MGPU_SPEEDUP_TABLES = output/mgpu_speedup_geomean_table.html.md \
	output/mgpu_speedup_all_table.html.md

MGPU_PARTITION_OUTPUTS = output/mgpu_partition.md
MGPU_PARTITION_TABLES = output/mgpu_partition_table.html.md

MGPU_SCALABILITY_OUTPUTS = output/mgpu_scalability.md
MGPU_PARTITION_TABLES = output/mgpu_scalability_BFS_table.html.md \
	output/mgpu_scalability_DOBFS_table.html.md \
	output/mgpu_scalability_PageRank_table.html.md

GROUTE_OUTPUTS = output/groute.md
GROUTE_TABLES = output/groute_table.html.md \
	output/groute_Tesla\ P100-PCIE-16GB.md \
	output/groute_Tesla\ K40c.md \
	output/groute_Tesla\ K40m.md \
	output/groute_Tesla\ K80.md \
	output/groute_Tesla\ M60.md

ALLX = $(ENGINES_OUTPUTS) \
	$(AB_RANDOM_OUTPUTS) \
	$(GUNROCK_GPUS_OUTPUTS) \
	$(FRONTIER_SIZE_OUTPUTS) \
	$(MGPU_SPEEDUP_OUTPUTS) \
	$(MGPU_PARTITION_OUTPUTS) \
	$(MGPU_SCALABILITY_OUTPUTS) \
	$(GROUTE_OUTPUTS)

ALL_OUTPUTS = $(GUNROCK_GPUS_OUTPUTS) \
	$(ENGINES_OUTPUTS)
ALL_TABLES = $(GUNROCK_GPUS_TABLES) \
	$(ENGINES_TABLES)

PLOTTING_FILES = fileops.py filters.py logic.py

DEST_OUTPUTS = "../../gunrock-docs/source/includes"
DEST_TABLES = "../../gunrock-docs/source/tables"

all: $(ALL_OUTPUTS) $(ALL_TABLES)

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
		cp $(ALL_OUTPUTS) $(DEST_OUTPUTS)
		cp $(ALL_TABLES) $(DEST_TABLES)

clean:
		rm $(ALL)
