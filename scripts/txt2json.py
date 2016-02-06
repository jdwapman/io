#!/usr/bin/env python2

import os, re, math, time, json, glob, distutils.dir_util

# This is the base class that implements necessary features for parsing engine outputs.
# For each GPU Engine, we will inherit this class and make a customized parser.
# To create a customized parser, regex_array needs to be specified according
# to the format of that engine's outputs. Also, other methods may be overridden.
# (See class GPUEngineOutputParserCuSha as an example)
class GPUEngineOutputParserBase(object):	

	# Constructor
	def __init__(self, input_path = "", regex_array = [], \
			   dataset_names = ["roadNet-CA", "europe_osm", "rgg", "indochina-2004", \
					    "roadnet", "kron", "soc-orkut", "soc", "hollywood-2009", \
					    "osm", "bitcoin", "delaunay_n24", "ljournal-2008"]):
		self.input_path = input_path
                self.regex_array = regex_array
		self.dataset_names = dataset_names
		self.parsed_data = {}
		self.possible_algs = ["BFS", "CC", "BC", "SSSP", "PR"]
		self.algname_translator = {"PR" : "PageRank"}
		# translate to "standard" names
		self.datasetname_translator = {"kron" : "kron_g500-logn21", "rgg" : "rgg_n_2_24_s0", \
					       "soc" : "soc-orkut", "osm" : "europe_osm", \
					       "roadnet" : "roadNet-CA" }
		self.engine = "Generic"
		self.m_teps_switcher = {
			"BFS"	: lambda edges, elapsed: float(edges) / elapsed / 1000.0,
			"BC"	: lambda edges, elapsed: 2 * float(edges) / elapsed / 1000.0,
		}
	
	# Enumerate all possible input files in the given input path
	def EnumerateOutputFile(self):
		file_list = glob.glob(self.input_path)
		return file_list
	# A utility function to convert a string to another type (float, int, etc)
	# given the name of that type
	def ConvertToType(self, string, exp):
		if exp.find("{}") < 0:
			exp = exp + "({})"
		exp = exp.format("\"" + string + "\"")
		try:
			ret = eval(exp)
		except ValueError:
			ret = string
		return ret
	
	# Extract the dataset name from the input filename
	def GuessDatasetName(self, filename):
		filename = os.path.basename(filename)
		name_cleaner = re.compile('[\W_]+')
		alphanumerical_name = name_cleaner.sub('', filename).lower()
		for name in self.dataset_names:
			cleaned_name = name_cleaner.sub('', name).lower()
			if alphanumerical_name.find(cleaned_name) >= 0:
				if name in self.datasetname_translator:
					name = self.datasetname_translator[name]
				return name
		guessing_name = (re.findall('[a-zA-Z0-9]+', filename) or ["Unknown"])[0]
		print "Warning: Filename \"{}\" does not contain known dataset names.".format(filename)
		return guessing_name

	# Detect the alogrithm used in this output file. This can either from the output directly, or somewhere in path
	def DetectAlgorithm(self, param_dict, filename):
		if "algorithm" in param_dict:
			alg_string = param_dict["algorithm"]
		else:
			alg_string = filename
		alg = ""
		for possible_alg_name in self.possible_algs:
			if alg_string.upper().find(possible_alg_name) >= 0:
				alg = possible_alg_name
				break
		if alg and not "algorithm" in param_dict:
			param_dict["algorithm"] = alg
		if "algorithm" in param_dict:
			if param_dict["algorithm"] in self.algname_translator:
				param_dict["algorithm"] = self.algname_translator[param_dict["algorithm"]]
		return alg

	# Post-processing data, e.g., calculate m_teps
	def PostProcess(self, param_dict, filename):
		if ('edges_visited' in param_dict) and ('elapsed' in param_dict) \
		   and ('algorithm' in param_dict) and not ('m_teps' in param_dict):
			edges = param_dict['edges_visited']
			elapsed = param_dict['elapsed'] 
			m_teps = self.m_teps_switcher.get(
				param_dict['algorithm'], lambda e, t: float("nan"))(edges, elapsed)
			if not math.isnan(m_teps):
				param_dict['m_teps'] = m_teps
		return filename

	# Parse a single file using the given regex and store the extracted words in a dictionary
	def ParseSingleFile(self, filename):
		param_dict = {}
		with open(filename) as f:
			param_dict["rawfile"] = os.path.abspath(filename)
			for line in f:
				for r in self.regex_array:
					matched = r["regex"].match(" ".join(line.split()))
					if matched:
						for i in range(0, r["regex"].groups):
							k = r["keys"][i]["name"]
							o = self.ConvertToType(matched.group(i+1), r["keys"][i]["type"])
							if k in param_dict and isinstance(o, dict):
								param_dict[k].update(o)
							else:
								param_dict[k] = o
		param_dict["engine"] = self.engine
		return param_dict

	# Parse all file, with some post processing (calculate m_teps, etc)
	def Parse(self):
		file_list = self.EnumerateOutputFile()
		self.parsed_data = {}
		for filename in file_list:
			param_dict = self.ParseSingleFile(filename)
			param_dict['dataset'] = self.GuessDatasetName(filename)
			param_dict['time'] = time.ctime(os.path.getmtime(filename)) + '\n'
			self.DetectAlgorithm(param_dict, filename)
			filename = self.PostProcess(param_dict, filename)
			filename = os.path.basename(filename)
			update_filename = True
			for name in self.possible_algs:
				if filename.upper().find(name) >= 0:
					update_filename = False
			if update_filename and 'algorithm' in param_dict:
				if filename.upper().find(param_dict['algorithm'].upper()) < 0:
					filename = param_dict['algorithm'] + '-' + filename
			filename = os.path.splitext(os.path.basename(filename))[0]+'.json'
			self.parsed_data[filename] = param_dict
	
	# Write parsed results to JSON files		
	def WriteJSON(self, output_path = ""):
		self.Parse()
		if output_path:
			distutils.dir_util.mkpath(output_path)
		for filename, param_dict in self.parsed_data.iteritems():
			if output_path:
				p = os.path.join(output_path, filename)
				with open(p, 'w') as out:
					out.write(json.dumps(param_dict, sort_keys = True, indent = 4)+'\n')
			else:
				print json.dumps(param_dict, sort_keys = True, indent = 4)
	

