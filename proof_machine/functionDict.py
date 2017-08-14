funDict = {
	# Inequality
	'cauchySchwarz': [cauchySchwarz, '<=', ''],
	'markov': [markov, '<=', ''],
	'chernoff': [chernoff, '<=', ''],
	'jensen': [jensen, '<=', ''],
	'concavity': [concavity, '<=', ''],

	# Equality
	'expSumToProduct': [expSumToProduct, '=', ''],
	'expProductToSum': [expProductToSum, '=', ''],
	'logProductToSum': [logProductToSum, '=', ''],
	'logSumToProduct': [logSumToProduct, '=', ''],

	'pInclusionExclusion': [pInclusionExclusion, '=', ''],
	'inclusionExclusion': [inclusionExclusion, '=', ''],
	'independencePullOut': [independencePullOut, '=', ''],

	'sumPushIn': [sumPushIn, '=', ''],
	'sumPullOut': [sumPullOut, '=', ''],

	'cupForwardAssociative': [cupForwardAssociative, '=', ''],
	'cupBackwardAssociative': [cupBackwardAssociative, '=', ''],

	'capForwardAssociative': [capForwardAssociative, '=', ''],
	'capBackwardAssociative': [capBackwardAssociative, '=', ''],

	'cupSimplify': [cupSimplify, '=', ''],
	'capSimplify': [capSimplify, '=', ''],

	'cupDeMorgan': [cupDeMorgan, '=', ''],
	'capDeMorgan': [capDeMorgan, '=', ''],

	'invariant': [invariant, '=', ''],
	'symmetry': [symmetry, '=', ''],
	'tautology': [tautology, '=', '']
}
