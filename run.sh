# Path to the Lightroom Catalog file
export CATALOG=$1

# Path to the lightroom previews root directory
export PREVIEW_DIR=$2

# OPTIONAL -- Exported photos will be saved here
export OUTPUT_DIR=${3:-"photos"}

echo "Gathering image filenames from catalog"
strings "$CATALOG" | python uid_to_name.py

echo "Extracting best avaliable images from previews"
find "$PREVIEW_DIR" -name '*.lrprev' | xargs -I % -L1 -P4 python extract_image.py % "$OUTPUT_DIR"
