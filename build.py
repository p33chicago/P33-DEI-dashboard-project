from p33py.output import (
    output_dir,
    metrics,
    scorecard,
    make_clean_output_directory,
)

output_dir("./output")

print("Removing ./output/ and recreating")
make_clean_output_directory()
print()

print("Writing scorecard")
scorecard()
print()

print("Writing metric figures")
metrics()
print()
