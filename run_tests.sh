#!/bin/bash

set -e
source .venv/Scripts/activate

pytest tests/

EXIT_CODE=$?

deactivate

if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