# Parser class for parsing CuSha output
class GPUEngineOutputParserCuSha(GPUEngineOutputParserBase):
	def __init__(self, input_path):
		super(GPUEngineOutputParserCuSha, self).__init__(input_path)
		self.regex_array = [{   "regex": re.compile("Graph is populated with ([0-9]+) vertices and ([0-9]+) edges."),
					"keys" : [{ "name" : "vertices_visited", "type" : "int"}, 
						  { "name" : "edges_visited", "type" : "int"},
					 	 ]
				    },
				    {	"regex": re.compile("Processing finished in : (\d+(?:\.\d+)?) \(ms\)"),
					"keys" : [{ "name" : "elapsed", "type" : "float"}]
				    }
		]
		self.engine = "CuSha"

# Parser class for parsing MapGraph output
class GPUEngineOutputParserMapGraph(GPUEngineOutputParserBase):
	def __init__(self, input_path):
		super(GPUEngineOutputParserMapGraph, self).__init__(input_path)
		self.regex_array = [{	"regex": re.compile("Converting ([0-9]+) vertices, ([0-9]+) directed edges"),
					"keys" : [{ "name" : "vertices_visited", "type" : "int"}, 
						  { "name" : "edges_visited", "type" : "int"},
					 	 ]
				    },
				    {	"regex": re.compile("Wall time took: (\d+(?:\.\d+)?) ms"),
					"keys" : [{ "name" : "elapsed", "type" : "float"}]
				    },
				    {	"regex": re.compile("Device [0-9]: \"(.+)\""),
					"keys" : [{ "name" : "gpuinfo", "type" : "dict(name={})" }]
				    },
				    {	"regex": re.compile("Total amount of global memory: [0-9]+ MBytes \(([0-9]+) bytes"),
					"keys" : [{ "name" : "gpuinfo", "type" : "dict(total_global_mem={})" }]
				    },
				    {	"regex": re.compile("CUDA Driver Version / Runtime Version ([0-9]+\.[0-9]+) / ([0-9]+\.[0-9]+)"),
					"keys" : [{ "name" : "gpuinfo", "type" : "dict(driver_version=int(float({})*1000))"},
						  { "name" : "gpuinfo", "type" : "dict(runtime_version=int(float({})*1000))"}]
				    },
				    {	"regex": re.compile("Running on host: (.+)"),
					"keys" : [{ "name" : "sysinfo", "type" : "dict(nodename={})"}]
				    }
		]
		self.engine = "MapGraph"


# Parser class for parsing Ligra output
class GPUEngineOutputParserLigra(GPUEngineOutputParserBase):
	def __init__(self, input_path):
		super(GPUEngineOutputParserLigra, self).__init__(input_path)
		self.regex_array = [{	"regex": re.compile(".+ : (\d+(?:\.\d+)?)"),
					"keys" : [{ "name" : "elapsed", "type" : "1000*float"}]
				    }
		]
		self.engine = "Ligra"

