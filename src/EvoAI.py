from evo_init import Init 
from evo_eval import Eval
from evo_gp import GP

init = Init("test.ini")	# Read in the config file
evaluator = Eval( init.parameters['environment'] )
gp = GP()

population = init.new_pop()

for i in range( int(init.parameters['epochs']) ):
	for b in range( int(init.parameters['btree_sims_per_epoch'])):
		evaluator.eval( population )
		gp.operate( population, "BTrees" )
	for t in range( int(init.parameters['actiontree_sims_per_epoch'])):
		evaluator.eval( population )
		gp.operate( population, "ActionTrees" )



