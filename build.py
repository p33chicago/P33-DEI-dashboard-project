from p33py.output import output_dir, figures, tables

output_dir('./output')
print('Writing figure JSON')
figures(format='json')
print()

print('Writing figure SVGs')
figures(format='svg')
print()

print('Writing tables')
tables()
