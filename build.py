from p33py.output import (
    output_dir,
    figures,
    scorecard,
    make_clean_output_directory,
)

output_dir("./output")

print("Removing ./output/ and recreating")
make_clean_output_directory()
print()

print("Writing EI scorecard JSON")
scorecard()
print()

print("Writing figure SVGs and JSON")
figures()
print()
