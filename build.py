from p33py.output import output_dir, figures, tables, equity_indices, make_clean_output_directory

output_dir('./output')

print('Removing ./output/ and recreating')
make_clean_output_directory()
print()

print('Writing EI JSON')
equity_indices()
print()

print('Writing figure JSON')
figures(format='json')
print()

print('Writing figure SVGs')
figures(format='svg')
print()

print('Writing tables')
tables()
