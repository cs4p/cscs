# jhead
HEAD is a simple command line tool for displaying and some manipulation
of EXIF header data embedded in jpeg images from digital cameras.


https://github.com/Matthias-Wandel/jhead

# Installation
## MacOS
    brew install jhead
## Debian
    apt install jhead
## Script
    curl http://example.com/script.sh

# Examples

## Insert php code into the jpeg file
    jhead -ce file.jpg
The -ce option of jhead will launch a text editor to edit the comment section of the metadata.

We can then insert the following PHP code:
    <?php  echo 'Hello, world!'; __halt_compiler(); ?>

The __halt_compiler() instruction is used to stop parsing the rest of the JPG file.

The injected code will be executed if file.jpg is read as a PHP file. The most obvious way this can take place is by storing the file in the server using a php extension. See what happens when we access file.jpg.php.

# Help output
```
Jhead is a program for manipulating settings and thumbnails in Exif jpeg headers
used by most Digital Cameras.  v3.04 Matthias Wandel, Nov 22 2019.
http://www.sentex.net/~mwandel/jhead

Usage: jhead [options] files
Where:
 files       path/filenames with or without wildcards
[options] are:

GENERAL METADATA:
  -te <name> Transfer exif header from another image file <name>
             Uses same name mangling as '-st' option
  -dc        Delete comment field (as left by progs like Photoshop & Compupic)
  -de        Strip Exif section (smaller JPEG file, but lose digicam info)
  -di        Delete IPTC section (from Photoshop, or Picasa)
  -dx        Deletex XMP section
  -du        Delete non image sections except for Exif and comment sections
  -purejpg   Strip all unnecessary data from jpeg (combines -dc -de and -du)
  -mkexif    Create new minimal exif section (overwrites pre-existing exif)
  -ce        Edit comment field.  Uses environment variable 'editor' to
             determine which editor to use.  If editor not set, uses VI
             under Unix and notepad with windows
  -cs <name> Save comment section to a file
  -ci <name> Insert comment section from a file.  -cs and -ci use same naming
             scheme as used by the -st option
  -cl string Insert literal comment string
  -zt        Trim exif header trailing zeroes (Nikon 1 wastes 30k that way)

DATE / TIME MANIPULATION:
  -ft        Set file modification time to Exif time
  -dsft      Set Exif time to file modification time
  -n[format-string]
             Rename files according to date.  Uses exif date if present, file
             date otherwise.  If the optional format-string is not supplied,
             the format is mmdd-hhmmss.  If a format-string is given, it is
             is passed to the 'strftime' function for formatting
             %d Day of month    %H Hour (24-hour)
             %m Month number    %M Minute    %S Second
             %y Year (2 digit 00 - 99)        %Y Year (4 digit 1980-2036)
             For more arguments, look up the 'strftime' function.
             In addition to strftime format codes:
             '%f' as part of the string will include the original file name
             '%i' will include a sequence number, starting from 1. You can
             You can specify '%03i' for example to get leading zeros.
             This feature is useful for ordering files from multiple digicams to
             sequence of taking.
             The '.jpg' is automatically added to the end of the name.  If the
             destination name already exists, a letter or digit is added to
             the end of the name to make it unique.
             The new name may include a path as part of the name.  If this path
             does not exist, it will be created
  -a         (Windows only) Rename files with same name but different extension
             Use together with -n to rename .AVI files from exif in .THM files
             for example
  -ta<+|->h[:mm[:ss]]
             Adjust time by h:mm forwards or backwards.  Useful when having
             taken pictures with the wrong time set on the camera, such as when
             traveling across time zones or DST changes. Dates can be adjusted
             by offsetting by 24 hours or more.  For large date adjustments,
             use the -da option
  -da<date>-<date>
             Adjust date by large amounts.  This is used to fix photos from
             cameras where the date got set back to the default camera date
             by accident or battery removal.
             To deal with different months and years having different numbers of
             days, a simple date-month-year offset would result in unexpected
             results.  Instead, the difference is specified as desired date
             minus original date.  Date is specified as yyyy:mm:dd or as date
             and time in the format yyyy:mm:dd/hh:mm:ss
  -ts<time>  Set the Exif internal time to <time>.  <time> is in the format
             yyyy:mm:dd-hh:mm:ss
  -tf file   Set the exif time to the modicfation time from another file
  -ds<date>  Set the Exif internal date.  <date> is in the format YYYY:MM:DD
             or YYYY:MM or YYYY

THUMBNAIL MANIPULATION:
  -dt        Remove exif integral thumbnails.   Typically trims 10k
  -st <name> Save Exif thumbnail, if there is one, in file <name>
             If output file name contains the substring "&i" then the
             image file name is substitute for the &i.  Note that quotes around
             the argument are required for the '&' to be passed to the program.
             An output name of '-' causes thumbnail to be written to stdout
  -rt <name> Replace Exif thumbnail.  Can only be done with headers that
             already contain a thumbnail.
  -rgt[size] Regnerate exif thumbnail.  Only works if image already
             contains a thumbail.  size specifies maximum height or width of
             thumbnail.  Relies on 'mogrify' programs to be on path

ROTATION TAG MANIPULATION:
  -autorot   Invoke jpegtran to rotate images according to Exif orientation tag
             anc clear Exif orientation tag
             Note: Windows users must get jpegtran for this to work
  -norot     Zero out the rotation tag.  This to avoid some browsers from
             rotating the image again after you rotated it but neglected to
             clear the rotation tag

OUTPUT VERBOSITY CONTROL:
  -h         help (this text)
  -v         even more verbose output
  -q         Quiet (no messages on success, like Unix)
  -V         Show jhead version
  -exifmap   Dump header bytes, annotate.  Pipe thru sort for better viewing
  -se        Suppress error messages relating to corrupt exif header structure
  -c         concise output
  -nofinfo   Don't show file info (name/size/date)

FILE MATCHING AND SELECTION:
  -model model
             Only process files from digicam containing model substring in
             camera model description
  -exonly    Skip all files that don't have an exif header (skip all jpegs that
             were not created by digicam)
  -quality x Only work on images with JPEG quality factor x or higher
  -cmd command
             Apply 'command' to every file, then re-insert exif and command
             sections into the image. &i will be substituted for the input file
             name, and &o (if &o is used). Use quotes around the command string
             This is most useful in conjunction with the free ImageMagick tool.
             For example, with my Canon S100, which suboptimally compresses
             jpegs I can specify
                jhead -cmd "mogrify -quality 80 &i" *.jpg
             to re-compress a lot of images using ImageMagick to half the size,
             and no visible loss of quality while keeping the exif header
             Another invocation I like to use is jpegtran (hard to find for
             windows).  I type:
                jhead -cmd "jpegtran -progressive &i &o" *.jpg
             to convert jpegs to progressive jpegs (Unix jpegtran syntax
             differs slightly)
  -orp       Only operate on 'portrait' aspect ratio images
  -orl       Only operate on 'landscape' aspect ratio images
```
