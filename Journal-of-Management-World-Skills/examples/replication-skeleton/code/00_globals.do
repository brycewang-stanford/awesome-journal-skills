version 17

global root "."
global raw "$root/data/raw"
global intermediate "$root/data/intermediate"
global analysis "$root/data/analysis"
global output "$root/output"

cap mkdir "$intermediate"
cap mkdir "$analysis"
cap mkdir "$output/tables"
cap mkdir "$output/figures"

set seed 20260531
