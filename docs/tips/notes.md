# Capturing notes and activities

## Using the script command

To capture output to a file:

    # Start logging immediately
    script output.txt
    # Your commands here
    # Exit logging with: exit
    
    # Or append to existing file
    script -a output.txt

## Using the `tee` command

The `tee` command is useful for duplicating output to both a file and standard output:

    # Redirect output to file and display on screen
    command | tee output.txt

    # Append to file and display on screen
    command | tee -a output.txt