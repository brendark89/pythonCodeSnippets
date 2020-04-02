quarterback_stats = {
    'Aaron Rodgers': {'COMP': 371, 'YDS': 4925, 'TD': 39, 'INT': 8},
    'Peyton Manning': {'COMP': 400, 'YDS': 4659, 'TD': 37, 'INT': 11},
    'Greg McElroy': {'COMP': 19, 'YDS': 214, 'TD': 1, 'INT': 1},
    'Matt Leinart': {'COMP': 16, 'YDS': 115, 'TD': 0, 'INT': 1}
}

print('2012 quarterback statistics:')

print('  Passes completed:')
for qb in quarterback_stats:
    comp = quarterback_stats[qb]['COMP']
    print('    %s: %d' % (qb, comp))  # Replace conversion specifiers
    # Hint: Use the conversion flag '-' to left-justify names

print('  Passing yards:')
for qb in quarterback_stats:
	comp = quarterback_stats[qb]['YDS']
	print('    %s: %d' % (qb, comp))
    # Hint: Use the conversion flag '-' to left-justify names

print('  Touchdown / interception ratio:')
for qb in quarterback_stats:
	td = quarterback_stats[qb]['TD']
	ints=quarterback_stats[qb]['INT']
	ratio=float(td)/float(ints)
	print('    %s: %.2f' % (qb, ratio))
	# Hint: Convert TD/INTs to float before calculating ratio 
