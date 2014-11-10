This script extracts images from lightroom previews, useful if you lost your originals but still have the lightroom metadata.

Example usage:

./run.sh $path_to_lr_catalog $path_to_lr_previews_dir

e.g.

➜ git:(master) ✗ ./run.sh \
/Users/cabraham/Pictures/Lightroom/Lightroom\ 4\ Catalog.lrcat \
/Users/cabraham/Pictures/Lightroom/Lightroom\ 4\ Catalog\ Previews.lrdata \

Gathering image filenames from catalog
Extracting best avaliable images from previews
writing: photos/DSC_8996.JPG
writing: photos/DSC_9961.JPG
writing: photos/DSC_9201.NEF
writing: photos/DSC_2232.JPG
...

If you don't have a catalog or don't care about restoring the original filenames, you can use the extract_image.py script directly on individal preview files.

./extract_image.py path/to/single/preview.lrprev output
