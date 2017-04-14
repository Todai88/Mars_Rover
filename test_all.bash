#!/bin/bash

#
#
# A bash-script to run all the unittests
# It gives you an output in the end which will
# indicate if all the unittests finished without any issue.
#
#

function test_exit_code()
{

    echo "Test exit code = $2"
    if (( $2 == 0)); then
        ((count++))
    fi

}
function test_all()
{
    count=0
    echo ">>> Running rover_tests.py"
    python3 rover_tests.py
    test_exit_code "$count" "$?"
    #########
    echo ">>> Running mars_tests.py"
    python3 mars_tests.py
    test_exit_code "$count" "$?"
    #########
    echo ">>> Running main_tests.py"
    python3 main_tests.py
    test_exit_code "$count" "$?"
    #########
    echo "Finished running tests. $count/3 returned fine"
}

test_all
