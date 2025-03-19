#!/usr/bin/env bash
# release.sh
# Example shell script to build & upload your package

set -e  # Exit immediately if a command exits with a non-zero status.

# 1) Remove old artifacts
rm -rf dist build *.egg-info

# 2) Build
python -m build

# 3) Upload
twine upload dist/*

# 4) (Optional) Remove old local version & reinstall from local
pip uninstall -y kashima
pip install .