# Parser class for parsing Hardwired BC output
class GPUEngineOutputParserHardwiredBC(GPUEngineOutputParserBase):
	def __init__(self, input_path):
		super(GPUEngineOutputParserHardwiredBC, self).__init__(input_path)
		self.regex_array = [{	"regex": re.compile("there are ([0-9]+) vertices ([0-9]+) edges"),
					"keys" : [{ "name" : "vertices_visited", "type" : "int"}, 
						  { "name" : "edges_visited", "type" : "int"},
						 ]
				    },
				    {	"regex": re.compile("kernel time: (\d+(?:\.\d+)?) secs"),
					"keys" : [{ "name" : "elapsed", "type" : "1000*float"}]
				    }
		]
		self.engine = "Hardwired-BC"


# Parser class for parsing Hardwired CC output
class GPUEngineOutputParserHardwiredCC(GPUEngineOutputParserBase):
	def __init__(self, input_path):
		super(GPUEngineOutputParserHardwiredCC, self).__init__(input_path)
		self.regex_array = [{	"regex": re.compile("Elapsed Time: (\d+(?:\.\d+)?)ms"),
					"keys" : [{ "name" : "elapsed", "type" : "float"}]
				    }
		]
		self.engine = "Hardwired-CC"
	def PostProcess(self, param_dict, filename):
		param_dict['algorithm'] = "CC"
		return filename
		

# Parser class for parsing Hardwired BFS output
class GPUEngineOutputParserHardwiredBFS(GPUEngineOutputParserBase):
	def __init__(self, input_path):
		super(GPUEngineOutputParserHardwiredBFS, self).__init__(input_path)
		self.regex_array = [{	"regex": re.compile(".*nodes visited: ([0-9]+), edges visited: ([0-9]+)"),
					"keys" : [{ "name" : "vertices_visited", "type" : "int"}, 
						  { "name" : "edges_visited", "type" : "int"},
						 ]
				    },
				    {	"regex": re.compile("\[Time \(ms\)\]: u: (\d+(?:\.\d+)?)"),
					"keys" : [{ "name" : "elapsed", "type" : "float"}]
				    },
				    {	"regex": re.compile("\[Rate MiEdges/s\]: u: (\d+(?:\.\d+)?)"),
					"keys" : [{ "name" : "m_teps", "type" : "float"}]
				    },
				    {	"regex": re.compile("Using device [0-9]: (.+)"),
					"keys" : [{ "name" : "gpuinfo", "type" : "dict(name={})"}]
				    }
		]
		self.engine = "Hardwired-BFS"

# Now let's get started parsing CuSha output files
cusha_input_path = "/data/Compare/CuSha/results/{}/*.txt"
cusha_output_path = "./CuSha-output"
cusha_available_algs = ["bfs", "pr", "sssp"]
for alg in cusha_available_algs:
	GPUEngineOutputParserCuSha(cusha_input_path.format(alg)).WriteJSON(cusha_output_path)


# parse MapGraph output files
mapgraph_input_path = "/data/Compare/MapGraph/Algorithms/results/{}/*.txt"
mapgraph_output_path = "./MapGraph-output"
mapgraph_available_algs = ["CC", "BFS", "PR", "SSSP"]
for alg in mapgraph_available_algs:
	GPUEngineOutputParserMapGraph(mapgraph_input_path.format(alg)).WriteJSON(mapgraph_output_path)

# parse Ligra output files
ligra_input_path = "/data/Compare/ligra_may22-2014/ppopp16/*-result"
ligra_output_path = "./Ligra-output"
GPUEngineOutputParserLigra(ligra_input_path).WriteJSON(ligra_output_path)

# parse Hardwired BC output files
bc_input_path = "/data/Compare/gpu_BC/ppopp16/*.txt"
bc_output_path = "./HardwiredBC-output"
GPUEngineOutputParserHardwiredBC(bc_input_path).WriteJSON(bc_output_path)

# parse Hardwired BFS output files
bfs_input_path = "/data/Compare/b40c/test/bfs/eval/PPOPP16/*.txt"
bfs_output_path = "./HardwiredBFS-output"
GPUEngineOutputParserHardwiredBFS(bfs_input_path).WriteJSON(bfs_output_path)

# parse Hardwired CC output files
cc_input_path = "/data/Compare/conn/test_results/*.txt"
cc_output_path = "./HardwiredCC-output"
GPUEngineOutputParserHardwiredCC(cc_input_path).WriteJSON(cc_output_path)



