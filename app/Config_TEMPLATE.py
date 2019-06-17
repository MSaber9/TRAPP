######################################
# HOW TO USE THIS FILE
# Copy its contents to a file named ‘Config.py’ under the ‘app’ folder and fill in the missing paths
######################################

######################################
####### GENERAL CONFIGURATION ########
######################################

# True if we want to use the SUMO GUI
sumoUseGUI = True

# True for printing extra info
debug = False

log_overheads = True

log_utilizations = True

log_baseline_result = False

do_adaptation = True

do_EPOS_planning = True

multiple_car_routes = True

# which seed to be used in the random functions, for repeatability
random_seed = 1

# The path to EPOS jar that is called from Python for planning
# TODO
epos_jar_path = "<path to EPOS jar>"

######################################
#### CONFIGURATION OF SIMULATION #####
######################################

# The SUMO config (links to the network) we use for our simulation
# TODO
sumoConfig = "<path to SUMO cfg file>"

# The SUMO network file we use for our simulation
# TODO
sumoNet = "<path to SUMO net.xml file>"

# The total number of cars we use in our simulation
totalCarCounter = 500

# How long the simulation will run
simulation_horizon = 1000

######################################
##### CONFIGURATION OF PLANNING ######
######################################

# whether the simulation should start with an EPOS invocation
start_with_epos_optimization = True

# How frequently EPOS planning will be invoked (runtime-configurable parameter)
planning_period = 1000

# the number of steps to look in the future while planning
planning_steps = 1

# how long a planning step should be
planning_step_horizon = 100

# double from [0, 1], unfairness
alpha = 0

# double from [0, 1], selfishness or local objective
beta = 0
# unfairness + selfishness <= 1
# alpha*unfairness + beta*local_cost + (1-alpha-beta)*global_costs

# Suggested values : “XCORR”, VAR”, “RSS”, “RMSE”
globalCostFunction="VAR"

######################################
#### CONFIGURATION OF ADAPTATION #####
######################################

# how often adaptation should be triggered
adaptation_period = 1000

# the actual adaptation logic. Possible values: “load_balancing”, “avoid_overloaded_streets”, “tune_planning_resolution”
adaptation_strategy = "load_balancing"

###############################################
#### CONFIGURATION for Alpha/Beta Testing #####
###############################################

# the name of the folder where the alpha/beta testing output
# files(overheads and global and local cost), suggest naming it the city testing
resultsFolder= "eichstaedt"

#which experiment are you planning on running, current options: "alpha" or "beta"
# if this is anything else, it will output a file in 'data' folder
experiment_name="overheads"

######################################
#### CONFIGURATION OF Districts #####
######################################

#to use districts to select trip origins
use_districts = True

#run once with do_gridding to load in the district files and population probabilities, does not run a simulation
do_gridding = False

#the grid size for the network districts
districtSize = 1000

#the file containing the zip codes and their population
zipcodes = 'app/map/eichstaedt_zips.csv'

#city name, to store districts and TAZ in a folder under app/map, needs to be kept consistent for each city
city_name = 'city_name'
