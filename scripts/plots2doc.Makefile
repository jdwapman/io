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

ALL = $(ENGINES_OUTPUTS) $(AB_RANDOM_OUTPUTS) $(GUNROCK_GPUS_OUTPUTS)

PLOTTING_FILES = fileops.py filters.py logic.py

DEST = "../../gunrock/doc/stats"

all: $(ALL)

$(ENGINES_OUTPUTS): altair_engines.py $(PLOTTING_FILES)
		./altair_engines.py

$(AB_RANDOM_OUTPUTS): altair_do_ab_random.py $(PLOTTING_FILES)
		./altair_do_ab_random.py

$(GUNROCK_GPUS_OUTPUTS): altair_gunrock_gpus.py $(PLOTTING_FILES)
		./altair_gunrock_gpus.py

install: $(ALL)
		cp $(ALL) $(DEST)

clean:
		rm $(ALL)
