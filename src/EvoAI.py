from evo_init import Init 
from evo_eval import Eval
from evo_gp import GP

init = Init("test.ini")	# Read in the config file
evaluator = Eval( init.environment )
gp = GP()

population = init.new_pop()

print(population[0]["ind"])

for i in range( init.epochs):
	for b in range(init.btree_sims_per_epoch):
		evaluator.eval( population )
		gp.operate( population, "BTrees" )
	for t in range(init.actiontree_sims_per_epoch):
		evaluator.eval( population )
		gp.operate( population, "ActionTrees" )



