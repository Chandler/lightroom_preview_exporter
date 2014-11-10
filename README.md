!!only tested with Lightroom 4!!
 
This script extracts images from lightroom previews.

This can be a lifesaver if you lost your original photos but still have your lightroom metadata. 

This basic logic is:
  1. Run Unix 'Strings' over the lightroom catalog file to extract out the original filenames based on a questionable regex. 
  2. Scan the lightroom preview binaries for embedded jpegs and write out the largest one.

Alternatives: 
- A faster c program by @maxmouchet that doesn't attempt to preserve original filenames.
  https://github.com/maxmouchet/lrprev-extract
- An official lightroom plugin from Adobe that I had issues with.
  http://helpx.adobe.com/lightroom/kb/extract-previews-lightroom-4.html

Usage:

    ./run.sh path/to/lr/catalog path/to/lr/previews/dir

Example:

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

If you don't have a catalog file or don't care about restoring the original filenames, you can use the extract_image.py script directly on individual preview files.

    ./extract_image.py path/to/single/preview.lrprev output
