# Evolving Behavior Trees and Action Nodes Concurrently

The goal of this project is to investigate a method by which both behavior trees, and their action/leaf nodes can be evolved using genetic programming, at the same time.  

Typed genetic programming will be used over trees representing both the actual behavior trees, and the leaf nodes used by them, which represent small 'atomic' procedures that take place in the game environment.

Alternating sets of simulations will first evaluate a random set of behavior trees and action nodes.  A set of genetic operations will operate on just the behavior trees.  Then, a set of simulations will be performed, after which just the set of action nodes will have genetic operations performed on them.  These two sets of evaluation and operation will be performed for a set number of epochs.  

Hopefully, this will yeild a GP method that allows for an efficient search of both the game-action space, and the game-behavior space at the same time.  The coarse nature of the actions can be modified while also searching the broad domain of 'higher level' game-behavior space.  

Eventaully, this will include a form of speciation within the action node space.  Where placeholders in the behavior trees can refer to specific species of action program trees.  Then, the genetic operations in this action-program space can be tailored to minimize disruption of these species.  

The inital populations of trees will still use a notion of placeholder, with an ID that relates to a member of the action-program population.

Following the structure of behavior trees, all trees in the action-program population will return a value indicating 'pass' or 'fail', a single binary measure to be used by that programs parent node in the actual behavior tree.  
